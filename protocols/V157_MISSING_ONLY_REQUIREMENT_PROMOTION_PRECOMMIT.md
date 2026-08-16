# V157 — Missing-Only Requirement Promotion Precommit

## Residual
V156 provenance-preserving promotion validly rescued all frozen causal/generalization probes, but full protected behavior failed only in `ScheduleQualityRegressionTest`: the exact generated constant `instArbitrarySizedSuchThatListNatMemNat.aux_arb` disappeared.

The regression test explicitly snapshots kernel-elaborated derived code to detect generated-code changes. Therefore this is a real protected regression, not an apparatus exception.

The current V156 rule promotes every unconstrained-producer requirement, even when Lean can already synthesize that requirement in the exact schedule-compilation local context. This can add unnecessary typeclass premises and alter generated declaration shape/names. The V153/V156 target requirements (`Arbitrary p.Meta`, held-out `Arbitrary q.Carrier`, and the two-field dependent fixture) are precisely requirements that are missing in their symbolic local contexts.

## Question
Is the lawful prerequisite rule:

> promote a requirement iff (a) its origin is `unconstrained` and (b) Lean's typeclass solver cannot already synthesize it in the exact local context where the unconstrained producer requirement is created?

## Frozen intervention
Starting from K2+K5 plus the V156 provenance representation and V156B checker compatibility adapter:
1. Extend each `RequiredInstance` record with `needsPromotion : Bool`.
2. At `unconstrainedProducer`, after constructing the exact requirement type syntax (e.g. `Arbitrary T` / `Enum T`), elaborate that type in the current `TermElabM` local context and call Lean's own `Meta.synthInstance?` under a fresh metavariable context.
3. Set `needsPromotion := true` iff synthesis returns `none`; otherwise false.
4. At `constrainedProducer`, preserve origin=`constrained` and set `needsPromotion := false`; constrained requirements are never promoted by this intervention.
5. At final standalone producer emission, promote only records satisfying both `origin == .unconstrained` and `needsPromotion == true`, deduplicate original term syntax, and thread those into both outer and inner scopes exactly as V156.
6. No string inspection, name-based exceptions, schedule-quality special case, source/test/domain special case, or post-hoc filtering.
7. No change to schedule search, scoring, MExp producer semantics, generated producer calls, checker semantics, or existing constrained-producer synthesis.

## Frozen tests
A. V156 primary projected-type fixture.
B. V156 source-distinct held-out projected-type fixture.
C. V156 valid two-missing-unconstrained-requirement fixture.
D. `InstanceParameterTest`.
E. `MutuallyRecursiveRelationsTest`.
F. `ScheduleQualityRegressionTest` — must now pass unchanged, including exact `aux_arb` snapshot.
G. Full `lake build` and `lake test`.
H. Ablation: K2+K5 baseline without V157 retains primary symbolic-instance failure.

## Gates
G1 baseline primary = SYMBOLIC_INSTANCE.
G2 primary passes.
G3 held-out passes.
G4 multi-missing fixture passes.
G5 InstanceParameterTest passes.
G6 MutuallyRecursiveRelationsTest passes.
G7 ScheduleQualityRegressionTest passes unchanged.
G8 full protected build and test pass.
G9 ablation restores primary failure.
G10 implementation uses only provenance + actual synthesis availability in the creation-site local context; no syntactic/name/domain special cases.

## Verdicts
- `PASS_V157_MISSING_ONLY_PROMOTION_ADMITTED_SCOPED` iff G1..G10 all pass.
- `NEGATIVE_V157_MISSING_ONLY_PROMOTION_NOT_ADMITTED` for a scientific gate failure after valid execution.
- `R10_V157_INCONCLUSIVE` only if apparatus prevents the frozen intervention/gates from executing.

## Claim boundary
A pass earns scoped K6 missing-only provenance-preserving prerequisite promotion. It does not by itself establish constructor development. The next lawful step after admission is a separately frozen later-frontier causal-dependence experiment showing this admitted capability enables a later capability/task the pre-V157 constructor cannot reach.
