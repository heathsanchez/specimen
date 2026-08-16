# V156 — additive requirement-aware derivation operator

Frozen before implementation outcome is inspected.

## Earned residual
V153 established expressive closure: Lean can express both a generic conditional constrained-producer plus an exact closed-value bridge, and a direct fixed specialized producer, while existing Specimen derivation routes cannot. V155 then accepted an explicit standalone instance binder but dropped it from emitted code; the old standalone route still failed. Core audit shows `deriveConstrainedProducer` already discovers `requiredInstances`, reports them, and discards them before instance assembly.

Therefore the licensed hypothesis is **missing derivation automation**, not new Lean expressivity.

## Candidate operator
Add an opt-in command `derive_generator_with_requirements` that uses the same existing schedule search and MExp compilation as `derive_generator`, but threads the already-discovered dependent typeclass requirements into both the generated outer instance and its inner producer function.

The legacy `derive_generator` path must remain behaviorally unchanged by default. No fixture names, fixed values, `Unit`, `Bool`, `Meta`, or `Carrier` may appear in implementation source.

## Frozen families
A: `P` with field `Meta : Type`, named `def P0 := ⟨Unit⟩`, transparent `abbrev PA := ⟨Unit⟩`, dependent `Box p`, witness relation `Has`.

B held-out: independently named `Q` with field `Carrier : Type`, named `def Q0 := ⟨Bool⟩`, dependent `Packet q`, witness relation `Accepts`.

## Arms and gates
G1 baseline ablation: old `derive_generator` on generic A reproduces `SYMBOLIC_INSTANCE`.

G2 new operator generic A elaborates and installs a conditional producer.

G3 named-def A: after the exact V152 bridge `Arbitrary P0.Meta := by change Arbitrary Unit; infer_instance`, fixed `#synth ArbitrarySizedSuchThat (Box P0) ...` passes.

G4 transparent A: using `abbrev PA`, fixed synth passes with no explicit bridge.

G5 held-out B: new operator elaborates; after exact bridge `Arbitrary Q0.Carrier := by change Arbitrary Bool; infer_instance`, fixed synth passes.

G6 targeted ablation: replacing the new operator with legacy `derive_generator` restores generic symbolic-instance failure on both independently named families.

G7 implementation is generic: forbidden fixture tokens absent from modified Specimen source.

G8 protected `lake build` and `lake test` both pass.

## Verdicts
PASS only if all G1–G8 pass: `PASS_V156_REQUIREMENT_AWARE_OPERATOR_ADMITTED_SCOPED`.

If implementation does not compile or does not exercise requirement threading: R10.

If intended threading executes but A or B fails: `NEGATIVE_V156_OPERATOR_NOT_ADMITTED`.

If fixtures pass but protected suite fails: operator is not admitted.

## Claim boundary
A PASS admits only a **new additive Specimen derivation operator** that automates an already-expressible Lean construction. It does not establish new semantic expressivity, constructor development, developmental dependence, recursion, or open-ended learning. A later independently selected frontier task must show that the admitted operator enables a repair/derivation that the frozen prior operator set cannot reach before any repair-language-growth claim is promoted.