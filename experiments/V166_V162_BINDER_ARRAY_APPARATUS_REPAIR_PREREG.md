# V166 — V162 binder-array apparatus repair

## Status
Frozen before execution.

## Why V162 is R10
V162 reproduced the exact V156 arity ablation (`discovered 2`), then its finite-threading implementation failed to compile before any intervention arm. The generated array had syntax category `Array (TSyntax Lean.Elab.Deriving.instBinderF)` while command quotation required `TSyntaxArray Lean.Parser.Term.bracketedBinder`.

## Repair boundary
Preserve V162's exact operator semantics and admission fixtures. Change only binder-array construction to follow Specimen's existing `mkTypeClassInstanceBinders` typing discipline: construct binder syntax, then explicitly wrap it as `TSyntaxArray Lean.Parser.Term.bracketedBinder`.

No change to requirement discovery, deduplication, transport, schedules, dependency handling, or legacy routing is allowed.

## Frozen gates
Same as V162:
1. V156 two-leaf ablation = arity failure, discovered 2.
2. V166 candidate applies, produces nonempty diff, and core builds.
3. Two-leaf generic + transparent concrete specialization PASS.
4. Independently named three-leaf generic + transparent specialization PASS.
5. Singleton family remains PASS.
6. Legacy `derive_generator` on two-leaf family remains non-PASS.
7. Protected `lake build` and `lake test` PASS.

## Verdicts
- `PASS_V166_FINITE_REQUIREMENT_THREADING_ADMITTED_SCOPED`: all gates pass.
- `NEGATIVE_V166_FINITE_THREADING_DOES_NOT_CLOSE_PURE_MULTIPLICITY`: candidate genuinely applies but intervention gates fail.
- `R10_*`: apply/build/fixture/protected distortion.

## Claim boundary
A PASS admits only finite transport of already-discovered requirements. It does not discover, classify, derive, or discharge those requirements and adds no new Lean expressivity.
