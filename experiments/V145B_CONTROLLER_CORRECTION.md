# V145b controller correction

The workflow-generated verdict `LET_ROUTE_REACHED_BUT_DID_NOT_CLOSE` is not promotable under the frozen V145b precommit.

The precommit states that if standalone parsing/elaboration prevents the let-bound term from reaching schedule derivation, V145b is R10 and provides no semantic evidence for or against let-bound closure.

Observed let-arm errors were:
- `Error in parsing constraint: let p := V145BP0;`
- the same parsing error in the synthesis arm.

Therefore the let-bound scientific mechanism was not reached.

Hard evidence retained:
- standalone direct fixed global constant reproduces `NON_FVAR_APPLICABILITY`;
- standalone generic parameter reproduces the symbolic dependent-instance residual;
- protected build/test are green.

Correct V145b verdict: `R10_INCONCLUSIVE_LET_ROUTE_NOT_REACHED`.

No additional evidence for K6 necessity is earned by V145b. The let-bound old-language representation remains unresolved because the current command surface cannot express it.