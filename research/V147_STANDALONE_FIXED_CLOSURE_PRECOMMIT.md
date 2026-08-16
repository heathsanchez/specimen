# V147 — Standalone fixed-index old-closure separator

Frozen 2026-08-16 NZST under Rigorous Breakthrough Stack v1.1 before execution.

## Question

Is the V139 fixed-index residual a limitation of the mutual-derivation path rather than a missing constructor capability? Test the same fixed-index fixture using Specimen's pre-existing standalone `derive_generator` mechanism with exact admitted K2 and K5 unchanged.

No Specimen source mechanism is changed by this experiment.

## Frozen fixture and arms

Fixture: `V147P`, `V147P0 := ⟨Unit⟩`, dependent `V147Box p`, relation `V147Has`.

Arms:
- `MUTUAL_DIRECT`: `derive_mutual` with concrete `V147P0`. Control expected `NON_FVAR_APPLICABILITY`.
- `STANDALONE_DIRECT`: `derive_generator` with the identical concrete fixed index.
- `STANDALONE_DIRECT_SYNTH`: standalone derivation followed by `#synth ArbitrarySizedSuchThat (V147Box V147P0) ...`.
- `STANDALONE_ABBREV_SYNTH`: same through an abbrev of the concrete output type.
- `STANDALONE_GENERIC`: standalone derivation over ordinary variable `p`, retained as a diagnostic comparison.

## Decision rule

If the concrete standalone path derives and the original concrete producer synthesizes, with protected build/test green, reject a broad K6/new-constructor interpretation. Classify the residual as scoped to mutual derivation / representation routing and continue with the smallest repair of that path.

If standalone concrete reproduces the non-fvar/symbolic obstruction while controls and protected suite are valid, the fixed-index obstruction survives this old-language route and K6 remains licensed, not earned.

If the standalone syntax is not exercised due parser or fixture apparatus errors, classify R10 and draw no semantic conclusion.

## Claim boundary

Old-language closure separator only. No K6, operator invention, or constructor-development claim.