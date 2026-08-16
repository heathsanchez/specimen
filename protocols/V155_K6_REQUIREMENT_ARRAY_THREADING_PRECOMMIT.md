# V155 — K6 Requirement-Array Threading Precommit

## Question
Can the scoped V153 mechanism be generalized from one discovered dependent typeclass requirement to the complete deduplicated requirement array, while preserving protected behavior?

## Frozen evidence before intervention
- V153 baseline: symbolic projected-instance failure.
- V153 K6 singleton intervention: primary PASS; source-distinct held-out PASS; ablation restores failure.
- V153 protected suite: FAIL.
- Protected failures include explicit V153 bounded-K6 counts 2,3,4,5,24, proving natural multi-requirement cases exist.
- Some protected cases fail separately with malformed/context-sensitive `_` specialization after singleton threading.
- V154 diagnostic-only logging left full protected build/test green but failed to expose its intended requirement lines in direct-file probes. Therefore V154 counts are observability-R10 and are not used to justify absence/presence of requirements.

## Intervention
Starting from the same K2+K5 baseline used by V153, replace only V153's singleton/throw branch with generic array binding:
1. Preserve the exact deduplicated `requiredInstances` array already discovered by schedule compilation.
2. Construct one uniquely named bracketed instance binder per requirement for the generated outer instance.
3. Construct one uniquely named bracketed instance binder per requirement for the inner auxiliary producer's own parameter scope.
4. Splice the full binder arrays into their respective scopes.
5. No requirement filtering, no source-specific cases, no Cedar-specific cases, no opacity special cases, no changes to schedules/search/scoring/MExp requirement discovery.

## Frozen tests
A. V153 primary fixture, byte-identical semantics.
B. V153 source-distinct held-out fixture, byte-identical semantics.
C. New two-requirement fixture requiring both `Arbitrary p.A` and `Arbitrary p.B` in one generated producer.
D. Targeted ablation: K2+K5 baseline without V155 must retain the original symbolic failure on A.
E. Full `lake build` and `lake test` after V155.

## Gates
G1 baseline A is SYMBOLIC_INSTANCE.
G2 primary A passes after V155.
G3 held-out B passes after V155.
G4 explicit multi-requirement C passes after V155.
G5 targeted ablation restores baseline failure.
G6 full protected build and test both pass.
G7 intervention remains generic: no fixture identifiers or Cedar identifiers are used by the V155 patch.

## Verdicts
- `PASS_V155_K6_ARRAY_ADMITTED_SCOPED` only if G1..G7 all pass.
- `NEGATIVE_V155_K6_ARRAY_NOT_ADMITTED` for a scientific gate failure.
- `R10_V155_INCONCLUSIVE` only for apparatus failure preventing the frozen test from executing.

## Claim boundary
Passing V155 earns only scoped K6 requirement-array threading. It does not establish constructor development. A separately frozen later-frontier causal-dependence experiment is still required.
