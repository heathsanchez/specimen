# V177 — K6 → K7S dependency discriminator

Status: **PRECOMMITTED BEFORE RUN**

## Question

Does the already-admitted K7S capability require the already-admitted K6 stack in order to produce its verified natural/held-out effect, or are K6 and K7S operationally independent additions that merely occurred sequentially in the historical lineage?

This experiment does **not** test whether Python can spell K7S without K6. It tests a narrower and scientifically necessary causal question about the effective installed regime.

## Frozen substrate

Base: exact V169B workflow head `f56397956313d9a47184a054eecb9f08b56e6e06`.

Frozen fixtures:

- `fixtures/V165_UPSTREAM_ISSUE12_REPRO.lean` — natural target;
- `fixtures/V166_HELDOUT_SINGLE_CTOR_INDUCTIVE.lean` — source-distinct held-out;
- `fixtures/V166_MULTICTOR_WILDCARD_SAFETY.lean` — safety control.

Frozen mechanisms:

- K2: `scripts/v120_apply_binder_aware_fixed_parameter.py`
- K5: `scripts/v132_apply_output_dependent_input_determined.py`
- K6 stack:
  - `scripts/v156_apply_requirement_provenance_promotion.py`
  - `scripts/v156b_apply_checker_consumer_compat.py`
  - `scripts/v158_apply_scope_dependent_promotion.py`
- K7S: `scripts/v168_apply_certified_constructor_irrefutability.py`

No mechanism may be changed after this precommit in response to the result.

## Arms

All arms begin from a clean checkout of `Specimen` / `SpecimenTest`.

- **A — K2 + K5**
- **B — K2 + K5 + K7S, with K6 deliberately absent**
- **C — K2 + K5 + K6, with K7S absent**
- **D — K2 + K5 + K6 + K7S**

The same natural, held-out and safety fixtures are run in all four arms.

B and D additionally must pass full `lake build` and `lake test` for any positive interpretation.

## Frozen interpretations

### NEGATIVE dependency

If A and C reproduce natural+held-out failure, while B and D both pass natural+held-out+safety and protected build/test, then:

`NEGATIVE_V177_K6_NOT_REQUIRED_FOR_K7S_EFFECT`

Interpretation: K7S's verified effect does not depend on K6. The historical sequence is successive capability admission, not causal developmental depth between these two generations.

### POSITIVE execution-level dependency

If A, B and C fail natural+held-out, D passes them, safety remains passing, B and D protected behavior is valid, and the unchanged K7S intervention was actually applied in B, then:

`PASS_V177_K6_REQUIRED_FOR_K7S_EFFECT`

Interpretation: K6 is causally necessary for K7S's verified effect on this frozen frontier. This would establish an execution-level regime interaction, **not** strict raw constructor-language formability.

### NULL / INCONCLUSIVE

Any failure to reproduce the frozen A/C baselines, any protected regression, apparatus failure, or mixed target pattern is not evidence for dependency and receives an explicit null/inconclusive verdict.

## Claim boundary

Even a positive V177 would not prove that K7S was impossible to author in the host language before K6. It would show that the capability's verified operational effect requires the K6-extended effective regime on this frozen target family.

A negative result is equally valuable: it prevents chronological succession from being mislabeled as developmental causation.
