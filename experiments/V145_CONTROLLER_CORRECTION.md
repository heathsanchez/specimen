# V145 controller correction

The workflow-generated label `K6_REMAINS_LICENSED_AFTER_LET_CLOSURE` is **not promotable** under the frozen V145 precommit.

The precommit explicitly states: if let syntax/parser/elaboration fails before reaching the scientific path, classify R10. Both let arms failed at `derive_mutual` with `Expected constant in derive_mutual spec`; therefore they did not test whether a local let-bound fixed fvar solves the V139 residual.

Hard evidence retained from V145:
- direct closed constant reproduces `NON_FVAR_APPLICABILITY`;
- generic symbolic control reproduces `SYMBOLIC_INSTANCE`;
- protected build/test are green.

Correct V145 verdict: `R10_INCONCLUSIVE_LET_ROUTE_NOT_REACHED`.

No semantic conclusion about let-bound old closure. No additional K6 evidence is earned by V145. K6 remains only as licensed by the earlier V142/V143/V144 bounded closure results, with the let-bound representation rival unresolved.