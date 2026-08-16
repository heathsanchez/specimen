# V147b K6 global-fixed-input candidate — frozen precommit

Controller: Rigorous Breakthrough Stack v1.1.

## Closure ledger before construction
The following lawful existing/executable routes were tested under exact admitted K2+K5:
- direct fixed global constant: `NON_FVAR_APPLICABILITY`;
- generic parameterization: moves to dependent `SYMBOLIC_INSTANCE`;
- true instance-implicit binder: still `SYMBOLIC_INSTANCE` (V142);
- existing relation-instance transport: does not close and exposes context/free-variable failure (V143);
- auto-derive vs fallback routing: neither closes (V144).

A further semantic representation rival — local `let p := P0` — was attempted through both `derive_mutual` and standalone `derive_generator`, but both command surfaces reject the let form before schedule derivation. Those V145/V145b outcomes are R10 and are **not evidence that let-bound representation would semantically fail**.

Decision boundary: the currently executable old-constructor/command-language closure is exhausted for the fixed-global case. The unresolved let representation would itself require extending/changing the command surface. V147b therefore tests the smallest source-generic extension that directly represents the already-observed fixed-global residual. This does not claim a proof that all imaginable old encodings are impossible.

## Candidate
`K6_GLOBAL_FIXED_INPUT`: allow a non-output relation argument that is syntactically a global constant to remain a fixed global constant throughout fallback schedule derivation and code emission. It must never be replaced by a fresh universally quantified parameter.

Scope is deliberately narrow:
- global constants only;
- fallback/standalone derivation (`specimen.autoDeriveDeps false`) only;
- no literals, arbitrary closed applications, abbreviations, or auto-derive `SpecKey` path;
- no target-specific names.

## Frozen arms
- B: exact K2+K5, no K6, fixed-global target.
- I: exact K2+K5 + K6_GLOBAL_FIXED_INPUT, same target.
- A: targeted ablation = identical experiment without K6 patch; must reproduce B.
- G: exact K2+K5 + K6 on generic symbolic `p`; must preserve the separate missing-dependent-instance residual.

## Local causal PASS
All required:
1. B = `NON_FVAR_APPLICABILITY`.
2. I derives and `#synth`s the original `ArbitrarySizedSuchThat` predicate at the same global constant.
3. A = `NON_FVAR_APPLICABILITY`.
4. G remains `SYMBOLIC_INSTANCE`.
5. Full protected `lake build` and `lake test` under I are green.
6. Static patch audit contains no fixture/type/relation/global-constant identifiers.

Any malformed patch/build/parser failure before the mechanism is exercised is R10. A residual move without successful synthesis is not a K6 PASS.

## Promotion boundary
A local PASS earns only a scoped K6 candidate. Admission additionally requires a source-distinct held-out fixed-global case frozen before its outcome, with intervention vs targeted ablation and protected behavior. Constructor development additionally requires retained K6 to make a later natural constructor/capability frontier newly reachable or materially cheaper, with K6 ablation reversing that later advantage.