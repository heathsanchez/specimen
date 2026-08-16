# V173 — Standalone producer type-parameter pruning

Rigorous Breakthrough Stack v1.1 applies. Frozen verifier results are hard evidence; infrastructure failures are R10.

## Question
Does issue #19 require global parameter-liveness machinery, or is the residual solved by a narrower lawful closure: remove unconditional type-parameter producer/checker binders only from the standalone producer emitter actually used by the natural target, while leaving all mutual/checker emitters unchanged?

## Frozen substrate
Apply the admitted stack in order: v120, v132, v156, v156b, v158 (K6), v168 (K7S).

## Intervention
`scripts/v173_apply_standalone_producer_typeparam_pruning.py`, which removes exactly one four-space-indented standalone producer binder construction and asserts exactly three other type-parameter binder emitters remain. No target/type/fixture-specific tokens are permitted.

## Frozen probes
- Natural issue #19: `fixtures/V170_ISSUE19_PARAMETER_OVERCONSTRAINT.lean`
- Generated-type safety: `fixtures/V171_GENERATED_TYPE_SAFETY.lean`
- Equality safety: `fixtures/V171_EQUALITY_TYPEPARAM_SAFETY.lean`
- Full protected `lake test`.

## Arms
A prior stack only; B prior + V173; C independent prior-stack ablation.

## PASS
`PASS_V173_STANDALONE_PRUNING_ADMITTED` iff A natural fails; A safety probes pass; B natural and both safety probes pass; B full protected tests pass; C restores the natural failure; and the intervention self-check proves only the intended standalone emitter changed.

A PASS is closure/deletion, not a new constructor capability. It rejects K8 invention for this natural residual. A protected failure is `NEGATIVE_V173_SCOPED_PRUNING_NOT_ADMITTED`. An apparatus failure is R10.
