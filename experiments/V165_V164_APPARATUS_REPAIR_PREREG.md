# V165 — V164 apparatus repair

## Status
Frozen before execution.

## Why V164 is R10
V164's scientific ablations reproduced, but its intervention script exited before changing core because a shared source anchor occurred twice. The workflow piped the script through `tee` without `pipefail`, masking the failure and causing unchanged baseline code to be re-tested. Therefore V164's apparent negative is invalid apparatus evidence.

## Repair boundary
Preserve V164's exact scientific candidate and all fixtures. Change only:
1. target the first occurrence of the known shared standalone-source anchors instead of requiring global uniqueness;
2. execute the patch script without a masking pipeline and require its success marker;
3. verify a non-empty candidate diff exists before intervention execution.

No semantic change to `LIVE_OUTPUT_TYPE_RECONSTRUCTION` is permitted.

## Frozen gates
Same as V164:
- D0 and D1 ablations reproduce FREE_FVAR.
- candidate applies and core builds.
- D0 intervention PASS.
- D1 and recursive structure-projection family move past FREE_FVAR.
- plain-type control PASS.
- protected full build/test PASS.

## Verdicts
- `PASS_V165_LIVE_OUTPUT_TYPE_RECONSTRUCTION_CAUSAL`: all gates pass.
- `NEGATIVE_V165_RECONSTRUCTION_NOT_SUFFICIENT`: candidate genuinely applies but targeted FREE_FVAR persists.
- `R10_*`: any patch/apply/fixture/protected distortion.

## Claim boundary
Source-informed stale output-type binder repair only. No requirement/dependency/novelty claim.
