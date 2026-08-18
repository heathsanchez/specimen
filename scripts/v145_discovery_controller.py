from __future__ import annotations
import argparse, json, random, subprocess, time
from pathlib import Path

CANDIDATES = ["none", "input", "output", "both", "all"]
# Independent semantic classifier: preservation decision on boolean cases
# ordered (inputDetermined,inOutputType) = 00,01,10,11.
TRUTH = {
    "none":  [0,0,0,0],
    "input": [0,0,1,1],
    "output":[0,1,0,1],
    "both":  [0,0,0,1],
    "all":   [1,1,1,1],
}
O2_TRUTH = [0,0,0,1]

p = argparse.ArgumentParser()
p.add_argument("--arm", choices=["D", "D_O1"], required=True)
p.add_argument("--seed", type=int, required=True)
p.add_argument("--out", required=True)
a = p.parse_args()

root = Path.cwd()
source = Path("Specimen/DeriveConstrainedProducer.lean")
pristine = subprocess.check_output(["git","show","HEAD:Specimen/DeriveConstrainedProducer.lean"], text=True)
order = CANDIDATES[:]
random.Random(a.seed).shuffle(order)
records = []
first = None

def run(cmd, logname, timeout=240):
    t0=time.time()
    try:
        cp=subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout)
        rc=cp.returncode; out=cp.stdout
    except subprocess.TimeoutExpired as e:
        rc=124; out=(e.stdout or "") + "\nTIMEOUT\n"
    Path(logname).write_text(out)
    return rc, time.time()-t0

for idx, cand in enumerate(order, 1):
    source.write_text(pristine)
    prep_rc = 0
    prep_log = []
    if a.arm == "D_O1":
        cp=subprocess.run(["python","scripts/v120_apply_binder_aware_fixed_parameter.py"], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        prep_rc=max(prep_rc,cp.returncode); prep_log.append(cp.stdout)
    cp=subprocess.run(["python","scripts/v145_apply_candidate.py",cand], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    prep_rc=max(prep_rc,cp.returncode); prep_log.append(cp.stdout)
    Path(f"attempt_{idx}_{cand}_prep.log").write_text("\n".join(prep_log))
    build_rc, build_s = run(["lake","build","Specimen"], f"attempt_{idx}_{cand}_build.log") if prep_rc==0 else (prep_rc,0)
    target_rc, target_s = run(["lake","env","lean","SpecimenTest/V145O1O2Target.lean"], f"attempt_{idx}_{cand}_target.log") if build_rc==0 else (build_rc,0)
    protected_rc, protected_s = (999,0)
    if target_rc == 0:
        protected_rc, protected_s = run(["lake","build","SpecimenTest"], f"attempt_{idx}_{cand}_protected.log", timeout=420)
    qualified = target_rc == 0 and protected_rc == 0
    rec = {
        "evaluation":idx,"candidate":cand,"truth_table":TRUTH[cand],
        "o2_equivalent":TRUTH[cand]==O2_TRUTH,
        "prep_rc":prep_rc,"build_rc":build_rc,"target_rc":target_rc,
        "protected_rc":protected_rc,"qualified":qualified,
        "seconds":round(build_s+target_s+protected_s,3)
    }
    records.append(rec)
    if qualified:
        first=rec
        break

source.write_text(pristine)
result={
    "arm":a.arm,"seed":a.seed,"budget":5,"order":order,
    "evaluated":len(records),"records":records,
    "first_qualified":first,
    "discovered_o2": bool(first and first["o2_equivalent"]),
}
Path(a.out).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps(result,sort_keys=True))
