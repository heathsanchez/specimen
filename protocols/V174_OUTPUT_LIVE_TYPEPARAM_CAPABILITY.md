# V174 — Output-live type-parameter capability separator

## Earned residual
V172B established a genuine protected counterexample to blind V171 deletion. The `Diag` generator has output `g : α` while its fixed pair input has nonlinear shape `(b,b)`. Removing every default type-parameter capability makes this protected generator fail, while issue #19 Map/Set fixed-input-only type parameters are over-constrained by the original unconditional rule.

## Frozen candidate
For generator/enumerator emitters, retain the old default pair `[producerUnconstrainedClass α] [DecidableEq α]` **only** for relation type parameters syntactically occurring in a generated output type. Fixed-input-only type parameters receive no default capability. Checker/theorem defaults remain absent and real checker requirements must arrive through the admitted requirement path.

Intervention: `scripts/v174_apply_output_live_typeparam_capability.py`.

## Arms
- A: complete admitted K2+K5+K6+K7S state plus V169 scoped expectation maintenance, no V174.
- B: same state plus frozen V174 candidate.
- C: independent rebuild of A.

## Frozen gates
1. A full build/test pass.
2. A Map/Set issue-19 fixtures fail specifically by unwanted type-parameter constraints.
3. B Map/Set fixtures pass.
4. B genuine generated-α and equality safety fixtures pass.
5. B full build/test pass, including protected `Diag`/NEqGenerator.
6. C restores Map/Set failures.
7. V169 maintenance scope remains exactly its admitted three files in all arms.

## Interpretation
PASS licenses the bounded distinction `OUTPUT_LIVE_TYPEPARAM_CAPABILITY`: default producer/equality capability is justified by occurrence in a generated output type, not merely by being a relation type parameter. It does not claim this is globally minimal beyond the frozen corpus. Any protected failure kills the candidate. Apparatus failure is R10.