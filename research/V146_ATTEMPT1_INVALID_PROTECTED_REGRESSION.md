# V146 attempt 1 — apparatus-distorted separator

Run: GitHub Actions 31995393610
Artifact: 9276685624
Artifact SHA256: `baa83d2f3dc683b12cb5de5804770faf9f2abec3c96dcd8d86969d046d983cc9`

The first V146 implementation re-elaborated every reconstructed unconstrained-producer demand type before WHNF normalization.

Observed:

- B reproduced the V145 `Arbitrary fixedInput...Meta` residual.
- N compiled, but the direct arm logged `Unknown identifier fixedInput_0_1` and retained `Arbitrary fixedInput_0_1.Meta`.
- G likewise logged `Unknown identifier p_1` and retained `Arbitrary p_1.Meta`.
- Full build passed but protected `lake test` failed.
- A restored the V145 behavior.

## Correct classification

`INVALID_V146_ATTEMPT1_PROTECTED_REGRESSION`

The harness's provisional `PASS_V146_R_ERASURE_AT_OR_BEFORE_INSTANCE_DEMAND` string is **not admitted as the scientific verdict** because the frozen protected gate failed. The unknown-identifier diagnostics are useful obstruction evidence, but the global re-elaboration intervention distorted protected behavior.

## Apparatus repair rule

Do not alter the access-vs-erasure question. Replace semantic normalization with a diagnostic-only context-retention probe at the same instance-demand boundary: record the generated demand type and the user names actually present in the current local context, without changing the demand. This can decide whether the V145 let binding itself is still available at that boundary while preserving baseline semantics.
