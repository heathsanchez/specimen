# V158 Scope-Valid Prerequisite Placement — Result

Hard-evidence source: GitHub Actions run `31947018740`, job `95164546088`.

Verdict: `PASS_V158_SCOPE_VALID_PLACEMENT_ADMITTED_SCOPED`.

Earned scoped capability: `K6_SCOPE_DEPENDENT_REQUIREMENT_PROMOTION`.

Frozen gates: all G1–G14 passed. Baseline reproduced `SYMBOLIC_INSTANCE`; primary, source-distinct held-out, valid multi-requirement, instance-parameter, mutual-recursion, DependentArgs, STLC, Strata, and ScheduleQualityRegression discriminators all passed under intervention; full `lake build` and `lake test` returned 0; ablation is the frozen baseline and restores the symbolic failure.

Implementation scope: preserve requirement provenance and promote/rebind only unconstrained prerequisites whose syntax depends on an actual generated producer input. Closed/global and constrained requirements retain baseline use-site handling. No fixture/domain-specific special casing is admitted.

Claim boundary: this admits a scoped K6 only. Constructor development remains unestablished until the precommitted V159 later-frontier causal dependence experiment passes.

The first V158 run was R10-only because the local syntax walker lacked an inferable structural termination proof; V158B repaired only that apparatus with a top-level `partial def` and did not change the frozen scientific criterion.
