# V146 — Let-bound fixed-index old-closure separator

Frozen 2026-08-16 NZST under Rigorous Breakthrough Stack v1.1, before execution.

## Question

Can the V139 fixed-index applicability residual be solved without K6 by an existing Lean representation: let-bind the closed fixed index locally so the deriver sees an fvar whose value is definitionally the original constant?

No Specimen mechanism is changed. Exact admitted K2 and K5 are applied unchanged.

## Frozen arms

All arms use the same fresh fixture family `V146P`, `V146P0 := ⟨Unit⟩`, `V146Box`, `V146Has`.

- `DIRECT_CONST`: original fixed constant presentation. Expected control class: `NON_FVAR_APPLICABILITY`.
- `GENERIC_VAR`: ordinary variable `p`. Expected control class: `SYMBOLIC_INSTANCE`.
- `LET_BOUND_FIXED`: `let p : V146P := V146P0; ... V146Box p ...` with no new constructor or engine patch.
- `LET_BOUND_FIXED_SYNTH`: same let-bound derivation followed by synthesis of the original fixed `V146P0` constrained producer.
- `LET_BOUND_ABBREV_SYNTH`: source-distinct presentation using an abbrev for the fixed box type after the same let-bound derivation.

## PASS / rejection rule

If both let-bound derivation and original fixed specialization synthesize under unchanged K2+K5 while direct/generic controls reproduce and the protected build/test suite remains green, verdict is `REJECT_K6_LET_BOUND_OLD_CLOSURE_SUFFICES`.

If the let-bound path reaches the same or a new residual without solving fixed specialization, K6 remains licensed but not earned.

Any parse/elaboration problem that prevents the intended let-bound representation from being exercised is R10/apparatus inconclusive and has no semantic meaning.

## Claim boundary

This is an old-language closure test only. It cannot establish constructor development or K6.