# V170 — issue #19 natural baseline qualification

## Purpose
Qualify the next deterministic upstream natural frontier after admitted K7S without proposing K8.

## Source
Upstream strata-org/specimen issue #19, independently authored before this experiment: parameterized inductives receive unconditional Arbitrary/Enum and DecidableEq constraints on type parameters even when those parameters are fixed by the caller and never generated.

## Frozen minimal reproduction rule
The issue does not contain a complete standalone file, so freeze the smallest faithful instance of its stated structure before any K8 mechanism exists:
- a parameterized relation `{α : Type}`;
- an `α` value is fixed by context and is not an output;
- only a `Nat` output is generated;
- the generic producer is derived first;
- it is then specialized to a concrete opaque type deliberately lacking `Plausible.Arbitrary` and `DecidableEq`.

The concrete type and names are scientifically irrelevant and must not appear in any later production mechanism.

## Prior stack
Apply exact admitted production mechanisms K2 + K5 + K6 + K7S. K7S production identity is frozen to `scripts/v168_apply_certified_constructor_irrefutability.py`.

## Qualification verdict
PASS only if:
1. prior stack applies and Specimen builds;
2. generic derivation succeeds;
3. specialization fails specifically because Lean demands an unnecessary type-parameter class (`Plausible.Arbitrary V170Fixed` and/or `DecidableEq V170Fixed`);
4. no module/object-file/infrastructure failure occurs.

If specialization already succeeds, record NULL/CORPUS MOVED. If a different semantic residual occurs, record it without interpretation. R10 implies no semantic conclusion.

A PASS only establishes that issue #19 remains a natural executable frontier after K7S. It does not earn K8 or a second constructor-development generation.