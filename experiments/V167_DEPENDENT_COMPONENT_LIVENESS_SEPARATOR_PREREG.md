# V167 — Dependent component liveness separator

## Status
Frozen before execution.

## Background
V165 genuinely applied live output-type reconstruction and still left the structure-projection FREE_FVAR unchanged. Source audit shows `getComponentsOfArrowType` opens each dependent binder in a temporary local scope and accumulates its domain before returning. This can leave returned dependent domains containing fvars whose scopes have ended. Plain type-parameter derivation nevertheless works, so a raw dangling component alone cannot yet explain the selective structure failure.

## Question
Do raw arrow components contain out-of-scope dependent fvars for both ordinary type parameters and term-level structure parameters, while sequential reconstruction inside a persistent telescope makes both live?

## Frozen probes
Define:
- `V167Plain : (α : Type) → Option α → Prop`
- `V167Struct : (p : V167P) → Option p.A → Prop`

For each relation:
1. call existing `getComponentsOfArrowType` and, after it returns, attempt `inferType` on the second argument domain;
2. independently open the relation type with a persistent `forallTelescope`, call existing `getCorrectTypes` on those live argument fvars, and attempt `inferType` on the reconstructed second domain while the telescope remains open.

## Frozen interpretations
- `PASS_V167_RAW_COMPONENTS_STALE_BUT_SEQUENTIAL_LIVE`: raw second-domain inference fails for both Plain and Struct; sequential reconstructed second-domain inference succeeds for both.
- `PASS_V167_STRUCTURE_ONLY_RAW_STALE`: raw fails only for Struct and sequential succeeds.
- `V167_RAW_COMPONENTS_NOT_SOURCE`: raw Struct is already live or sequential Struct remains invalid.
- `R10_*`: metaprogram probe/setup/protected failure.

## Claim boundary
Mechanism localization only. No production code is modified and no repair is admitted.
