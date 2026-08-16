# V156 — Requirement Provenance Separator Precommit

## Residual
V153 proved that threading a missing unconstrained requirement such as `Arbitrary p.Meta` into both the outer generated instance and the inner auxiliary function can causally rescue a scoped dependent generator, including a source-distinct held-out family. V155 proved that promoting the entire flattened requirement array is not admissible: primary/held-out remained rescued but protected tests failed broadly.

Source inspection gives a pre-existing semantic distinction that V155 erased:
- `MExp.unconstrainedProducer` records ordinary producer requirements (`Arbitrary T` / `Enum T`).
- `MExp.constrainedProducer` separately records constrained-producer advisories (`ArbitrarySizedSuchThat _ ...` / `EnumSizedSuchThat _ ...`), which intentionally contain a placeholder target and are meant to resolve at their use site.
- Existing protected documentation for instance-implicit relation parameters says these are resolved by typeclass synthesis rather than generated.

## Question
Is the V153 mechanism valid when promotion preserves requirement provenance and promotes only requirements originating from unconstrained producers, while constrained-producer requirements remain advisory/use-site obligations?

## Frozen intervention
1. Replace the flattened compile-schedule requirement state with records carrying exactly:
   - the original requirement term syntax;
   - origin = `unconstrained` or `constrained`.
2. Tag requirements only at their existing creation sites. Do not change schedule search, scoring, MExp semantics, generated producer calls, or typeclass synthesis.
3. At final standalone constrained-producer emission, collect only `unconstrained` requirement terms, deduplicate them, and thread those terms into BOTH:
   - the outer generated instance;
   - the inner auxiliary producer's parameter scope.
4. Leave all `constrained` requirements unpromoted. They remain exactly where the existing generated call requests synthesis.
5. No string inspection, no `_` filtering, no source/test names, no Cedar special case, and no success-based filtering.

## Frozen tests
A. V153 primary projected-type fixture.
B. V153 source-distinct held-out projected-type fixture.
C. Valid two-unconstrained-requirement fixture with two dependent type fields, written with standard multiline Lean structure syntax.
D. `SpecimenTest/DeriveArbitrarySuchThat/InstanceParameterTest.lean` as a small protected separator because its documented invariant explicitly distinguishes synthesis-resolved instance parameters.
E. `SpecimenTest/DeriveArbitrarySuchThat/MutuallyRecursiveRelationsTest.lean` as a second protected separator.
F. Full `lake build` and `lake test`.
G. Ablation: K2+K5 baseline without V156 must retain V153 primary symbolic-instance failure.

## Gates
G1 baseline primary = SYMBOLIC_INSTANCE.
G2 primary passes after V156.
G3 source-distinct held-out passes.
G4 valid two-unconstrained-requirement fixture passes.
G5 InstanceParameterTest passes.
G6 MutuallyRecursiveRelationsTest passes.
G7 full protected build and test pass.
G8 ablation restores baseline failure.
G9 implementation is generic and provenance-based; no syntactic text filter or domain/test special case.

## Verdicts
- `PASS_V156_PROVENANCE_PROMOTION_ADMITTED_SCOPED` iff G1..G9 pass.
- `NEGATIVE_V156_PROVENANCE_PROMOTION_NOT_ADMITTED` for a scientific gate failure after the intervention executes.
- `R10_V156_INCONCLUSIVE` only if apparatus prevents a frozen gate from executing.

## Claim boundary
A pass earns scoped provenance-preserving requirement promotion only. It still does not establish constructor development. Constructor development requires a separately frozen later-frontier causal-dependence experiment in which this newly admitted capability is necessary for a later capability or task that the admitted pre-V156 constructor cannot reach.
