# V168 — Post-V166 pinned external frontier

## Status
Frozen before V166 outcome. Do not execute unless V166 is admitted under its frozen gates.

## External source
Exact same upstream source identity as V158:
- repository `strata-org/specimen`
- PR #47 head commit `da0e21613e9d18d44fe0f54e05ea003699a1adc0`
- fixture `SpecimenTest/DeriveArbitrarySuchThat/DeriveStructParamGenerator.lean`
- blob `b20b11e33026d2a69a4d715f44f3b5e564d5fc75`

## Question
If finite transport of the complete already-discovered requirement set is admitted, does that alone close the independently authored STLC fixture, or does the fixture still require automatic discharge/derivation of constrained dependencies?

## Frozen intervention
Apply only:
- K2 + K5;
- exact admitted V156;
- exact V166 finite-requirement transport, unchanged from admission.

Use the same V158 standalone adaptation boundary: preserve upstream definitions, exact generator target, and generator runtime check; replace only the original mutual generator/enumerator invocation by standalone `derive_generator_with_requirements`; remove only the enumerator path.

No V168-specific core change is allowed.

## Frozen outcomes
- `PASS_V168_FINITE_TRANSPORT_EXTERNAL_TRANSFER`: exact source verifies, adapted external generator + runtime PASS, protected build/test PASS.
- `PASS_V168_EXTERNAL_DEPENDENCY_DISCHARGE_RESIDUAL`: source verifies, finite transport gets past the V156 arity ceiling but external arm fails specifically because one or more transported constrained-producer premises cannot be synthesized/discharged; protected PASS.
- `NEGATIVE_V168_OTHER_EXTERNAL_RESIDUAL`: source verifies and finite transport gets past arity, but a different non-R10 residual remains.
- `R10_*`: source/adaptation/setup/protected distortion.

## Claim boundary
A dependency-discharge residual would identify the next capability boundary only. It would not license a discharge operator until a separate decomposition, candidate, ablation, held-out transfer, and protected gate are passed. A full transfer PASS would still not establish external novelty because upstream PR #47 already contains a broader solution family.
