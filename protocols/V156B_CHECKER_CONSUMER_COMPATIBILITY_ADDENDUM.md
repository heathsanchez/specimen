# V156B — Checker Consumer Compatibility Apparatus Addendum

## Classification of V156A protected residual
R10 representation-adapter incompatibility, not a scientific negative on provenance-preserving promotion.

V156A validly executed the frozen intervention. The following frozen scientific gates passed:
- baseline symbolic failure reproduced;
- primary projected-type fixture passed;
- source-distinct held-out fixture passed;
- valid two-unconstrained-requirement fixture passed;
- InstanceParameterTest passed;
- MutuallyRecursiveRelationsTest passed;
- ablation condition remained satisfied.

The full protected build failed in `Specimen/DeriveChecker.lean` only because that consumer still treats compile-schedule requirements as the old flat `TSyntax term` array:
- `List.eraseDups requiredInstances.toList` now asks for `BEq MExp.RequiredInstance`;
- tracing that list now asks for `ToMessageData (List MExp.RequiredInstance)`.

This is a direct representation-consumer mismatch introduced by preserving provenance. It occurs before any checker semantic decision and does not contradict the generator discriminator results.

## Only licensed repair
Update `DeriveChecker`'s existing advisory/reporting consumer to project each provenance record back to its original `.term` before deduplication and tracing:

`List.eraseDups (requiredInstances.toList.map (·.term))`

No checker requirement is promoted, filtered, reordered by origin, or otherwise changed. This adapter restores exactly the old consumer-level object: a deduplicated list of requirement terms.

## Frozen scientific content unchanged
No change to V156 hypothesis, provenance categories, promotion rule, emitter placement, fixtures, gates, ablation, protected suite, or claim boundary.

After this adapter repair, rerun the complete frozen V156 protocol. Any further protected semantic failure is scientific unless it is separately demonstrated to be apparatus/representation-only before interpretation.
