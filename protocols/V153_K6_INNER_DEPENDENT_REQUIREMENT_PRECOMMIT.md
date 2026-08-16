# V153 — K6 inner-dependent requirement threading precommit

Frozen 2026-08-16 NZST under Rigorous Breakthrough Stack v1.1 before any V153 intervention outcome.

## Evidence inherited

- V139/V140/V142/V143/V144/V147 exhausted the identified lawful old-constructor/routing routes without solving the dependent fixed-index residual.
- V148 `K6_DEPENDENT_REQUIREMENT_THREADING` was NEGATIVE: adding the discovered dependent requirement only to the outer generated instance did not solve primary or held-out families and protected tests regressed. It is rejected as sufficient.
- V151/V151A showed that a correctly scoped dependent premise lets the generic hand-written constrained-producer body elaborate in two source-distinct families, but their concrete gates were confounded by opaque fixed definitions.
- V151B1 established that `Arbitrary Unit` and `Arbitrary Bool` exist while projections through ordinary opaque `def` fixed values do not synthesize.
- V152 PASS established that with transparent `abbrev` fixed values, both projected capabilities and both generic hand-written dependent constrained-producer instances specialize successfully, while opaque controls fail.

## Structural residual

The generated producer has two parameter scopes. The top-level instance may carry a requirement about its parameter, but the generated local recursive auxiliary function (`aux_arb` / `aux_enum`) introduces a fresh parameter of the same type. A requirement on the outer parameter is not a requirement on this freshly bound inner parameter. The V148 generated body asks for `Arbitrary innerP.Meta` inside that inner scope.

## Frozen K6 candidate

`K6_INNER_DEPENDENT_REQUIREMENT_THREADING` is the smallest intervention:

1. Preserve the singleton dependent typeclass requirement already discovered by schedule compilation; do not invent a new requirement.
2. Add that requirement as an instance-implicit premise on the top-level generated constrained-producer instance.
3. Add the same requirement shape as an instance-implicit premise on the generated inner auxiliary function, after its ordinary inductive-relation parameters are bound, so it is resolved against the inner parameter scope.
4. Do not special-case fixture names, `Unit`, `Bool`, `P0`, `Q0`, `Meta`, or `Carrier`.
5. Encountering more than one independent discovered dependent requirement is outside this bounded candidate and must fail explicitly rather than silently generalize.

No other derivation/search/routing/scoring behavior may change.

## Frozen fixtures

Apply exact admitted K2 and K5 first using the existing V120 and V132 scripts.

Primary family A:
- structure `P` with dependent field `Meta : Type`;
- transparent fixed `abbrev P0 := ⟨Unit⟩`;
- dependent `Box p` and relation `Has` whose constructor requires `p.Meta`.

Held-out family B:
- structurally renamed `Q` with field `Carrier : Type`;
- transparent fixed `abbrev Q0 := ⟨Bool⟩`;
- dependent `Packet q` and `Accepts`.

The fixture files and hashes are frozen before K6 is applied.

## Arms and gates

BASE/ABLATION = exact K2+K5, no K6. Primary generic derivation must reproduce the symbolic dependent-instance failure.

INTERVENTION A = K2+K5+K6 on primary family. It must:
- derive the generic producer without an unsolved dependent `Arbitrary` error;
- permit concrete `#synth` at transparent P0.

HELD-OUT B = same K6 implementation, source-distinct renamed family, concrete Q0 specialization.

TARGETED ABLATION = remove K6 by using the pre-intervention tree; the prior failure must return.

PROTECTED = full `lake build` and `lake test` after K6 must both pass.

GENERICITY = implementation source must contain none of the frozen fixture identifiers or concrete types.

`PASS_V153_K6_ADMITTED_SCOPED` requires all gates. A PASS earns only the scoped capability `K6_INNER_DEPENDENT_REQUIREMENT_THREADING` for this dependent-requirement class. It does **not** establish constructor development.

Constructor development additionally requires a separately frozen later-frontier experiment in which K6 changes what a later natural constructor/capability frontier can reach or its preregistered cost, with K6 ablation reversing that later advantage.

Any build/parser/harness failure before the K6 mechanism is exercised is R10.