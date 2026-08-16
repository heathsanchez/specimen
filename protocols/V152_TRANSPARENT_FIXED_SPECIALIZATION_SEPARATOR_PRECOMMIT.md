# V152 — Transparent fixed-specialization separator

Frozen 2026-08-16 NZST under Rigorous Breakthrough Stack v1.1 before any V152 outcome.

## Residual

V151B1 used the byte-identical V151B fixture and established:
- `#synth Plausible.Arbitrary Unit` succeeds;
- `#synth Plausible.Arbitrary Bool` succeeds;
- `#synth Plausible.Arbitrary P0.Meta` fails when `P0` is an ordinary `def := ⟨Unit⟩`;
- `#synth Plausible.Arbitrary Q0.Carrier` fails when `Q0` is an ordinary `def := ⟨Bool⟩`;
- minimal dependent class synthesis at those opaque fixed values also fails.

Thus V151/V151A's concrete specialization gates were confounded by transparency of the fixed value. This is distinct from the already-observed fact that a correctly scoped dependent premise lets the generic instance body elaborate.

## Frozen separator

No Specimen source is modified.

Use the same two source-distinct families as V151A, but define the fixed values as transparent abbreviations:
- `abbrev P0 : P := ⟨Unit⟩`
- `abbrev Q0 : Q := ⟨Bool⟩`

For each family test:
1. direct projected capability synthesis: `#synth Plausible.Arbitrary P0.Meta` / `Q0.Carrier`;
2. the same correctly scoped generic hand-written constrained producer instance `{p} [Arbitrary p.Meta] : ArbitrarySizedSuchThat ...`;
3. concrete `#synth ArbitrarySizedSuchThat ... P0/Q0`.

A control retains ordinary opaque `def` fixed values and must reproduce the fixed projected-capability failure.

## PASS and interpretation

`PASS_V152_TRANSPARENT_SPECIALIZATION_CONFIRMED` iff:
- opaque controls fail projected capability synthesis;
- transparent projected capabilities succeed for A and B;
- transparent generic dependent constrained-producer instances elaborate and concrete fixed-value synthesis succeeds for A and B;
- untouched protected `lake build` and `lake test` pass.

A PASS establishes only that transparent fixed specialization plus a correctly scoped dependent premise is sufficient in these frozen families. It does **not** establish that Specimen's derivation machinery can discover/emit that premise, does not earn K6, and does not establish constructor development.

A PASS licenses a new minimal K6 candidate whose target is binding-aware transport/rebinding of discovered dependent requirements, while using transparent fixed values only in the fixed-specialization acceptance gate.

If transparent specialization fails, reject this route and do not implement that K6 candidate.