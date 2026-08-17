# V146 instance-demand zeta access — frozen precommit

Controller: Rigorous Breakthrough Stack v1.1.

## Prior hard result

V145 `K6_FIXED_INPUT_LET` crossed the direct closed-index non-fvar applicability barrier while preserving protected behavior and causal ablation, but the closed target moved to `Plausible.Arbitrary fixedInput_0_1.Meta`. The symbolic control remained `Plausible.Arbitrary p_1.Meta`. K6 is not admitted.

Source inspection after that result shows that schedule construction represents local fvars as `ConstructorExpr.Unknown userName`, and unconstrained producer compilation later reconstructs a type term from that symbolic schedule representation. The local let declaration created by V145 nevertheless remains in scope while the schedule is compiled.

## Rival explanations

- **R_ACCESS:** the exact fixed value still exists in the live local context, and `fixedInput.Meta` is reducible to its concrete type if the instance-demand type is re-elaborated/normalized there; existing compilation simply never asks for that normalization.
- **R_ERASURE:** by the instance-demand boundary, the information needed to specialize the dependent projection is no longer semantically recoverable from the reconstructed type term/local context. Local normalization will not produce the concrete type.

## Frozen separator

Keep exact K2+K5+V145 fixed-input-let transport unchanged. At the generic unconstrained-producer instance-demand boundary only:

1. take the already-generated type syntax `ty`;
2. elaborate it in the current `TermElabM` local context;
3. normalize only with Lean's ordinary reducible/WHNF machinery;
4. delaborate the normalized expression back to type syntax;
5. request the same existing `Arbitrary`/`Enum` instance using that normalized type.

Do not add any fixture-specific rewrite, projection rule, typeclass instance, equality proof, or special case. Do not alter schedule search, constructor classification, K2, K5, or V145 transport.

## Frozen arms

- **B:** exact K2+K5+V145, no demand normalization. Must reproduce V145 direct residual `Arbitrary fixedInput...Meta`.
- **N:** exact B plus instance-demand normalization above.
- **A:** remove only demand normalization while retaining V145; must restore B.
- **G:** symbolic parameter control. Normalization must not invent `Arbitrary p.Meta`.

## Gates

V146 supports `R_ACCESS` iff all hold:

1. B reproduces the V145 moved residual at `Arbitrary fixedInput...Meta`.
2. N's direct closed target progresses beyond that exact instance-demand residual; strongest outcome is full direct PASS.
3. A restores B.
4. G remains a symbolic missing-instance residual, not a manufactured success.
5. Full protected `lake build` and `lake test` pass under N.
6. Patch is source-generic and changes only the instance-demand normalization boundary.

If N compiles but the direct target retains `Arbitrary fixedInput...Meta`, support `R_ERASURE_AT_OR_BEFORE_INSTANCE_DEMAND` under this bounded separator.

If N fails to compile or cannot reach the separator because the apparatus is malformed, classify R10 and repair apparatus without changing the frozen separator.

## Claim boundary

A V146 pass establishes an access distinction at the instance-demand boundary. It does not admit K6, establish source-distinct transfer, or establish developmental constructor growth.
