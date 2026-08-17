# V135 — K6 Specialize-Before-Instance-Synthesis

Status: PRECOMMITTED BEFORE K6 IMPLEMENTATION

## Starting state

- Exact base: Specimen commit `25f7154e3333ec03683bd71536fdd3a060860ba3`.
- K2 is the admitted binder-aware implicit-fixed-parameter constructor rule from V120.
- K5 is the admitted preserve-input-determined-output-dependent-type-application rule from V132.
- V134 clean discriminator run `31998680174` returned `PASS_V134_SPECIALIZATION_INSTANCE_DISCRIMINATOR`.
- In the fixed arm, `V134P0.Meta` is definitionally `Unit`, yet derivation still failed by requesting `Arbitrary a_1.Meta`, the same symbolic obligation as the generic arm.

## Residual

K2+K5 preserve the relevant dependent application, but a target specialization that is already fixed at the top-level relation is not propagated into the downstream typeclass obligation before instance synthesis.

Observed bounded residual:

`P0.Meta ≡ Unit` at the target, but downstream synthesis requests `Arbitrary a.Meta` rather than `Arbitrary Unit`.

## K6 hypothesis

**SPECIALIZE_BEFORE_INSTANCE_SYNTHESIS**

Before asking Lean to synthesize a required instance whose type depends on relation parameters, apply only substitutions already justified by the derived target / fixed-input unification state. Then synthesize the resulting specialized obligation.

K6 may not:

- invent an instance;
- add an `Arbitrary P0.Meta` or target-specific instance;
- special-case `V134P`, `V134P0`, `Meta`, or `Unit`;
- widen global instance search;
- guess substitutions not already licensed by the relation target/unification state;
- alter K2 or K5 semantics.

The intended law is approximately:

`Synth(C[α])` → `σ := lawful-fixed-specialization(α)` → `Synth(C[σ(α)])`

where `σ` is derived only from already-established input/target equalities.

## V135 acquisition arms

A. **K2+K5 baseline** — exact V134 fixed arm. Expected FAIL with symbolic `Arbitrary *.Meta`.

B. **K2+K5+K6 intervention** — same fixed arm. Required PASS.

C. **K2+K5+K6 generic control** — exact V134 generic arm. It must still FAIL when the parameter is genuinely symbolic and no `Arbitrary p.Meta` is provided. A generic pass is evidence K6 broadened the language unsafely.

D. **K6 ablation** — remove only K6 from the intervention state. Required return to the V134 symbolic-instance residual.

## Negative control

Add a fixed family whose specialization leaves a genuinely instance-less concrete type. K6 must specialize the obligation and still fail instance synthesis; it must not fabricate evidence.

## Transfer gate

Before implementation, freeze at least one source-distinct dependent family with the same structural condition but different identifiers and projection shape. K6 must transfer unchanged.

## Protected gate

If acquisition succeeds, apply K2+K5+K6 to the full protected Specimen suite used to admit K5. Required: no regression relative to K2+K5. The historical K5 admission suite was 137/137.

## Verdict hierarchy

- `PASS_V135_K6_ACQUISITION`: fixed baseline fails with V134 residual; K6 fixed intervention passes; generic and missing-instance controls remain appropriately failing; K6 ablation restores V134 residual.
- `NULL_V135_K6_DOES_NOT_SOLVE_SPECIALIZATION_BARRIER`: K6 intervention does not solve fixed arm despite valid apparatus.
- `REJECT_V135_K6_OVERBROAD`: generic or missing-instance control passes, or protected evaluation regresses.
- `R10_INCONCLUSIVE_V135_APPARATUS`: unrelated parsing/build/environment failure.

## Claim boundary

A V135 acquisition pass earns K6 only within the tested specialization-before-instance-synthesis scope. It does **not** establish constructor development or multi-generation compounding. Those require protected transfer and a later frontier whose discovery is causally dependent on the admitted K6 lineage.
