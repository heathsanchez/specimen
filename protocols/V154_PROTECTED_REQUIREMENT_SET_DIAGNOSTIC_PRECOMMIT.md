# V154 — Protected requirement-set diagnostic

Frozen 2026-08-16 NZST under Rigorous Breakthrough Stack v1.1 before diagnostic outcomes.

V153 established a causal bounded mechanism hit: K6 inner-dependent requirement threading made both primary and source-distinct held-out singleton fixtures pass, and pre-intervention ablation restored the symbolic-instance failure. However the full protected suite failed, so K6 was not admitted.

The dominant protected residual was that natural derivations frequently discover more than one required instance; V153 intentionally rejected >1 rather than silently generalize. Some protected errors also suggested that not every printed requirement syntax is safely reusable as a binder.

V154 is diagnostic only. It changes no derivation/search/emission semantics and cannot earn K6.

## Frozen intervention

After exact admitted K2 and K5, add only a diagnostic `logInfo` beside the existing trace of `requiredInstances` in `deriveConstrainedProducer`. Log the deduplicated required-instance syntax and count. Do not pass requirements to the emitter, change schedules, add binders, catch failures, or alter instance generation.

Run the protected files that V153 exposed as high-information cases, including:
- `SpecimenTest/DeriveArbitrarySuchThat/InstanceParameterTest.lean`
- `SpecimenTest/DeriveArbitrarySuchThat/DependentArgs.lean`
- `SpecimenTest/CedarExample/CedarCheckerGenerators.lean`

If a named file is absent in the current tree, record that as apparatus metadata and continue with the existing files; do not substitute semantically selected cases after seeing logs.

## Questions

For each observed derivation classify:
- count of deduplicated requirements;
- singleton vs multi;
- textual requirement forms;
- whether placeholders/metavariable-looking `_` syntax occurs;
- repeated/duplicate requirements;
- whether the untouched protected file passes under diagnostic-only instrumentation.

## Interpretation

If multi-requirement sets are composed of ordinary lawful typeclass terms, a bounded all-requirements threading refinement is licensed.
If malformed/context-sensitive requirements occur, diagnose/filter/rebind before any generalization.
If diagnostic-only instrumentation itself changes protected behavior, V154 is R10.

No K6 admission, constructor development, or later-frontier claim follows from V154.