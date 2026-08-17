# V146R instance-demand context retention — frozen diagnostic

Controller: Rigorous Breakthrough Stack v1.1.

## Status entering V146R

V145 moved the direct fixed-index residual from non-fvar applicability to `Arbitrary fixedInput...Meta`. V146 attempt 1 tried global demand re-elaboration, but produced unknown-identifier diagnostics and failed the protected test gate, so that intervention is invalid as a scientific separator.

## Question

At the exact generic unconstrained-producer instance-demand boundary, does the current Lean local context still contain the V145 let-bound fixed input whose user name appears in the reconstructed demand type?

## Frozen diagnostic

Keep exact K2+K5+V145 semantics unchanged. Add trace-only instrumentation to `MExp.unconstrainedProducer` recording:

1. the incoming generated demand type syntax;
2. the user names of all fvars actually present in `getLCtx` at that point.

Do not re-elaborate, normalize, rewrite, synthesize, or otherwise change the demand. Enable the existing trace category only in the diagnostic target invocation.

## Decision rule

- `CONTEXT_BINDING_DROPPED_BEFORE_INSTANCE_DEMAND` iff a direct fixed target produces a demand containing the synthetic fixed-input name while that name is absent from the local-context-name trace at the same demand boundary.
- `FIXED_BINDING_RETAINED_AT_INSTANCE_DEMAND` iff the demand contains the fixed-input name and that same name is present in the local-context trace.
- `INVALID_DIAGNOSTIC` if the trace does not reach the target demand or instrumentation changes baseline behavior/protected behavior.

## Controls

- Direct target must retain the V145 `Arbitrary fixedInput...Meta` failure because instrumentation is trace-only.
- Symbolic control must retain `Arbitrary p...Meta`.
- Full `lake build` and `lake test` must pass with instrumentation installed and tracing disabled by default.
- Patch must be source-generic and trace-only.

## Claim boundary

This diagnostic localizes information availability only. It does not admit K6 or establish a repair, transfer, or developmental constructor growth.
