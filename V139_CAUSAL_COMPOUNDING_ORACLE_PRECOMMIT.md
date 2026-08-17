# V139 — Causal Compounding Oracle

## Question
Does the developmental state created by K5 make a later specialization-preserving discovery reachable, and does ancestor ablation move that later frontier backward?

This is the only claim under test. It is not a K6-admission test and does not use a production K6 patch.

## Frozen substrate
- Start from repository head `5e466fe23329c0a56c98396535f1d0191b5fe7c6`.
- K2 is applied with `scripts/v120_apply_binder_aware_fixed_parameter.py`.
- K5 is applied with `scripts/v132_apply_output_dependent_input_determined.py`.
- The later task is source-distinct from V137 and uses a different parameter/family vocabulary and `Bool` payload.
- The specialization oracle is explicit in the relation itself; no production source is modified to preserve fixed roots.

## Arms
A — ANCESTOR_ABLATION
- K2 only; K5 absent.
- Run the specialized later task.

B — PRE_LATER_FRONTIER
- K2+K5.
- Run the original fixed-root form of the later task.
- This arm should retain the root-specialization obstruction.

C — LATER_DISCOVERY
- K2+K5.
- Run the extensionally specialized form of the same later task.

## Crown-jewel pattern
`PASS_V139_CAUSAL_COMPOUNDING_ORACLE` iff:
- A fails;
- B fails with the expected dependent-instance/root-specialization obstruction;
- C succeeds.

Interpretation, if and only if the pattern holds:
1. K5 is a necessary ancestor for this later discovery under the frozen task.
2. K2+K5 alone does not reach the later discovery because root specialization is erased.
3. Restoring the specialization distinction makes the later discovery reachable.
4. Removing K5 moves the later frontier backward again.

This is bounded causal compounding evidence. It is not open-ended self-improvement and does not by itself admit K6.

## Nulls
- If A succeeds, K5 is not an ancestor of the later discovery: `NULL_V139_NO_ANCESTOR_DEPENDENCE`.
- If C fails, specialization is insufficient on the later task: `NULL_V139_NO_LATER_DISCOVERY`.
- If B succeeds, the later task does not instantiate the known specialization obstruction: `R10_V139_FRONTIER_NOT_SEPARATED`.
- Any unrelated parse/type/import failure is R10 and consumes no scientific result.

## Forbidden moves
- no changes to K2 or K5;
- no added typeclass instances;
- no target-name special casing;
- no production K6 patch;
- no changing the later task after observing an arm;
- no substituting a different task if the frozen task is inconvenient.
