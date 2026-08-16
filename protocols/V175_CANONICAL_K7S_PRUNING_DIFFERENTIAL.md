# V175 — Canonical K7S pruning differential

Rigorous Breakthrough Stack v1.1 applies.

## Question
Once the admitted K7S baseline is reconstructed with its separately frozen V169 obsolete-expectation maintenance, does V173 standalone-producer pruning add any genuine protected failure?

## Canonical prior baseline
Production stack: v120, v132, v156, v156b, v158/K6, v168/K7S.
Test apparatus maintenance: `scripts/v169_remove_obsolete_redundant_match_expectations.py`, applied identically to A and B. It may modify only the three frozen test files and no production source.

## Arms
A = canonical prior baseline + full `lake test`.
B = same canonical baseline + V173 standalone producer pruning + full `lake test`.

Also rerun the natural issue-19 fixture under B to ensure the pruning rescue remains.

## Classification
- PASS_V175_SCOPED_PRUNING_CANONICALLY_PROTECTED iff A test rc=0, B test rc=0, and B natural rc=0.
- SEPARATOR_V175_PRUNING_ADDS_GENUINE_FAILURE iff A test rc=0 and B test rc!=0; record exact new failing targets/errors.
- R10 if either suite or the natural probe does not execute.

A protected PASS would admit pruning as lawful closure and reject K8 invention for issue #19. A causal protected failure licenses a narrower liveness rule but not K8 construction until the failing requirement is structurally identified.
