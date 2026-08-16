# V166 — K7 exhaustive-match fallthrough elision

## Purpose
Test and, only if all frozen gates pass, admit a general constructor capability discovered from the V165-qualified natural issue #12 residual.

## Residual
The admitted prior stack K2+K5+K6 emits a synthetic wildcard-failure arm for every schedule `.Match`. On a scrutinee whose inductive type has only one constructor and whose explicit pattern is that constructor, the wildcard is unreachable and Lean rejects generated checker code with `lean.redundantMatchAlt`.

## Frozen K7 mechanism
`K7_EXHAUSTIVE_MATCH_FALLTHROUGH_ELISION`:

When compiling a schedule `.Match` with an explicit constructor pattern, query Lean environment metadata for that constructor's parent inductive. If the parent inductive has exactly one constructor, the explicit constructor pattern exhausts the scrutinee type and the compiler must emit only that explicit branch. Otherwise retain the existing synthetic wildcard-failure branch unchanged.

The mechanism may inspect only constructor/inductive metadata. It may not inspect issue numbers, fixture names, relation names, field names, concrete type names, or source paths.

## Frozen fixtures
1. Natural primary: exact V165 upstream issue #12 fixture, already qualified before K7 implementation.
2. Held-out one-constructor inductive: a source-distinct non-`structure` inductive with one constructor and a different field/premise shape. Baseline must fail with redundant wildcard; K7 must pass.
3. Multi-constructor safety: an inductive with at least two constructors where the relation pattern covers only one. K7 must preserve the wildcard and compile successfully; deleting all wildcards indiscriminately is therefore disallowed.

Fixtures are committed before K7 implementation.

## Arms
A — exact admitted prior stack K2+K5+K6, no K7.
B — exact admitted prior stack + K7.
C — independent K7 ablation rebuilt from A after B.

## Admission gates
K7 PASS requires all:
- A reproduces `redundantMatchAlt` on natural issue #12.
- A reproduces the same structural residual on the held-out one-constructor inductive.
- B passes natural issue #12 unchanged.
- B passes held-out one-constructor fixture unchanged.
- B passes multi-constructor safety fixture.
- C restores A's natural and held-out failures.
- B passes full `lake build` and `lake test`.
- static audit confirms K7 contains no target-specific tokens/paths and changes only generic match-fallthrough construction.

Any source-application/compiler/infrastructure failure is R10 only. If B fails one scientific fixture, K7 is not admitted.

## Constructor-development gate
Because issue #12 was independently authored, deterministically selected, and V165-qualified before K7 was proposed or implemented, a full V166 PASS additionally establishes one bounded natural constructor-development transition:

`K_previous → discovered residual → K7 → previously unreachable natural upstream target`

with independent ablation reversal.

This does **not** establish recursive/open-ended self-improvement, autonomous K7 invention without an external controller, or a general solution to all checker match exhaustiveness.
