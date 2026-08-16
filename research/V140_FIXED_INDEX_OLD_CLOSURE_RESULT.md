# V140 — Fixed-index old-closure result

Controller: Rigorous Breakthrough Stack v1.1
Scientific run: GitHub Actions 31938953614
Branch head tested: b8b8fcc440ee92546bbc0daa4681823687c6244f

## Frozen result

- Exact admitted K2+K5 applied and `Specimen.DeriveConstrainedProducer` built.
- `C0_DIRECT_CONST`: `NON_FVAR_APPLICABILITY` — `V140P0 is expected to be a variable.`
- `C1_PARAM_NO_INSTANCE`: `SYMBOLIC_INSTANCE` — failed to synthesize `Plausible.Arbitrary p_1.Meta`.
- `C2_PARAM_WITH_INSTANCE`: `SYMBOLIC_INSTANCE` — the same synthesis failure.
- `C3_FIXED_SPECIALIZATION`: the derive command retained the same symbolic-instance failure, so fixed specialization was not established.
- Full repository protected build/test after exact K2+K5: PASS (`BUILD=0`, `TEST=0`).

Frozen workflow gates: B1=true, B2=true, B3=true, B4=false, B5=false, B6=true. The workflow therefore emitted `PASS_V140_OLD_CLOSURE_EXHAUSTED_FOR_FROZEN_FAMILY`.

## Controller interpretation

That literal bounded-family verdict must **not** be promoted to “old closure is exhausted in general” or “K6 is required.” The apparatus correction after the first R10 run changed the intended typeclass assumption `[Plausible.Arbitrary p.Meta]` into an ordinary lambda input `(_inst : Plausible.Arbitrary p.Meta)`. Such an ordinary argument is not an instance-implicit binder, so the run did not actually test the strongest preregistered old-language rival: parameterize the fixed index while making the already-required downstream capability available in the local typeclass context.

Therefore the hard evidence is:

1. parameterization crosses the V139 `NON_FVAR_APPLICABILITY` boundary;
2. the next observed residual is symbolic typeclass synthesis for `p.Meta`;
3. an ordinary proof-object argument does not discharge that synthesis requirement;
4. exact K2+K5 preserve the protected repository suite.

## Classification

`V140 = PARTIAL CLOSURE / NEW SEPARATOR REQUIRED`.

The K6-invention claim remains **unearned**. The next smallest decision-changing experiment is a properly instance-scoped old-language arm using an instance-implicit lambda binder, followed by explicit specialization back to `P0`, with no derivation-engine mutation beyond exact K2+K5.

The first V140 workflow run (31938842310) is R10 only because section-bound variables were invisible to the command elaborator; it carries no semantic conclusion.

No result here establishes constructor development, recursive development, open-ended development, or operator invention.