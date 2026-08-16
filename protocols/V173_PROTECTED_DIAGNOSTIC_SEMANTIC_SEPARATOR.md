# V173 — Protected diagnostic semantic separator

## Frozen question
Did the V171 deletion law change the semantics of the exact protected relation shapes whose `#guard_msgs` snapshots failed in V172, or did it only remove redundant-alternative diagnostics?

## Frozen intervention
Exactly `scripts/v171_apply_delete_default_typeparam_constraints.py` as used in V171C/V172. No intervention edits are permitted.

## Semantic oracle
`fixtures/V173_PROTECTED_DIAGNOSTIC_SEMANTICS.lean` reproduces the protected structural families with derivation diagnostics neutralized and executable checks for the generated producer/checker behavior.

## Diagnostic oracle
The three original protected modules are compiled unchanged:
- `SpecimenTest/DeriveArbitrarySuchThat/Syntax.lean`
- `SpecimenTest/DeriveArbitrarySuchThat/FunctionCallsTest.lean`
- `SpecimenTest/DeriveArbitrarySuchThat/NEqGenerator.lean`

## Arms
- A: admitted prior stack K2+K5+K6+K7S.
- B: same stack plus frozen V171 deletion.
- C: independent rebuild of A.

## PASS conditions
1. V173 semantic fixture passes in A, B, and C.
2. All three original protected snapshot modules pass in A.
3. All three original protected snapshot modules fail in B specifically because the expected `#guard_msgs` docstrings no longer match generated diagnostics.
4. All three original protected snapshot modules pass again in C.
5. Core source build passes in B.

A PASS establishes only that the V172 protected failure is diagnostic-oracle drift for these frozen cases. It does not itself license editing protected tests or admitting the deletion law; that requires a subsequent verifier-repair experiment.