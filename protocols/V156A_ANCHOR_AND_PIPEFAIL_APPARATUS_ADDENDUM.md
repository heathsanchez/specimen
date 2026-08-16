# V156A — Anchor Specificity and Pipefail Apparatus Addendum

## Classification of V156 attempt 1
R10 apparatus / non-executed intervention.

The frozen V156 scientific intervention did not execute. `scripts/v156_apply_requirement_provenance_promotion.py` aborted at:

`V156 unconstrained push anchor count != 1: 2`

because a suffix intended to identify the unconstrained-producer requirement push appears in both the unconstrained and constrained producer blocks. The workflow then continued because the intervention command was piped through `tee` without `pipefail`, masking the Python process's nonzero exit.

Therefore the nominal `NEGATIVE_V156_PROVENANCE_PROMOTION_NOT_ADMITTED` verdict is void. The observed primary/held-out/multi failures and protected green state are baseline-like apparatus outcomes, not evidence about provenance-preserving promotion.

## Only licensed repairs
1. Replace the two requirement-push sites using larger, function-local exact blocks that uniquely distinguish `unconstrainedProducer` from `constrainedProducer`.
2. Add `set -o pipefail` to the workflow intervention step so any script failure aborts the scientific run.
3. Add an explicit post-apply assertion that the transformed source contains both provenance tags and the emitter/derive threading markers before building.

## Frozen scientific content unchanged
No change is permitted to:
- V156 question or hypothesis;
- provenance categories (`unconstrained`, `constrained`);
- which category is promoted (only `unconstrained`);
- outer/inner placement;
- deduplication;
- primary, held-out, corrected multi, InstanceParameter, mutual, or full protected fixtures;
- ablation;
- gates G1..G9;
- claim boundary.

After these apparatus repairs, rerun the complete V156 protocol from the frozen baseline.
