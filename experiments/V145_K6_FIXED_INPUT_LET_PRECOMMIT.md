# V145 K6 fixed-input let — frozen precommit

Controller: Rigorous Breakthrough Stack v1.1.

## Residual
V139/V140/V142/V143/V144 establish, within their bounded protocols, that a concrete closed index such as `P0` is rejected as a non-fvar input, while parameterizing it moves the residual to dependent `Arbitrary p.Meta` synthesis. Existing instance-binder, relation-instance, and auto-derive/fallback routing alternatives did not close the case. Protected behavior remained green.

## Candidate K6 hypothesis
`K6_FIXED_INPUT_LET`: when a non-output relation argument is a closed non-fvar expression, preserve its exact value inside schedule derivation by introducing a local **let-bound fixed input** of the expected relation-argument type and using that local fvar for the existing scheduler. Do not replace the value with a fresh universally quantified parameter. Do not special-case any fixture name, relation name, type, or constant.

## Frozen arms
- B: exact admitted K2+K5, no K6. Direct fixed-index target must reproduce the V139/V144 non-fvar residual.
- I: exact admitted K2+K5 + K6_FIXED_INPUT_LET.
- A: targeted ablation of K6 transport, restoring the original non-fvar handling while keeping all other intervention code/configuration identical where possible.
- G: generic symbolic control, to ensure K6 does not falsely claim to solve the separate missing-instance residual.

## Target
A source-generic fixture structurally equivalent to the V139 fixed-index case, with a closed constant index whose dependent field type is concrete and has an existing `Plausible.Arbitrary` instance.

## Gates
K6 local causal PASS requires all of:
1. B reproduces `NON_FVAR_APPLICABILITY`.
2. I elaborates and synthesizes the requested `ArbitrarySizedSuchThat` instance at the same closed fixed index.
3. A restores the B failure.
4. G remains correctly classified; K6 must not manufacture a symbolic dependent instance that is absent.
5. Full protected `lake build` and `lake test` pass under I.
6. Patch contains no fixture-specific identifiers or constants.

A local PASS does **not** admit K6. Admission additionally requires held-out/source-distinct transfer and protected behavior, followed by a later-frontier test. If the intervention fails to reach its own mechanism because the patch/apparatus is malformed, classify R10. If it merely moves the residual, record the new residual without claiming K6 capability.
