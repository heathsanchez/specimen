# V161 — Structure-projection layer separator

## Status
Frozen before execution.

## Background
V159 isolated the V157 free-variable residual to a later inductive argument whose type depends on a term-level structure projection (`s.Atom`). That does not yet distinguish dependent-type reconstruction from the earlier fixed-subterm/leaf-generation path.

## Question
Does merely mentioning `s.Atom` in the output type trigger the free-fvar residual, or is an actual generated value of type `s.Atom` required?

## Frozen arms
K2 + K5 only; legacy `derive_generator`; no V156.

### D0 — projection-dependent output, no leaf value generated
```
structure P where A : Type
inductive R0 (p : P) : Option p.A → Prop where
  | none : R0 p none
```
Target: `fun (p : P) => ∃ x : Option p.A, R0 p x`.
The output type depends on `p.A`, but the only constructor produces `none`; no value of `p.A` is generated.

### D1 — projection-dependent output with leaf generation
```
inductive R1 (p : P) : Option p.A → Prop where
  | some (a : p.A) : R1 p (some a)
```
Same target shape. A value of `p.A` must be generated.

### C — plain-type control
Same as D1 with `α : Type` replacing structure `p`; expected to avoid FREE_FVAR.

## Frozen interpretations
- `PASS_V161_DEPENDENT_TYPE_RECONSTRUCTION_IMPLICATED`: D0 and D1 are FREE_FVAR, C is not.
- `PASS_V161_LEAF_GENERATION_PATH_IMPLICATED`: D0 is not FREE_FVAR, D1 is FREE_FVAR, C is not.
- `V161_BROADER_PROJECTION_RESIDUAL`: another stable pattern.
- `R10_*`: malformed fixture or protected failure.

## Claim boundary
Mechanism localization only. No repair is admitted or implemented by V161.
