# V143 — Relation-instance old-closure result

Controller: Rigorous Breakthrough Stack v1.1
GitHub Actions run: 31939313545
Artifact: v143-relation-instance-old-closure, ID 9261593008, SHA256 e5b286c08959cebb0177a65e5d4ef63cbae56f97a05c85f039ee0c7fdf2edf72

## Frozen observations

- Exact admitted K2+K5 applied and `Specimen.DeriveConstrainedProducer` built.
- `R0_DIRECT`: the direct fixed presentation reports failed synthesis for `Plausible.Arbitrary V143P0.Meta` and then the V139 applicability residual `V143P0 is expected to be a variable`.
- `R1_PARAM_REL_INSTANCE`: the repository's pre-existing relation-instance route does not close the target; it reaches `unknown free variable p_1` inside derivation.
- `R2_FIXED_SPECIALIZATION`: the same `unknown free variable p_1` remains and fixed specialization is not established.
- Full repository build/test under exact K2+K5: PASS.

Frozen gates: H1=true, H2=true, H3=false, H4=false, H5=true.
Frozen workflow verdict: `OLD_CLOSURE_RELATION_INSTANCE_OBSTRUCTION`.

## Stack classification

V143 closes the strongest remaining old-language composition/refinement route identified from the existing repository: carrying the required capability as an instance parameter of the constraining relation, a mechanism already exercised by the protected `InstanceParameterTest` fixture.

The bounded evidence now supports a scoped structural obstruction:

1. a direct closed/fixed non-output index is rejected by the current applicability surface because non-output constraining-relation arguments are required to be free variables;
2. lifting that index to an ordinary free variable crosses the applicability boundary but exposes a dependent symbolic typeclass requirement;
3. neither an external instance-implicit binder nor the existing relation-instance transport preserves the needed dependent context through this path;
4. the admitted K2+K5 substrate remains protected-green throughout.

This is sufficient to **license** construction of a smallest K6 candidate aimed at preserving fixed/ambient dependent context through constrained-producer derivation. It does not earn K6 and it is not a theorem that every conceivable old encoding is impossible.

## Next separator

The next intervention must be source-generic and structurally targeted. It must not special-case `V143P0`, `Box`, or `Has`. The candidate should explain the observed family of failures by preserving fixed or ambient dependent inputs through derivation and emission while keeping them fixed rather than silently universalizing them.

Required next gates remain baseline/intervention/targeted-ablation, protected behavior, held-out/source-distinct transfer, and later-frontier movement before any constructor-development claim.

No result here establishes K6, constructor development, multi-generation development, recursive development, open-ended development, or operator invention.