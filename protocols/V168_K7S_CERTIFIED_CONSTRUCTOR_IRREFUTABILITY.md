# V168 — K7S certified constructor irrefutability

## Status entering V168
V167 established the full A/B/C causal pattern on the natural issue #12 frontier and a held-out single-constructor transfer: A reproduced both redundant-wildcard failures, B removed them while preserving the multi-constructor safety case, and C restored both failures. Full `lake build` passed under B. Full `lake test` still failed.

The V167 test failures split into two classes:
1. stale `#guard_msgs` expectations that explicitly pin the redundant-match diagnostic intentionally removed by K7R;
2. genuine hard errors caused by recursively treating every nested `CtorPattern` name as a Lean data constructor. Existing protected paths contain names such as `StateResult`, `Nat`, `List`, `String`, and `CedarExpr` in this representation, for which `getConstInfoCtor` must not be called unconditionally.

## Frozen K7S mechanism
`K7S_CERTIFIED_CONSTRUCTOR_IRREFUTABILITY` is a conservative refinement of K7R.

Define complete-pattern irrefutability structurally:
- `UnknownPattern _` => irrefutable.
- `LitPattern _` => refutable.
- `CtorPattern name args` => first inspect `getConstInfo name`.
  - If and only if metadata is `.ctorInfo info`, inspect the parent inductive. The pattern is irrefutable iff that parent has exactly one constructor and every nested argument pattern is recursively irrefutable.
  - For any non-constructor metadata result, return false and retain the wildcard. Never throw merely because a nested pattern name is not a constructor.

The mechanism may inspect only `Pattern` structure and Lean constant metadata. It may not inspect fixture names, issue numbers, relation names, concrete protected-test identities, source paths, or domain names.

## Frozen evidence
Reuse unchanged:
- `fixtures/V165_UPSTREAM_ISSUE12_REPRO.lean`
- `fixtures/V166_HELDOUT_SINGLE_CTOR_INDUCTIVE.lean`
- `fixtures/V166_MULTICTOR_WILDCARD_SAFETY.lean`

Run admitted prior stack A, prior stack + K7S B, and independent clean ablation C.

For B, record full `lake build` and full `lake test` without masking failure details.

## Test-result separation rule
Do not update protected tests during the production experiment.

After B, classify every full-suite failure into exactly one of:
- `OBSOLETE_EXPECTATION`: a `#guard_msgs` mismatch whose removed expected message is only the redundant-wildcard diagnostic intentionally eliminated by K7S, with no new Lean error at that location;
- `SEMANTIC_OR_COMPILATION_FAILURE`: any other error, missing case, failed instance, unexpected diagnostic, or compiler failure.

K7S production eligibility requires zero `SEMANTIC_OR_COMPILATION_FAILURE` results. Obsolete expectations may justify a separate, explicit test-maintenance phase only after this separator passes; they are not silently ignored and are not part of the production intervention.

## Scientific gates
- A natural and held-out reproduce `redundantMatchAlt`; A safety passes.
- B natural and held-out pass unchanged; B safety passes.
- B full build passes.
- B full test has zero semantic/compilation failures after diagnostic classification; any remaining failures are exclusively obsolete expectations.
- C restores natural and held-out failures; C safety passes.
- K7S-only production diff contains no target/domain tokens.

If exclusively obsolete expectations remain, V168 may conclude `PASS_V168_K7S_PRODUCTION_ELIGIBLE_TEST_MAINTENANCE_REQUIRED`, but K7S is not fully admitted until the separately frozen expectation-maintenance run passes the complete suite.

A fully green B suite with all causal gates passes directly as `PASS_V168_K7S_ADMITTED_BOUNDED_NATURAL_CONSTRUCTOR_DEVELOPMENT`.
