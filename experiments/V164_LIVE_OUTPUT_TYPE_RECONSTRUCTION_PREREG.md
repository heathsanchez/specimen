# V164 — Live output-type reconstruction

## Status
Frozen before execution.

## Evidence boundary
V159 and V161 localize a standalone deriver residual to output types that depend on a term-level structure projection. V161 showed the free-fvar failure even when no value of the projected leaf is generated. Source audit shows standalone code uses the original existential `outputTypes` after entering a freshly reconstructed inductive-argument context, whereas the mutual compiler already recomputes live argument types with `getCorrectTypes`.

Because upstream PR #47 has now been inspected, this is classified as a source-informed mechanistic repair experiment, not independent novelty.

## Candidate
`LIVE_OUTPUT_TYPE_RECONSTRUCTION`:
- inside the fresh inductive-argument context, call existing `getCorrectTypes` on the fresh argument fvars;
- select output-position types from those live types;
- use those live output types for schedule output triples and MExp output-type assembly;
- pass the live output types through final standalone instance assembly;
- change nothing about requirement threading, flattening, schedule search, class discovery, dependency closure, or legacy command routing.

## Frozen arms
All use K2 + K5. The intervention changes only output-type reconstruction.

1. A0: V161 D0 baseline must reproduce FREE_FVAR.
2. A1: V161 D1 baseline must reproduce FREE_FVAR.
3. I0: D0 under candidate must no longer produce FREE_FVAR and must elaborate successfully.
4. I1: D1 under candidate must move past FREE_FVAR; because no dependent requirement threading is enabled in legacy `derive_generator`, an ordinary `Arbitrary p.A` synthesis residual is acceptable and expected. A direct PASS is also acceptable.
5. I2: plain-type control must remain PASS.
6. I3: V159 recursive `List s.Atom` family must move past FREE_FVAR; downstream requirement/synthesis failure is acceptable evidence that this specific reconstruction residual is removed.
7. Protected full `lake build` and `lake test` must PASS.

## Verdicts
- `PASS_V164_LIVE_OUTPUT_TYPE_RECONSTRUCTION_CAUSAL`: A0/A1 reproduce FREE_FVAR; I0 PASS; I1 and I3 are not FREE_FVAR; I2 PASS; protected pass.
- `NEGATIVE_V164_RECONSTRUCTION_NOT_SUFFICIENT`: valid ablations reproduce but candidate leaves FREE_FVAR in any targeted intervention.
- `R10_*`: candidate compile, fixture, or protected distortion.

## Claim boundary
A PASS admits only a repair for stale output-type binders in standalone constrained derivation. It does not admit structure-leaf class propagation, V156 finite arity, dependency closure, or external PR47 parity.
