# V151B — Fixed capability synthesis separator

Frozen 2026-08-16 NZST under Rigorous Breakthrough Stack v1.1 before any V151B outcome.

V151A established that adding a correctly scoped dependent premise lets both primary and held-out instance bodies elaborate through their calls to `Plausible.Arbitrary.arbitrary`; only the final fixed-value `#synth ArbitrarySizedSuchThat ...` failed.

Remaining rivals:
1. the underlying fixed projected capabilities (`Arbitrary Unit`, `Arbitrary Bool`, or the reduced projections `P0.Meta`, `Q0.Carrier`) are unavailable;
2. those capabilities exist, but typeclass search cannot use the generic dependent relation instance at the fixed projected target.

V151B is diagnostic only. No Specimen source is modified.

Frozen checks:
- `#synth Plausible.Arbitrary Unit`
- `#synth Plausible.Arbitrary Bool`
- define `P0 := ⟨Unit⟩`, then `#synth Plausible.Arbitrary P0.Meta`
- define `Q0 := ⟨Bool⟩`, then `#synth Plausible.Arbitrary Q0.Carrier`
- define a minimal class `Witnessed (p : P)` and generic instance `{p : P} [Plausible.Arbitrary p.Meta] : Witnessed p`; test `#synth Witnessed P0`; repeat held-out Q family.

Interpretation:
- if direct fixed projected `Arbitrary` synthesis fails, V151/V151A concrete gates were apparatus-invalid for testing rebinding and no K6 conclusion follows;
- if direct projected synthesis passes but the minimal dependent class fails, the residual is typeclass applicability/matching at dependent fixed targets;
- if both pass, the residual is specific to the `ArbitrarySizedSuchThat` relation/predicate instance shape.

No K6, constructor-development, or later-frontier claim can be earned by V151B.