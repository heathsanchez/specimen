# V159 — Dependent argument reconstruction separator

## Status
Frozen before execution and before V158 outcome inspection.

## Residual
V157's two constructed recursive families both failed with an earlier shared error (`unknown free variable s_1` / `w_1`) in both the legacy and V156 arms. Protected build/test remained clean.

## Question
Is that residual caused by recursive derivation generally, by a dependent output type generally, or specifically by reconstructing an inductive argument type that depends on a preceding **structure-valued** parameter?

## Frozen arms
All arms use K2 + K5 only and legacy `derive_generator`; V156 is irrelevant to this separator.

### N — structure parameter, non-dependent output type
A recursive relation carries a structure parameter `s`, but its generated output is `List Nat`, independent of `s`.
Expected: no `unknown free variable` residual.

### T — plain type parameter, dependent recursive output
A recursive sequence relation has a plain `α : Type` parameter and output `List α`.
Expected: no `unknown free variable` residual; ordinary type-parameter binder machinery should handle it.

### S — structure parameter, projection-dependent recursive output
Same recursive sequence shape, but the generated output is `List s.Atom` for `s : Schema`.
Expected: reproduces `unknown free variable`.

## Frozen interpretation
- `PASS_V159_STRUCTURE_DEPENDENT_ARG_RECONSTRUCTION_ISOLATED`: N and T avoid FREE_FVAR; S is FREE_FVAR.
- `V159_GENERAL_DEPENDENT_ARG_RECONSTRUCTION`: both T and S are FREE_FVAR while N is not.
- `V159_GENERAL_RECURSIVE_RESIDUAL`: N also FREE_FVAR.
- `R10_*`: controls malformed or protected suite fails.

## Claim boundary
This is a mechanism-localization experiment only. It does not repair the residual and does not bear on V156's admitted singleton dependent-requirement operator.
