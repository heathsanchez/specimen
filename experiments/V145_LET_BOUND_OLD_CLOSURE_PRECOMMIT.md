# V145 let-bound old-closure separator — frozen precommit

Controller: Rigorous Breakthrough Stack v1.1.

Question: does the V139/V144 fixed-index residual disappear if the same closed constant is represented as a local `let` fvar inside the user specification, without any engine modification?

Frozen arms:
- B_DIRECT: exact admitted K2+K5; direct closed constant index. Must reproduce `NON_FVAR_APPLICABILITY`.
- L_LET: exact admitted K2+K5; same semantic target, but `let p := P0` is introduced inside the specification term and all dependent occurrences use `p`.
- L_LET_SYNTH: same as L_LET plus synthesis of the resulting `ArbitrarySizedSuchThat` instance at the original closed `P0` target.
- G_SYMBOLIC: generic symbolic `p` without supplying the required dependent instance; should retain the known symbolic-instance residual.

No source modification beyond exact admitted K2+K5 is permitted. Same toolchain and protected suite.

PASS `REJECT_K6_LET_BOUND_OLD_CLOSURE_SUFFICES` requires B_DIRECT = NON_FVAR_APPLICABILITY, L_LET = PASS, L_LET_SYNTH = PASS, G_SYMBOLIC = SYMBOLIC_INSTANCE, and protected build/test green.

If let syntax/parser/elaboration fails before reaching the scientific path, classify R10. If L_LET changes but does not solve the residual, record the new residual and do not claim K6. A PASS rejects the K6 invention claim for this residual; it does not establish constructor development.