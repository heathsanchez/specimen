# V158 — Upstream PR #47 external frontier

## Status
Frozen before V157 outcome inspection.

## External source
- Repository: `strata-org/specimen`
- PR: #47, created 2026-07-08, still open at freeze time.
- PR head commit: `da0e21613e9d18d44fe0f54e05ea003699a1adc0`
- Fixture: `SpecimenTest/DeriveArbitrarySuchThat/DeriveStructParamGenerator.lean`
- Fixture Git blob SHA: `b20b11e33026d2a69a4d715f44f3b5e564d5fc75`

The fixture predates V156 and was authored independently upstream. It defines a structure-parameterized recursive STLC with two required structure-leaf types, including a nested projection (`P.info.Metadata`) and a direct projection (`P.VarId`), and includes runtime generation checks.

## Adaptation boundary
Preserve the external fixture definitions and exact generator target. Replace only the fixture's `derive_mutual generator + enumerator` invocation with one standalone generator invocation so the legacy standalone command and the already-frozen V156 standalone command can be compared. Preserve the upstream generator runtime `#eval`; remove only the enumerator derivation/runtime path, which V156 does not target.

No V158-specific change to the Specimen implementation is allowed.

## Arms
- B0: K2 + K5, adapted external fixture, legacy `derive_generator`.
- I0: K2 + K5 + exact frozen V156 implementation, same adapted external fixture, `derive_generator_with_requirements`.
- Protected: full `lake build` and `lake test` after K2 + K5 + V156.

## Frozen expected discriminator
V156 is admitted only for a singleton dependent requirement. The external fixture needs at least two independently used leaf requirements (`P.info.Metadata`, `P.VarId`). Therefore the most diagnostic expected I0 residual is the frozen V156 requirement-arity ceiling. This expectation is written before execution and does not license changing V156 after the result.

## Verdicts
- `PASS_V158_V156_EXTERNAL_TRANSFER`: baseline fails, I0 passes including the upstream runtime generator check, protected suite passes.
- `PASS_V158_EXTERNAL_FRONTIER_EXPOSES_V156_SINGLETON_CEILING`: baseline fails, I0 fails specifically because V156 encounters multiple independent dependent requirements, protected suite passes.
- `NEGATIVE_V158_OTHER_EXTERNAL_RESIDUAL`: baseline fails and I0 fails for some non-R10 reason other than the singleton ceiling.
- `REJECT_V158_BASELINE_ALREADY_SUFFICES`: baseline passes.
- `R10_*`: source pin/adaptation/setup/protected distortion.

## Claim boundary
This is an externally authored, pre-existing frontier test. A singleton-ceiling verdict does not count as transfer; it identifies the next operator residual. A transfer PASS would still not establish novelty relative to upstream PR #47, because that PR already contains a broader structure-leaf solution.
