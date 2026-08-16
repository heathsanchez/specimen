from pathlib import Path

p = Path('Specimen/MExp.lean')
s = p.read_text()

anchor = '''private def nameAndConstructorExprToTypedVar (v : Name × Option ConstructorExpr) : Name × Option Expr :=
  Prod.map id (ToExpr.toExpr <$> ·) v
'''
helper = '''private def nameAndConstructorExprToTypedVar (v : Name × Option ConstructorExpr) : Name × Option Expr :=
  Prod.map id (ToExpr.toExpr <$> ·) v

/-- Whether a complete generated pattern is certified structurally irrefutable. -/
private partial def patternIrrefutable (pattern : Pattern) : MetaM Bool := do
  match pattern with
  | .UnknownPattern _ => pure true
  | .LitPattern _ => pure false
  | .CtorPattern ctorName args =>
    match (← getConstInfo ctorName) with
    | .ctorInfo ctorInfo =>
      let inductInfo ← getConstInfoInduct ctorInfo.induct
      if inductInfo.ctors.length != 1 then
        pure false
      else
        for arg in args do
          if !(← patternIrrefutable arg) then
            return false
        pure true
    | _ => pure false
'''
if anchor not in s:
    raise SystemExit('K7S_HELPER_ANCHOR_NOT_FOUND')
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
    raise SystemExit('K7S_MATCH_ANCHOR_NOT_FOUND')
s = s.replace(old, new, 1)

for forbidden in ['V165', 'V166', 'V167', 'V168', 'ISSUE12', 'Issue12', 'Cedar', 'StateResult', 'Packet', 'Choice', 'fixtures/']:
    if forbidden in s:
        raise SystemExit(f'K7S_TARGET_TOKEN_LEAK:{forbidden}')

p.write_text(s)
print('K7S_CERTIFIED_CONSTRUCTOR_IRREFUTABILITY_APPLIED')
