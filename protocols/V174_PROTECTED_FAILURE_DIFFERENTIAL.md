# V174 — Protected failure differential

Rigorous Breakthrough Stack v1.1 applies.

Question: are the V173 protected failures caused by scoped standalone pruning, or already present in the admitted prior stack on this exact substrate?

Frozen arms:
A = prior admitted stack (v120, v132, v156, v156b, v158/K6, v168/K7S), then full `lake test`.
B = same prior stack + byte-identical V173 standalone producer pruning, then full `lake test`.

Record exact failing target names and test exit codes. No scientific mechanism changes.

PASS_DIFFERENTIAL_NEUTRAL iff A and B have identical protected failure sets and identical pass/fail status; then V173's previous attribution is invalidated and must be reclassified using the paired baseline.
NEGATIVE_DIFFERENTIAL_CAUSAL iff B adds any protected failure absent from A.
R10 if either suite does not execute.
