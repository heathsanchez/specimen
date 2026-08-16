# V153 — exact-bridge old-closure separator

Frozen before any V153 outcome is inspected.

## Why this is required
V152 proved that the named-definition residual is specifically typeclass transparency across a dependent projection: `Arbitrary Unit`, literal projection, and `abbrev` all synthesize; a named `def P0 := ⟨Unit⟩` does not; an exact bridge `Arbitrary P0.Meta := by change Arbitrary Unit; infer_instance` restores synthesis.

V140/V142 did not include that exact normalized concrete bridge. Therefore K6 cannot be called a new constructor until the strongest old-language composition is tested.

## No core intervention
V153 uses only the exact admitted K2 and K5 baseline. It does not apply V148 or V150 and does not edit Specimen source.

## Frozen family
`P` has a dependent field `Meta : Type`; `P0 : P := ⟨Unit⟩`; `Box p` stores `p.Meta`; `Has` witnesses the box.

## Arms
C0 — direct fixed Specimen derivation, no bridge. Must replay the non-fvar barrier.
C1 — generic Specimen derivation, no bridge. Must replay the symbolic-instance barrier.
C2 — exact concrete bridge `Arbitrary P0.Meta`, then direct fixed Specimen derivation.
C3 — exact concrete bridge, then generic Specimen derivation with an explicit instance binder `[Arbitrary p.Meta]`, then fixed `#synth` at P0.
C4 — old-language manual conditional producer `[Arbitrary p.Meta]` plus the exact bridge, then fixed `#synth` at P0.
C5 — old-language direct specialized producer at P0, then fixed `#synth`.

## Frozen interpretation
- If C0/C1 controls do not replay, R10.
- If C2 passes, the direct fixed residual was only missing the bridge and K6 is rejected.
- If C3 passes, existing Specimen parameterization + exact bridge suffices and K6 is rejected.
- If C2/C3 fail but C4/C5 pass, Lean has expressive closure but Specimen lacks an automated derivation mechanism. This licenses only an **automation/operator** candidate, not a claim of new semantic expressivity.
- If C4/C5 fail, V152's result failed to transfer to the exact frozen family and no K6 is licensed.

Protected `lake build` and `lake test` must remain green because there is no core intervention.

Claim boundary: this experiment distinguishes old Specimen closure, old Lean expressive closure, and missing derivation automation. It cannot by itself establish constructor development or open-ended development.