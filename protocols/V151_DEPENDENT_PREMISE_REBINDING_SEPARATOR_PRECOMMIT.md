# V151 — Dependent-premise rebinding separator

Frozen 2026-08-16 NZST under Rigorous Breakthrough Stack v1.1 before any V151 fixture outcome.

## Residual

V148's generic intervention caused the suggested generated instance to print a dependent premise such as `[Plausible.Arbitrary p.Meta]`, but primary and held-out fixtures still failed synthesis and protected tests regressed. Therefore V148 is NEGATIVE and K6 was not admitted.

Inspection leaves two materially different diagnoses:

1. PREMISE_INSUFFICIENT — even a correctly scoped dependent premise is insufficient to make the generated producer lawful/usable;
2. REBINDING/HYGIENE — the premise discovered by `MExp.mexpToTSyntax` was delaborated in an earlier local context and then spliced as syntax into a later emitted command, so names that print identically may not be bound to the later command's parameter.

V151 is the smallest separator. It does not modify Specimen and cannot earn K6.

## Frozen test

Use two source-distinct synthetic families already frozen by V148:
A: `P.Meta`, fixed `P0 := ⟨Unit⟩`, `Box p`, `Has`.
B: `Q.Carrier`, fixed `Q0 := ⟨Bool⟩`, `Packet q`, `Accepts`.

For each family compare:
- BASE: a generic hand-written constrained-producer instance with no dependent premise. It must fail to elaborate/use `Plausible.Arbitrary` for the dependent field.
- REBOUND: the same generic instance, but with the type parameter explicitly bound first and a correctly scoped instance-implicit premise `[Plausible.Arbitrary p.Meta]` / `[Plausible.Arbitrary q.Carrier]`. It must elaborate and a concrete `#synth` at the fixed value must succeed.

The body is intentionally minimal and semantically transparent: generate the dependent payload using `Plausible.Arbitrary.arbitrary`, then wrap it in the relation constructor. No derivation command is used. This is a mechanism separator, not a replacement implementation.

## PASS / interpretation

PASS_V151_REBINDING_RIVAL_CONFIRMED iff:
- BASE A and BASE B fail specifically for missing dependent `Arbitrary`;
- REBOUND A and REBOUND B compile and concrete fixed-value `#synth` succeeds.

A PASS establishes only that a correctly scoped dependent premise is sufficient in principle and that V148's failure is consistent with rebinding/hygiene rather than premise insufficiency. It licenses a minimal K6 candidate that transports required instance expressions through a binding-aware representation and re-delaborates them in the final emitter context.

If REBOUND fails, reject the rebinding diagnosis and do not spend a binding-aware K6 intervention.

No constructor-development, later-frontier, or generality claim follows from V151.