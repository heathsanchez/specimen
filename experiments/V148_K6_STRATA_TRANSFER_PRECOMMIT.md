# V148 K6 source-distinct transfer — frozen target selection

Controller: Rigorous Breakthrough Stack v1.1.

This target is frozen before the V147b local K6 outcome is inspected.

## Pre-existing natural target
Use the vendored Strata Lambda definitions in `SpecimenTest/StrataDefs/LambdaCore.lean` and the documented residual in `SpecimenTest/StrataLexprGen.lean`.

`StrataLexprGen.lean` explicitly records that the real `Lambda.LExpr` carries a structure parameter and that the constrained deriver does not yet handle it; the file therefore substitutes the erased `LExprU` representation to demonstrate other mechanisms. The source-distinct target is to return to the real parameterized relation rather than author a new isomorphic toy.

Frozen specialization:
- define one global `Lambda.LExprParams` value with `Unit` metadata and identifier metadata;
- target the actual `Lambda.LExpr.HasTypeA` relation specialized to that global parameter;
- preserve the pre-existing lookup-producer support and ordinary unconstrained instances needed by the natural Strata relation;
- do not alter `LambdaCore.lean` or the typing relation.

## Conditional execution
Run V148 only if V147b achieves its frozen local causal K6 PASS. Otherwise record `NOT_RUN_LOCAL_K6_NOT_EARNED`.

## Transfer arms
- T0: exact admitted K2+K5, K6 ablated, real Strata fixed-global specialization.
- T1: exact K2+K5+frozen V147b K6 patch, same specialization.

Hold command path (`specimen.autoDeriveDeps false`), toolchain, supporting instances, target, and verifier fixed.

## Transfer PASS
Requires T0 to reproduce a fixed-global applicability obstruction, T1 to derive and synthesize the requested constrained producer for the real Strata `LExpr.HasTypeA` specialization, full protected build/test green under T1, and static confirmation that the K6 source patch contains no Strata/Lambda target names.

A V148 PASS would admit K6 only for the bounded scope `fallback derivation of global fixed relation inputs` across the local synthetic separator plus this source-distinct Strata transfer. It would still not establish constructor development. That requires a subsequent later-frontier causal test with K6 retained vs ablated.