# V167 — K7R recursive irrefutable pattern

## Status entering V167
V166 established all three scientific target observations for K7: prior-stack A reproduced the natural issue #12 residual and the held-out single-constructor residual while preserving the multi-constructor safety case; K7 B made all three frozen fixtures pass. However B failed the protected full suite with missing-pattern cases in existing checker tests, and C did not execute. V166 is therefore not an admission result.

## Residual learned from V166
Outer-constructor cardinality is insufficient to determine whether a generated pattern match is exhaustive. A pattern may use the sole constructor of its outer inductive while containing nested constructor or literal subpatterns that reject values. Removing the wildcard in that case creates non-exhaustive generated Lean code.

## Frozen K7R mechanism
`K7R_RECURSIVE_IRREFUTABLE_PATTERN`:

Define pattern irrefutability structurally:
- `UnknownPattern _` is irrefutable.
- `LitPattern _` is refutable.
- `CtorPattern C args` is irrefutable iff Lean environment metadata reports that `C` is the sole constructor of its parent inductive **and every nested argument pattern is irrefutable**.

For schedule `.Match`, omit the synthetic wildcard-failure branch iff the complete pattern is irrefutable by the rule above. Otherwise preserve the wildcard unchanged.

The mechanism may inspect only `Pattern` structure and constructor/inductive metadata. It may not inspect issue numbers, fixture names, relation names, concrete type names, source paths, or protected-test identities.

## Frozen evidence targets
Reuse without modification the pre-K7 fixtures already frozen before the first K7 implementation:
1. Natural issue #12 reproduction: `fixtures/V165_UPSTREAM_ISSUE12_REPRO.lean`.
2. Held-out one-constructor inductive: `fixtures/V166_HELDOUT_SINGLE_CTOR_INDUCTIVE.lean`.
3. Multi-constructor wildcard safety: `fixtures/V166_MULTICTOR_WILDCARD_SAFETY.lean`.
4. Full protected `lake build` and `lake test`, whose V166 failure supplies the independent nested-pattern counterexample.

## Arms
A — admitted prior stack K2+K5+K6, no K7/K7R.
B — admitted prior stack + K7R.
C — independent ablation: clean A rebuilt without K7R after B.

## Admission gates
PASS requires all:
- A natural fails with `redundantMatchAlt`.
- A held-out fails with `redundantMatchAlt`.
- A multi-constructor safety passes.
- B natural passes unchanged.
- B held-out passes unchanged.
- B multi-constructor safety passes unchanged.
- B full `lake build` passes.
- B full `lake test` passes.
- C restores natural and held-out `redundantMatchAlt` failures and safety remains passing.
- static audit finds no target-specific token in the production K7R diff.

Any harness/compiler/source-application failure is R10 only.

## Claim boundary
A full PASS admits K7R as the corrected general capability and establishes one bounded natural constructor-development transition from an independently authored natural residual through a generalized mechanism with held-out transfer, protected counterexample refinement, and independent ablation reversal. It does not establish autonomous or open-ended recursive self-improvement.
