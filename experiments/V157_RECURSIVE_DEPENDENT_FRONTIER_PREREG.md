# V157 — Recursive dependent frontier

## Status
Frozen before execution.

## Question
Does the already-admitted V156 singleton requirement-aware constrained-derivation operator causally extend beyond its one-constructor admission fixtures to structurally different recursive dependent families?

## Prior operator set
K2 + K5 only, plus the admitted V156 operator exactly as frozen in `scripts/v156_apply_requirement_aware_deriver.py`. No V157-specific implementation changes are allowed.

## Frontier F1 — length-indexed recursive sequence
```
structure V157Schema where Atom : Type

def V157Schema0 : V157Schema := ⟨Nat⟩

inductive V157Seq (s : V157Schema) : Nat → List s.Atom → Prop where
  | nil : V157Seq s 0 []
  | cons (x : s.Atom) {n : Nat} {xs : List s.Atom} :
      V157Seq s n xs → V157Seq s (Nat.succ n) (x :: xs)
```
Target: `(fun (s : V157Schema) (n : Nat) => ∃ xs : List s.Atom, V157Seq s n xs)`.

## Frontier F2 — branching recursive tree
```
structure V157World where Label : Type

def V157World0 : V157World := ⟨Bool⟩

inductive V157Tree (α : Type) where
  | leaf : α → V157Tree α
  | fork : V157Tree α → V157Tree α → V157Tree α

inductive V157Full (w : V157World) : Nat → V157Tree w.Label → Prop where
  | leaf (x : w.Label) : V157Full w 0 (.leaf x)
  | fork {n : Nat} {l r : V157Tree w.Label} :
      V157Full w n l → V157Full w n r →
      V157Full w (Nat.succ n) (.fork l r)
```
Target: `(fun (w : V157World) (n : Nat) => ∃ t : V157Tree w.Label, V157Full w n t)`.

## Frozen arms
1. B1: K2+K5 + legacy `derive_generator` on F1. Expected residual class: dependent symbolic instance failure.
2. B2: K2+K5 + legacy `derive_generator` on F2. Expected residual class: dependent symbolic instance failure.
3. I1: Apply the exact frozen V156 operator; derive F1 with `derive_generator_with_requirements`; provide only an exact concrete bridge for `V157Schema0.Atom`; require synthesis at `V157Schema0`.
4. I2: Apply the exact frozen V156 operator; derive F2 with `derive_generator_with_requirements`; provide only an exact concrete bridge for `V157World0.Label`; require synthesis at `V157World0`.
5. Protected: full `lake build` and `lake test` after applying K2+K5+V156.

## Admission gates
- G1 B1 is not PASS and is classified as a dependent/symbolic instance residual.
- G2 B2 is not PASS and is classified as a dependent/symbolic instance residual.
- G3 I1 PASS.
- G4 I2 PASS.
- G5 no V157 token appears in the V156 operator patch.
- G6 protected build PASS.
- G7 protected test PASS.

## Verdicts
- `PASS_V157_RECURSIVE_FRONTIER_CAUSALLY_EXTENDED`: all G1–G7 pass.
- `REJECT_V157_PRIOR_OPERATOR_ALREADY_SUFFICES`: either B1 or B2 passes.
- `NEGATIVE_V157_V156_DOES_NOT_TRANSFER`: baselines fail as required but I1 or I2 fails without R10.
- `R10_*`: malformed fixture, setup, environment, or protected-control distortion.

## Claim boundary
A PASS establishes causal extension of the already-admitted V156 operator to two structurally different constructed recursive frontiers. It does **not** establish natural discovery, autonomous repair-language growth, or a new Lean semantic primitive, because these frontiers were designed after V156 was known.
