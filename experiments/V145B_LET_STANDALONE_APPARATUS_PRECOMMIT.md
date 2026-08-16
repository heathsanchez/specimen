# V145b let-bound closure apparatus repair — frozen precommit

Controller: Rigorous Breakthrough Stack v1.1.

V145 mutual-command let arms did not reach the scientific mechanism (`Expected constant in derive_mutual spec`) and are R10 under the V145 precommit. V145b changes only the command entrypoint to the pre-existing standalone `derive_generator`; the semantic target, exact K2+K5 state, and let-bound representation are unchanged.

Arms:
- S_DIRECT: standalone direct fixed constant.
- S_LET: standalone `let p := P0` representation.
- S_LET_SYNTH: same plus synthesis at the original `P0` predicate.
- S_GENERIC: standalone generic `p`, expected symbolic dependent-instance residual.

No engine modification is permitted. Protected build/test must remain green.

If S_LET and S_LET_SYNTH pass while direct/generic reproduce their controls, reject K6 for this residual. If standalone parsing/elaboration still prevents the let term from reaching schedule derivation, V145b is R10 and provides no semantic evidence for or against let-bound closure. If it reaches scheduling but fails semantically, record that residual.