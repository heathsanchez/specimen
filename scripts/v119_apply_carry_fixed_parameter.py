from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()
old = '''    let (ctorName, args) := e.getAppFnArgs
    let mut actualArgs := #[]
    for arg in args do
'''
new = '''    let (ctorName, args) := e.getAppFnArgs
    -- V119 CARRY_FIXED_PARAMETER: uniform inductive parameters are already
    -- carried by the target family.  Constructor applications include those
    -- parameters in their fully elaborated Expr spine, but generated constructor
    -- syntax must not re-apply them as constructor fields.  Indices / explicit
    -- constructor arguments remain after `numParams` and are preserved.
    let fixedParamCount ←
      match (← getConstInfo ctorName) with
      | .ctorInfo info => pure info.numParams
      | _ => pure 0
    let mut actualArgs := #[]
    for arg in args.toList.drop fixedParamCount do
'''
if old not in text:
    raise SystemExit("V119 patch anchor not found")
if text.count(old) != 1:
    raise SystemExit(f"V119 patch anchor count != 1: {text.count(old)}")
path.write_text(text.replace(old, new, 1))
