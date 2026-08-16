from pathlib import Path

p = Path('Specimen/MExp.lean')
s = p.read_text()

anchor = '''private def nameAndConstructorExprToTypedVar (v : Name × Option ConstructorExpr) : Name × Option Expr :=
  Prod.map id (ToExpr.toExpr <$> ·) v
'''
helper = '''private def nameAndConstructorExprToTypedVar (v : Name × Option ConstructorExpr) : Name × Option Expr :=
  Prod.map id (ToExpr.toExpr <$> ·) v

/-- Whether a single constructor pattern exhausts its parent inductive type. -/
private def constructorPatternExhaustive (pattern : Pattern) : MetaM Bool := do
  match pattern with
  | .CtorPattern ctorName _ =>
    let ctorInfo ← getConstInfoCtor ctorName
    let inductInfo ← getConstInfoInduct ctorInfo.induct
    pure (inductInfo.ctors.length == 1)
  | _ => pure false
'''
if anchor not in s:
    raise SystemExit('K7_HELPER_ANCHOR_NOT_FOUND')
s = s.replace(anchor, helper, 1)

old = '''  | .Match explicit scrutinee pattern =>
    pure $ .MMatch explicit (.MId scrutinee) [(pattern, k), (wildCardPattern, .MFail)]
'''
new = '''  | .Match explicit scrutinee pattern => do
    let exhaustive ← constructorPatternExhaustive pattern
    let cases :=
      if exhaustive then [(pattern, k)]
      else [(pattern, k), (wildCardPattern, .MFail)]
    pure $ .MMatch explicit (.MId scrutinee) cases
'''
if old not in s:
    raise SystemExit('K7_MATCH_ANCHOR_NOT_FOUND')
s = s.replace(old, new, 1)

# Generic-only self-audit: implementation source must not mention experimental targets.
for forbidden in ['V165', 'V166', 'ISSUE12', 'Issue12', 'S.mk', 'V166Packet', 'V166Choice']:
    if forbidden in s:
        raise SystemExit(f'K7_TARGET_TOKEN_LEAK:{forbidden}')

p.write_text(s)
print('K7_EXHAUSTIVE_MATCH_FALLTHROUGH_ELISION_APPLIED')
