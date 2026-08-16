# V163 — V160 apparatus repair

## Status
Frozen before execution.

## Purpose
Repair only the malformed L2 fixture from V160. V160 wrote two structure fields on one line separated by `;`, which Lean rejected before the intended two-leaf requirement-multiplicity mechanism was exercised. No scientific target changes are permitted.

## Fixed apparatus
Use ordinary Lean structure syntax with one field per line:
```
structure V163P2 where
  A : Type
  B : Type
```
All other mechanisms match V160.

## Arms
All arms use K2 + K5 + exact frozen V156 and `derive_generator_with_requirements`.

- L1: one structure leaf, no constrained dependency. Must PASS.
- L2: two independent structure leaves, no constrained dependency. Must fail only at V156's frozen arity ceiling with `discovered 2`.
- D1: one structure leaf plus one missing constrained subproducer dependency. Must reproduce V160's valid `discovered 2` arity residual.
- Protected: full `lake build` and `lake test`.

## Verdicts
- `PASS_V163_PURE_TWO_LEAF_MULTIPLICITY_CONFIRMED`: L1 PASS, L2 arity failure count 2, D1 arity failure count 2, protected pass.
- `V163_PURE_TWO_LEAF_PATTERN_DIFFERS`: L1 valid but L2 does not show the frozen count-2 arity ceiling.
- `R10_*`: fixture/setup/protected distortion.

## Claim boundary
A PASS establishes that pure two-leaf multiplicity independently exceeds V156's singleton operator. It also shows cardinality alone does not distinguish pure leaf multiplicity from leaf+dependency, because D1 has the same count. It does not admit V162 or dependency closure by itself; it only satisfies V162's execution precondition.
