# V142 — Instance-scoped old-closure separator

Frozen: 2026-08-16 NZST
Controller: Rigorous Breakthrough Stack v1.1
Parent hard evidence: V139 + V140 only.

## Question

Does the strongest still-live lawful old-language closure solve the V139 fixed-index residual without adding any new derivation-engine constructor mechanism?

V140 established that parameterizing the concrete index crosses the `NON_FVAR_APPLICABILITY` boundary, but its apparatus correction supplied the downstream `Arbitrary p.Meta` proof as an ordinary explicit lambda input. That did not put the proof in Lean's typeclass context. Therefore V140 did not test the intended instance-scoped rival.

## Frozen old-language candidate

Use exact admitted K2+K5 and no other mutation of `Specimen/DeriveConstrainedProducer.lean`.

Represent the concrete fixed-index target by:

1. lifting `P0` to a lambda-bound free variable `p : P` at the derive surface;
2. binding the already-required capability as an **instance-implicit lambda binder** `[inst : Plausible.Arbitrary p.Meta]`;
3. deriving the unchanged `Box p` / `Has` relation;
4. specializing/synthesizing the resulting capability at the original `P0`, where `P0.Meta = Unit` and the ordinary existing `Arbitrary Unit` instance is available.

No source-specific axiom, global fabricated `Arbitrary`, target-specific engine patch, or protected evidence is permitted.

## Frozen arms

- T0_DIRECT: direct concrete `P0` target; must replay `NON_FVAR_APPLICABILITY`.
- T1_PARAM_NO_INSTANCE: parameterized `p` without instance binder; must replay `SYMBOLIC_INSTANCE`.
- T2_PARAM_INSTANCE_BINDER: parameterized `p` with `[inst : Plausible.Arbitrary p.Meta]`. This is the decisive old-language closure arm.
- T3_FIXED_SPECIALIZATION: same T2 derivation plus `#synth ArbitrarySizedSuchThat (Box P0) (fun b => Has b)`.

## Gates

S1 exact K2+K5 module build.
S2 T0 = `NON_FVAR_APPLICABILITY`.
S3 T1 = `SYMBOLIC_INSTANCE`.
S4 T2 = PASS.
S5 T3 = PASS.
S6 full repository build/test after exact K2+K5 = PASS.

## Verdicts

- `REJECT_K6_OLD_CLOSURE_SUFFICES` iff S1–S6 all hold. The V139 fixed-index residual is then solvable through existing lawful composition; K6 is not licensed for it.
- `OLD_CLOSURE_INSTANCE_SCOPE_OBSTRUCTION` iff S1–S3 and S6 hold, the instance-implicit syntax elaborates normally, but T2 or T3 fails at a semantic/derivation boundary. This closes the strongest currently identified old-language rival but still does not itself earn K6; the next smallest structural separator must identify the remaining invariant before construction.
- Parser/runner/build/tooling failure before the scientific arm reaches the derivation mechanism is R10 and carries no semantic conclusion.

## Claim boundary

Even a full PASS only rejects K6 for this residual. It does not establish constructor development, multi-generation development, recursive development, open-ended development, or operator invention.