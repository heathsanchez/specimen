# V147 let-value IR retention — frozen discriminator

Controller: Rigorous Breakthrough Stack v1.1.

## Prior hard state

V145 fixed-input let causally moved the direct closed-index target from `NON_FVAR_APPLICABILITY` to `Plausible.Arbitrary fixedInput...Meta`, with targeted ablation restoring the original failure, symbolic control remaining symbolic, and full protected build/test green. K6 was not admitted.

V146 attempt 1 was invalid because its normalization intervention regressed protected tests. V146R was trace-only and protected-green, but did not observe the relevant `fixedInput...Meta` demand at `MExp.unconstrainedProducer`, proving only that this was the wrong demand site to localize the residual.

Source inspection shows `Schedules.exprToConstructorExpr` maps every fvar to `ConstructorExpr.Unknown localDecl.userName`.

## Question

When the V145 synthetic fixed input reaches `exprToConstructorExpr`, is it still represented by a local **let declaration carrying the original closed value**, immediately before conversion to name-only `ConstructorExpr.Unknown`?

## Frozen diagnostic

Keep exact K2+K5+V145 behavior unchanged. Add trace-only instrumentation to the `.fvar` branch of `exprToConstructorExpr` recording the complete local declaration before returning `.Unknown localDecl.userName`.

Do not inspect fixture names in source code. Do not branch on declaration kind. Do not change the returned `ConstructorExpr`. Tracing is enabled only in the diagnostic fixtures.

## Arms / controls

- **D — direct closed-index target:** must retain the V145 `Arbitrary fixedInput...Meta` residual.
- **G — generic symbolic target:** must retain `Arbitrary p...Meta`.
- Full protected `lake build` and `lake test` must pass with trace instrumentation present and disabled by default.
- Patch must be source-generic and trace-only.

## Decision rule

`PASS_V147_VALUE_PRESENT_THEN_DISCARDED_AT_IR` iff:
1. a trace for the synthetic fixed input is observed at `exprToConstructorExpr`;
2. that local declaration is a let declaration whose stored value is the original closed fixed expression (or a definitionally equivalent elaborated form);
3. the function then returns the unchanged name-only `.Unknown` representation;
4. D and G retain their prior residuals;
5. protected build/test pass;
6. instrumentation contains no fixture-specific identifier.

`PASS_V147_VALUE_NOT_PRESENT_AT_IR_ENTRY` iff the synthetic fixed input reaches the fvar branch but its local declaration is not let-bound / carries no recoverable value, with all controls green.

`INVALID_V147_DIAGNOSTIC` if the relevant fvar trace is not reached or protected/baseline behavior changes.

## Claim boundary

A `VALUE_PRESENT_THEN_DISCARDED` pass localizes a representation-loss boundary. It licenses, but does not admit, a smallest successor that preserves let-bound values in the schedule IR. It does not itself establish K6, source-distinct transfer, or developmental constructor growth.
