# V155 — standalone instance-context old-closure separator

Frozen before any V155 outcome is inspected and before any additive derivation operator is constructed.

## Residual
V153 proved expressive closure but missing Specimen automation: direct/generic Specimen routes fail, while a manual conditional producer plus an exact normalized bridge succeeds. V154 attempted section-local context but was R10 because the standalone command did not resolve the section variable `p` at all.

V155 tests the strongest remaining old-operator rival without relying on implicit section capture.

## No core intervention
Apply only exact admitted K2 and K5. No V148/V150 or new source changes.

## Frozen family
`P` has dependent field `Meta : Type`; named `def P0 := ⟨Unit⟩`; transparent `abbrev PA := ⟨Unit⟩`; `Box p` stores `p.Meta`; `Has` witnesses the box.

## Arms
T0 — ordinary standalone generic derivation with no instance binder. Must replay `SYMBOLIC_INSTANCE`.

T1 — standalone explicit instance-binder derivation:
`derive_generator (fun (p : P) [inst : Arbitrary p.Meta] => ∃ b : Box p, Has b)`.
No bridge and no fixed synth. This asks only whether standalone can carry the explicit instance binder into the generated body.

T2 — same T1 derivation, plus the exact V152 bridge `Arbitrary P0.Meta`, then fixed `#synth ArbitrarySizedSuchThat (Box P0) ...`.

T3 — same T1 derivation, then fixed synth at transparent `abbrev PA` with no explicit bridge.

T4 — section-context syntax repaired with `include p` and `include inst`, then standalone derivation specialized to section variable. If Lean rejects `include` or the custom command still cannot resolve `p`, classify this arm as section-context unavailable, not scientific failure.

## Frozen interpretation
- T0 control fails to replay => R10.
- T1 PASS and (T2 or T3) PASS => existing standalone operator composition suffices: reject any new derivation operator claim.
- T1 PASS but T2/T3 fail => standalone carries the premise but cannot install a reusable fixed-specializable producer; old standalone closure remains incomplete.
- T1 fails with `failed to synthesize Arbitrary p.Meta` after the explicit binder is accepted => explicit standalone instance-binder rival is killed.
- T1 fails at command parsing/binder syntax => R10 for T1; no claim.
- T4 unknown-identifier/section rejection is recorded separately and cannot rescue or condemn T1–T3.

Protected `lake build` and `lake test` must remain green. No result here establishes new Lean expressivity, constructor development, or open-ended development.