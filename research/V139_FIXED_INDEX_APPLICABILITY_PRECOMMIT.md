# V139 — Fixed-index applicability discriminator

Date frozen: 2026-08-16 NZST

## Prior residual

V134 did not reach its intended specialization-before-instance-synthesis question. Under exact admitted K2+K5, the generic arm failed as expected with `Plausible.Arbitrary p_1.Meta`, but the fixed arm failed earlier with `V134P0 is expected to be a variable.` Inspection of the frozen derivation path shows that non-output family/constructor arguments are rejected unless they are free variables.

This is therefore an applicability/representation/access residual, not evidence for or against specialization before instance synthesis.

## Question

Is the V134 fixed-arm failure caused specifically by the derivation surface rejecting a concrete fixed family index, rather than by the later symbolic-instance barrier that V134 intended to test?

## Frozen apparatus

Use the V134 controlled family unchanged in meaning:

- `P` has `Meta : Type`.
- `P0 : P` has `Meta := Unit`.
- `Box (p : P)` carries `p.Meta`.
- `Has` witnesses a `Box p`.

Apply exact admitted K2+K5 unchanged. No K6 or source repair is allowed in V139.

Run four matched presentation arms, all generated before interpreting outcomes:

1. `GENERIC_VAR`: `p : P` appears as the family index. This is the positive applicability control and should reach instance synthesis, normally exposing `Arbitrary p.Meta`.
2. `DIRECT_CONST`: the output family index is the concrete definition `P0`, matching V134.
3. `ABBREV_CONST`: the output type is routed through a reducible abbreviation `Box0 := Box P0`; this changes only presentation, not semantics.
4. `WRAPPER_CONST`: a fresh one-constructor wrapper has a field of type `Box P0`, and the derived output is the wrapper. This changes the outer representation while preserving the same fixed indexed payload and provides a separator for whether rejection is tied specifically to the top-level family argument position.

The direct and abbreviation arms are semantically the same fixed target. The wrapper arm is a diagnostic representation separator and is not allowed to count as solving the original target.

## Frozen classification

For each arm record exit code and the first dominant diagnostic class:

- `NON_FVAR_APPLICABILITY` iff diagnostics contain `expected to be a variable`.
- `SYMBOLIC_INSTANCE` iff diagnostics contain an `Arbitrary`, `Synth`, or typeclass instance failure involving a symbolic `.Meta` term.
- `PASS` iff Lean accepts the derivation.
- otherwise `OTHER_FAILURE`.

## Gates

A1 — exact K2+K5 apply and the derivation module builds.

A2 — `GENERIC_VAR` reaches `SYMBOLIC_INSTANCE` rather than `NON_FVAR_APPLICABILITY`.

A3 — `DIRECT_CONST` is `NON_FVAR_APPLICABILITY`.

A4 — `ABBREV_CONST` is either `NON_FVAR_APPLICABILITY` or, if elaboration preserves the abbreviation surface far enough, reaches a later class; its result is reported without post-hoc gate changes.

A5 — no Strata-specific name, V134 outcome-dependent edit, or K6 repair is introduced.

Verdict `PASS_V139_FIXED_INDEX_APPLICABILITY_BARRIER` iff A1, A2, A3, and A5 hold. A4 is descriptive and cannot rescue or invalidate the primary causal separator.

If `DIRECT_CONST` reaches `SYMBOLIC_INSTANCE`, verdict `NULL_V139_DIRECT_CONSTANT_REACHES_INSTANCE_SYNTHESIS`; V134's prior fixed-arm diagnostic was not stable under exact replay.

If `GENERIC_VAR` does not reach the expected later symbolic-instance stage, verdict `INVALID_V139_GENERIC_CONTROL`.

## Successor licensing

A V139 PASS licenses a separately frozen K6 whose only purpose is to admit/preserve concrete fixed family arguments through the derivation representation far enough to reach the same downstream schedule/instance-synthesis machinery. K6 must then be tested with:

- DIRECT fixed target,
- generic control,
- K6 ablation,
- exact K2+K5 retained,
- full protected build/test,
- and the original V134 scientific discriminator after the applicability barrier is removed.

V139 itself does not admit K6 and does not establish constructor growth.

## Claim boundary

A PASS establishes only that the current Specimen derivation surface has a causal fixed-index applicability boundary before the V134 specialization question. It does not establish that specialization would succeed or fail after that boundary is removed, and it does not establish open-ended development.