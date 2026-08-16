# V172 — Issue #19 source-distinct transfer

## Frozen question
Does the V171C deletion law transfer, without retuning, from the one-parameter V170 reproduction to two issue-native structural families: a Map-shaped relation with two fixed type parameters and a Set-shaped relation with one fixed type parameter?

## Frozen intervention
Exactly `scripts/v171_apply_delete_default_typeparam_constraints.py` as admitted by V171C. No edits to the intervention are permitted from V172 fixture evidence.

## Arms
- A: admitted prior stack K2+K5+K6+K7S, no V171 deletion.
- B: same prior stack plus frozen V171 deletion.
- C: independent rebuild of A after B.

## Required gates
1. A fails both source-distinct transfer fixtures from unwanted type-parameter constraints.
2. B passes both fixtures.
3. B still passes the V171 genuine-generated-type and equality safety fixtures.
4. B passes full repository `lake build` and `lake test`.
5. C restores failure on both transfer fixtures.

## Interpretation
- PASS only if all gates pass: bounded evidence that unconditional default type-parameter capability binders are redundant when actual capability requirements are already supplied by the admitted requirement-provenance machinery.
- Any protected regression kills admission.
- Apparatus failure is R10 and does not count as scientific evidence.
