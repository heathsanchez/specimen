# V140 — Fixed-index old-constructor closure separator

Date frozen: 2026-08-16 NZST
Controller: Rigorous Breakthrough Stack v1.1
Parent evidence: V139 only.

## Hard prior facts

Under exact admitted K2+K5, V139 established a presentation-specific applicability boundary: a generic free-variable family index reaches the later symbolic `Arbitrary p.Meta` instance-synthesis residual, while semantically fixed direct and reducible-abbreviation presentations stop earlier because the concrete family index is required to be a variable.

V139 did not admit K6 and did not establish constructor development.

## Question

Can the fixed-index target be represented and discharged by lawful composition of mechanisms already available in Lean/Specimen plus exact admitted K2+K5, without changing `Specimen/DeriveConstrainedProducer.lean` beyond those admitted patches?

The specific old-language closure candidate is parameterize-then-specialize:

1. replace the concrete family index at the derivation surface by a section free variable `p : P`;
2. make explicit the already-observed downstream requirement `[Plausible.Arbitrary p.Meta]` rather than inventing a new constructor mechanism;
3. derive the producer using the unchanged derivation machinery;
4. instantiate/specialize the resulting declaration at `p := P0`, using the pre-existing `Arbitrary Unit` instance.

This is a closure test, not a K6 intervention. No source edit that teaches the derivation engine to accept non-fvars is permitted.

## Frozen apparatus

Use the V139 semantic fixture unchanged:

- `P` has `Meta : Type`.
- `P0 : P := ⟨Unit⟩`.
- `Box (p : P)` carries `p.Meta`.
- `Has` witnesses a `Box p`.

Apply exactly:

- `scripts/v120_apply_binder_aware_fixed_parameter.py` (admitted K2), and
- `scripts/v132_apply_output_dependent_input_determined.py` (admitted K5).

No other mutation of `Specimen/DeriveConstrainedProducer.lean` is allowed.

## Frozen bounded closure arms

All arms are materialized before interpreting any arm outcome.

- `C0_DIRECT_CONST`: exact V139 direct concrete target. Negative applicability control.
- `C1_PARAM_NO_INSTANCE`: same target lifted to a section/free variable `p : P`, without an `Arbitrary p.Meta` assumption. This should separate applicability from the downstream instance requirement.
- `C2_PARAM_WITH_INSTANCE`: same parameterized target with `[Plausible.Arbitrary p.Meta]` supplied as an ordinary existing typeclass input. No derivation-engine code changes.
- `C3_FIXED_SPECIALIZATION`: same C2 derivation followed by an explicit elaboration/check that the generated capability can be instantiated at `p := P0` under the existing `Arbitrary Unit` instance. If generated-declaration naming prevents a direct check, the workflow must report `APPARATUS_NAME_DISCOVERY_REQUIRED`; it must not infer specialization success from C2 alone.

A diagnostic `C4_WRAPPER` may replay the V139 wrapper representation, but it cannot rescue the primary closure gate.

## Frozen classifications

Per arm record exit code and dominant diagnostic:

- `PASS` — Lean accepts the complete arm.
- `NON_FVAR_APPLICABILITY` — `expected to be a variable`.
- `SYMBOLIC_INSTANCE` — typeclass synthesis involving symbolic `.Meta`.
- `NAME_DISCOVERY` — C2 derives but the frozen C3 explicit specialization check cannot identify the generated declaration without a separately frozen naming probe.
- `OTHER_FAILURE` — anything else.
- runner/build/network/tooling failures are R10 and carry no semantic conclusion.

## Gates

B1 — exact K2+K5 apply and module builds.

B2 — `C0_DIRECT_CONST = NON_FVAR_APPLICABILITY` (V139 replay/control).

B3 — `C1_PARAM_NO_INSTANCE = SYMBOLIC_INSTANCE`, showing parameterization lawfully crosses only the applicability boundary.

B4 — `C2_PARAM_WITH_INSTANCE = PASS` with no derivation-engine mutation beyond exact K2+K5.

B5 — `C3_FIXED_SPECIALIZATION = PASS`: the capability produced in C2 is explicitly usable/specializable at `P0`, not merely derivable for an abstract parameter.

B6 — full repository build/test or the same protected suite used for K5 admission remains green after exact K2+K5. A protected-suite infrastructure failure is R10, not a semantic fail.

## Verdicts

`REJECT_K6_OLD_CLOSURE_SUFFICES` iff B1–B6 all hold. This means the V139 residual is solvable through lawful old-language composition; no K6 invention is licensed for this residual.

`OLD_CLOSURE_PARTIAL_SPECIALIZATION_UNPROVEN` iff B1–B4 hold but B5 is `NAME_DISCOVERY`/otherwise undecided. A separately frozen naming/specialization separator is then licensed; K6 is still not licensed.

`PASS_V140_OLD_CLOSURE_EXHAUSTED_FOR_FROZEN_FAMILY` iff B1–B3 hold and the bounded closure family fails B4 or B5 for a semantic/representation reason. This does not by itself prove all conceivable old-language encodings impossible; it only closes this preregistered highest-value closure family and licenses the next smallest separator before any K6 construction.

Any apparatus failure => `R10_INCONCLUSIVE`.

## Claim boundary

A successful C2 alone is not enough to reject K6; explicit fixed specialization C3 is required. A failure of this bounded family is not a theorem that no old composition exists. No result here establishes K6, constructor development, recursive development, or open-ended development.