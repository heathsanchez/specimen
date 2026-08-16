from pathlib import Path

p = Path('Specimen/MExp.lean')
s = p.read_text()

anchor = '''private def nameAndConstructorExprToTypedVar (v : Name × Option ConstructorExpr) : Name × Option Expr :=
  Prod.map id (ToExpr.toExpr <$> ·) v
'''
helper = '''private def nameAndConstructorExprToTypedVar (v : Name × Option ConstructorExpr) : Name × Option Expr :=
  Prod.map id (ToExpr.toExpr <$> ·) v

/-- Whether a complete generated pattern is structurally irrefutable. -/
private partial def patternIrrefutable (pattern : Pattern) : MetaM Bool := do
  match pattern with
  | .UnknownPattern _ => pure true
  | .LitPattern _ => pure false
  | .CtorPattern ctorName args =>
    let ctorInfo ← getConstInfoCtor ctorName
    let inductInfo ← getConstInfoInduct ctorInfo.induct
    if inductInfo.ctors.length != 1 then
      pure false
    else
      for arg in args do
        if !(← patternIrrefutable arg) then
          return false
      pure true
'''
if anchor not in s:
    raise SystemExit('K7R_HELPER_ANCHOR_NOT_FOUND')
s = s.replace(anchor, helper, 1)

old = '''  | .Match explicit scrutinee pattern =>
    pure $ .MMatch explicit (.MId scrutinee) [(pattern, k), (wildCardPattern, .MFail)]
'''
new = '''  | .Match explicit scrutinee pattern => do
    let irrefutable ← patternIrrefutable pattern
    let cases :=
      if irrefutable then [(pattern, k)]
      else [(pattern, k), (wildCardPattern, .MFail)]
    pure $ .MMatch explicit (.MId scrutinee) cases
'''
if old not in s:
    raise SystemExit('K7R_MATCH_ANCHOR_NOT_FOUND')
s = s.replace(old, new, 1)

# Production source must remain target-agnostic.
for forbidden in ['V165', 'V166', 'V167', 'ISSUE12', 'Issue12', 'Cedar', 'S.mk', 'Packet', 'Choice', 'fixtures/']:
    if forbidden in s:
        raise SystemExit(f'K7R_TARGET_TOKEN_LEAK:{forbidden}')

p.write_text(s)
print('K7R_RECURSIVE_IRREFUTABLE_PATTERN_APPLIED')
