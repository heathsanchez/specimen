# V160 — Requirement-set decomposition

## Status
Frozen before execution and independently of V159 outcome.

## Motivation
V158's pinned external standalone target exposed five discovered requirements, but diagnostics show the set mixes at least two semantic kinds: unconstrained structure-leaf requirements (`Arbitrary P.info.Metadata`, `Arbitrary P.VarId`) and constrained subproducer dependencies (`Lookup`, paired `HasType`). Before generalizing V156 beyond singleton arity, isolate those mechanisms.

## Frozen arms
All arms use K2 + K5 + exact frozen V156 and `derive_generator_with_requirements`. We inspect only the V156 arity residual; no implementation changes are permitted.

### L1 — one leaf, no constrained dependency
One structure field `A : Type`; one constructor consumes `A`.
Expected discovered requirement count: 1; V156 elaborates.

### L2 — two leaves, no constrained dependency
Structure fields `A B : Type`; one constructor consumes both.
Expected: V156 arity residual with count 2. This isolates pure leaf multiplicity.

### D1 — one leaf plus one constrained producer dependency
Structure field `A : Type`. The target constructor consumes an `A` and a witness generated through a separate relation over `Nat` for which no constrained producer is in scope.
Expected: arity >1 or a distinct dependency residual. This isolates dependency closure from leaf multiplicity.

## Verdicts
- `PASS_V160_PURE_LEAF_MULTIPLICITY_ISOLATED`: L1 PASS, L2 is arity=2, D1 demonstrates a requirement/dependency set distinct from L2.
- `V160_LEAF_MULTIPLICITY_NOT_ISOLATED`: L1/L2 do not produce the frozen pattern.
- `R10_*`: malformed fixtures or protected failure.

## Claim boundary
Mechanism decomposition only. No multi-requirement operator is admitted by this experiment.
