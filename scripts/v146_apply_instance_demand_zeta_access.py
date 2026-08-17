from pathlib import Path

path = Path("Specimen/MExp.lean")
text = path.read_text()

old = '''def unconstrainedProducer (prodSort : ProducerSort) (ty : TSyntax `term) : CompileScheduleM MExp := do
  let typeClassName :=
    match prodSort with
    | .Enumerator => ``Enum
    | .Generator => ``Arbitrary
  let typeClassInstance ← `( $(Lean.mkIdent typeClassName) $ty:term )
'''

new = '''def unconstrainedProducer (prodSort : ProducerSort) (ty : TSyntax `term) : CompileScheduleM MExp := do
  -- V146 separator: re-elaborate the already-generated demand type in the
  -- still-live local context and ask only Lean's ordinary reducible WHNF to
  -- expose any value already available through local let declarations.
  let demandExpr ← elabTerm ty .none
  let demandExpr ← Lean.Meta.withTransparency .reducible <| Lean.Meta.whnf demandExpr
  let localCtx ← getLCtx
  let normalizedTy ← delabExprInLocalContext localCtx demandExpr
  let typeClassName :=
    match prodSort with
    | .Enumerator => ``Enum
    | .Generator => ``Arbitrary
  let typeClassInstance ← `( $(Lean.mkIdent typeClassName) $normalizedTy:term )
'''

count = text.count(old)
if count != 1:
    raise SystemExit(f"V146 expected exactly one unconstrainedProducer anchor, found {count}")
text = text.replace(old, new, 1)
path.write_text(text)
print("V146 instance-demand reducible WHNF normalization applied")
