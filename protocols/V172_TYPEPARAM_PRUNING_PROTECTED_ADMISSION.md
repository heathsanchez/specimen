# V172 — Type-parameter pruning protected admission

## Controller
Rigorous Breakthrough Stack v1.1. Frozen verifier results are hard evidence; infrastructure failures are R10 and imply no semantic conclusion.

## Question
Does the V171C closure intervention — deleting unconditional default type-parameter producer/checker binders from all four emitters while retaining only use-site/discovered requirements supplied by the existing admitted stack — solve the natural issue-19 frontier without protected regressions?

This is a closure/pruning test, not a new-constructor invention test.

## Frozen substrate
Apply, in order, the already admitted prior-stack scripts:
1. v120 binder-aware fixed parameter
2. v132 output-dependent input-determined
3. v156 requirement provenance promotion
4. v156b checker consumer compatibility
5. v158 scope-dependent promotion (K6)
6. v168 certified constructor irrefutability (K7S)

Then apply byte-identical `scripts/v171_apply_delete_default_typeparam_constraints.py` from V171C.

## Frozen probes
- Natural: `fixtures/V170_ISSUE19_PARAMETER_OVERCONSTRAINT.lean`
- Generated-type safety: `fixtures/V171_GENERATED_TYPE_SAFETY.lean`
- Equality safety: `fixtures/V171_EQUALITY_TYPEPARAM_SAFETY.lean`

## Arms
A — prior admitted stack only.
B — prior stack + V171 deletion/pruning closure.
C — independent clean rebuild of prior stack only (targeted ablation).

## Admission gates
PASS_V172_PRUNING_CLOSURE_ADMITTED only if all hold:
1. A natural fails on the frozen issue-19 residual.
2. A generated and equality safety probes pass.
3. B natural passes.
4. B generated and equality safety probes pass.
5. B `lake build` passes.
6. B full `lake test` passes.
7. C natural restores the original failure.
8. Intervention script self-check proves all four unconditional type-parameter binder emitters were removed.

If B rescues the natural target but any protected gate fails: NEGATIVE_V172_PRUNING_NOT_ADMITTED.
If B does not rescue: NEGATIVE_V172_PRUNING_NOT_SUFFICIENT.
If any apparatus step prevents an arm/gate from executing: R10_V172_INCONCLUSIVE.

## Claim discipline
A PASS rejects the need for K8 on this residual: the issue is solved by lawful closure/deletion plus already-admitted requirement discovery. It does not earn a new constructor capability and does not by itself establish another constructor-development generation.
