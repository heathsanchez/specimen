# V144 — Auto-derive context-loss separator

Frozen: 2026-08-16 NZST
Controller: Rigorous Breakthrough Stack v1.1
Parent hard evidence: V139, V140, V142, V143.

## Rival diagnosis

Before constructing K6, inspect the two already-existing `derive_mutual` routes.

The auto-derive route parses only `(inductiveName, outputIndices, deriveSort)` into a `SpecKey` and derives schedules from that key. It does not carry the lambda-bound `_args` from the user specification into `deriveBestInductiveSchedule`.

The fallback route (`specimen.autoDeriveDeps = false`) elaborates the full user term, calls `withParsedDerivingArgs`, and passes `args` into `deriveConstrainedProducerParts`.

Therefore the V142/V143 context loss may be a routing/path limitation rather than a missing constructor capability.

## Question

Does disabling the auto-derive route, while holding exact K2+K5 and the same semantic fixture fixed, preserve enough ambient dependent context for the parameterized-instance closure to succeed and specialize to the original fixed target?

## Frozen arms

- A0_AUTO_DIRECT: current default auto-derive route, direct `P0`. Control: `NON_FVAR_APPLICABILITY`.
- A1_AUTO_PARAM_INSTANCE: current default auto-derive route, parameterized `p` with instance-implicit `[inst : Plausible.Arbitrary p.Meta]`. Control: `SYMBOLIC_INSTANCE`.
- F0_FALLBACK_DIRECT: same direct `P0`, with `set_option specimen.autoDeriveDeps false`. This tests whether the route alone changes direct applicability.
- F1_FALLBACK_PARAM_INSTANCE: same parameterized instance-scoped target with auto-derive disabled.
- F2_FALLBACK_SPECIALIZATION: same F1 derivation plus explicit `#synth` at `P0`.

No change to `Specimen/DeriveConstrainedProducer.lean` beyond exact admitted K2+K5 is permitted.

## Gates / verdicts

P1 exact K2+K5 builds and protected suite remains green.
P2 A0/A1 replay V139/V142 controls.
P3 F1 passes.
P4 F2 passes.

If P1–P4 hold: `REJECT_K6_ROUTING_PATH_EXPLAINS_CONTEXT_LOSS`. K6 is not licensed for this residual; the remaining issue is an auto-derive path/context propagation defect or representation limitation.

If P1/P2 hold and F1/F2 fail at the same semantic context boundary: `K6_REMAINS_LICENSED_AFTER_ROUTING_SEPARATOR`.

Parser/option/runner/build failures before the intended path is exercised are R10 and imply no semantic conclusion.

## Claim boundary

Even a routing PASS does not establish constructor development. A routing failure only licenses a separately frozen K6 intervention; it does not earn K6.