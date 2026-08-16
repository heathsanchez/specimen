# V143 — Relation-instance old-closure separator

Frozen: 2026-08-16 NZST
Controller: Rigorous Breakthrough Stack v1.1
Parent hard evidence: V139, V140, V142.

## Motivation

V142 established that an instance-implicit binder external to the constraining relation does not survive into the deriver's symbolic synthesis path. Before inventing K6, one stronger lawful existing mechanism must be tested: Specimen's pre-existing support for typeclass instance parameters carried by the inductive relation itself (`SpecimenTest/DeriveArbitrarySuchThat/InstanceParameterTest.lean`).

## Question

Can the V139 fixed-index target be represented by threading the already-required `Plausible.Arbitrary p.Meta` capability through the relation's ordinary instance-parameter channel, then parameterizing and specializing, with no derivation-engine mutation beyond exact admitted K2+K5?

## Frozen fixture

- `P` has `Meta : Type`.
- `P0 := ⟨Unit⟩`.
- `Box p` carries `p.Meta`.
- The relation is refined only by adding an instance parameter `[Plausible.Arbitrary p.Meta]` to `Has`; its witness semantics remain `Has (Box.mk x)`.
- No fabricated global instance and no target-specific source patch.

## Frozen arms

R0_DIRECT: direct `P0`, using the existing `Arbitrary Unit` relation instance. Expected control: direct fixed index may still fail `NON_FVAR_APPLICABILITY`.

R1_PARAM_REL_INSTANCE: parameterized `p`, explicit relation instance argument `inst : Plausible.Arbitrary p.Meta`, with target `@Has p inst b` in the same pattern already admitted by the repository's instance-parameter test.

R2_FIXED_SPECIALIZATION: same R1 derivation plus `#synth` at `P0` with the existing `Arbitrary Unit` instance.

## Gates

H1 exact K2+K5 module build.
H2 R0 reproduces `NON_FVAR_APPLICABILITY` (presentation control).
H3 R1 PASS.
H4 R2 PASS.
H5 full repository build/test PASS.

## Verdicts

- `REJECT_K6_RELATION_INSTANCE_CLOSURE_SUFFICES` iff H1–H5 hold. Then the V139 residual is solvable by lawful existing composition/representation, so K6 is not licensed for this target.
- `OLD_CLOSURE_RELATION_INSTANCE_OBSTRUCTION` iff H1/H2/H5 hold but R1 or R2 reaches a semantic derivation failure. Only then is K6 construction licensed.
- Parser/runner/build/tooling failures before the scientific mechanism are R10 and imply no semantic conclusion.

## Claim boundary

A PASS rejects K6 for this residual; it does not establish constructor development. A failure licenses K6 construction but does not earn K6. No recursive/open-ended-development claim.