# V142 — Instance-scoped old-closure result

Controller: Rigorous Breakthrough Stack v1.1
GitHub Actions run: 31939138908
Artifact: v142-instance-scoped-old-closure, ID 9261549250, SHA256 d5c19fdf07d72dabdc68f3722e25ff2077187b691ff5b4d6abe5288e5b0a34dd

## Frozen observations

- Exact admitted K2+K5 applied and built.
- T0_DIRECT: `NON_FVAR_APPLICABILITY` — `V142P0 is expected to be a variable.`
- T1_PARAM_NO_INSTANCE: `SYMBOLIC_INSTANCE` — failed to synthesize `Plausible.Arbitrary p_1.Meta`.
- T2_PARAM_INSTANCE_BINDER: `SYMBOLIC_INSTANCE` — the same failure despite an actual instance-implicit lambda binder `[inst : Plausible.Arbitrary p.Meta]`.
- T3_FIXED_SPECIALIZATION: derivation retained the same symbolic-instance failure; specialization was not established.
- Full repository build/test under exact K2+K5: PASS.

Frozen gates: S1=true, S2=true, S3=true, S4=false, S5=false, S6=true.
Frozen verdict: `OLD_CLOSURE_INSTANCE_SCOPE_OBSTRUCTION`.

## Stack classification

This kills the narrow rival that V140 failed only because the capability proof was an ordinary argument. A genuine instance-implicit lambda binder also does not survive into the relevant symbolic synthesis context.

It still does **not** earn K6. Before invention, one existing lawful mechanism remains: Specimen already supports instance parameters that are part of the inductive relation itself. That relation-instance transport is therefore the next closure separator (V143).

No result here establishes constructor development, multi-generation development, recursive development, open-ended development, or operator invention.