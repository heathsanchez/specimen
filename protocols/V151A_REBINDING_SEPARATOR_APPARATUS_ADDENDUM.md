# V151A — Rebinding separator apparatus-only binder repair

Frozen 2026-08-16 NZST under Rigorous Breakthrough Stack v1.1 before any V151A outcome.

V151's REBOUND fixture bodies elaborated past the dependent `Plausible.Arbitrary.arbitrary` use, but the final concrete `#synth` failed. Inspection of the frozen fixture shows the relation parameter was declared as an **explicit** instance argument `(p : V151P)` / `(q : V151Q)`. Typeclass search does not invent explicit arguments for candidate instances, so the concrete `#synth` gate did not test the intended mechanism.

This is an R10 fixture/apparatus defect. No semantic conclusion is taken from V151's nominal NEGATIVE verdict.

V151A changes only the parameter binder on the REBOUND and BASE instance declarations from explicit `(p : P)` / `(q : Q)` to implicit `{p : P}` / `{q : Q}`. All types, bodies, dependent instance premises, fixed values, families, imports, PASS gates and protected baseline checks remain unchanged.

PASS requires the same V151 gates:
- BASE A/B fail specifically for missing dependent `Arbitrary`;
- REBOUND A/B compile and their concrete fixed-value `#synth` succeeds;
- untouched protected `lake build` and `lake test` pass.

A PASS confirms only the scoped rebinding/premise-sufficiency rival and licenses a binding-aware K6 intervention. It does not earn K6 or constructor development.