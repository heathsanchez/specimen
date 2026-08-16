# V176 — Standalone type-parameter equality liveness

Rigorous Breakthrough Stack v1.1 applies. This is closure/composition before invention.

## Prior evidence
V175 established on the canonical admitted K6+K7S baseline that standalone blanket pruning rescues natural issue #19 but adds exactly one genuine protected failure: `NEqGenerator`, where generated code needs `DecOpt (b₁ = b)` over the type parameter. The repository already contains the pre-existing `fix-polymorphic-dep-constraints` line, whose frozen commit history implements bottom-up class propagation from schedule dependencies rather than hardcoded per-sort constraints.

## Question
Can existing schedule dependency information plus admitted K6 replace the unconditional standalone `[Arbitrary α] [DecidableEq α]` pair with lawful liveness?

## Frozen rule
For the standalone producer emitter only:
1. Do not add a blanket producer-class binder for every type parameter. Actual unconstrained generation requirements remain supplied by the admitted K6 requirement mechanism.
2. Retain `DecidableEq α` iff at least one compiled producer schedule contains a non-recursive equality check whose `ConstructorExpr` tree references type parameter α.
3. No target names, concrete types, issue numbers, or fixture paths may influence the rule.
4. Mutual/checker emitters are unchanged.

This is a scoped extraction/composition of the pre-existing bottom-up dependency principle, not a new K8 constructor.

## Frozen probes
- Natural: `fixtures/V170_ISSUE19_PARAMETER_OVERCONSTRAINT.lean` — must pass without blanket α constraints.
- Held-out equality liveness: `fixtures/V176_EQUALITY_LIVENESS_HELDOUT.lean` — must pass and retain lawful equality capability.
- Generated-type safety: `fixtures/V171_GENERATED_TYPE_SAFETY.lean` — must pass via actual generation/K6 requirement.
- Canonical K7S protected suite: apply V169 obsolete-expectation maintenance identically, then full `lake test`.

## Arms
A: canonical prior stack only.
B: canonical prior stack + V176 liveness rule.
C1 targeted ablation: prior + V173 blind standalone pruning; held-out equality fixture must fail.
C2 natural ablation: canonical prior stack only; issue #19 must fail.

## PASS
`PASS_V176_EQUALITY_LIVENESS_CLOSURE_ADMITTED` iff:
- A natural fails;
- B natural passes;
- B held-out equality passes;
- B generated-type safety passes;
- B full canonical protected suite passes;
- C1 equality held-out fails;
- C2 natural fails;
- source self-audit confirms no target/type special casing and no mutual/checker emitter change.

A PASS rejects K8 invention for issue #19 and admits a scoped closure/liveness refinement. It is not a new constructor generation. Any protected regression is a scientific negative. Any intervention/build/runner failure before gates execute is R10.
