from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()

# Generic helper: ordinary arguments remain local declarations; a concrete
# non-output argument becomes a let-bound fvar whose value is the original
# elaborated expression.  This preserves definitional equality rather than
# inventing an unconstrained variable.
anchor = "open Lean Elab Command Meta Term Parser\nopen Idents Schedules ProofWidgets\n"
helper = r'''

/-- V140 K6: introduce argument declarations while preserving concrete fixed
    argument values as let-bound free variables. -/
partial def withPreservedFixedArgumentDecls {α : Type}
  (decls : List (Name × Expr × Option Expr)) (k : MetaM α) : MetaM α := do
  match decls with
  | [] => k
  | (n, ty, val?) :: rest =>
    match val? with
    | some val =>
      withLetDecl n ty val fun _ =>
        withPreservedFixedArgumentDecls rest k
    | none =>
      withLocalDeclD n ty fun _ =>
        withPreservedFixedArgumentDecls rest k
'''
if helper.strip() not in text:
    if anchor not in text:
        raise SystemExit("V140 helper anchor not found")
    text = text.replace(anchor, anchor + helper, 1)

old_map_a = '''  let argNames ← constrArgs.mapIdxM
    (fun i (ident : Expr) =>
      if ident.isFVar then
        ident.fvarId!.getUserName
      else if let some outIdx := outputIdxs.findIdx? (· == i) then
        outputVars[outIdx]!.fvarId!.getUserName
      else throwError m!"{ident} is expected to be a variable.")
  let argNamesTypes := argNames.zip argTypes
'''
old_map_b = '''  let argNames ← constrArgs.mapIdxM
    (fun i (ident : Expr) =>
      if ident.isFVar then ident.fvarId!.getUserName
      else if let some outIdx := outputIdxs.findIdx? (· == i) then
        outputVars[outIdx]!.fvarId!.getUserName
      else throwError m!"{ident} is expected to be a variable.")
  let argNamesTypes := argNames.zip argTypes
'''
new_map = '''  let argNames ← constrArgs.mapIdxM
    (fun i (ident : Expr) =>
      if ident.isFVar then
        ident.fvarId!.getUserName
      else if let some outIdx := outputIdxs.findIdx? (· == i) then
        outputVars[outIdx]!.fvarId!.getUserName
      else
        pure ((`fixedArg).appendAfter s!"_{i}"))
  let argNamesTypes := argNames.zip argTypes
  let argDecls := (argNamesTypes.zip constrArgs.toList).mapIdx (fun i x =>
    let ((n, ty), original) := x
    let preserve := if original.isFVar || outputIdxs.contains i then none else some original
    (n, ty, preserve))
'''
count = text.count(old_map_a) + text.count(old_map_b)
if count != 6:
    raise SystemExit(f"V140 expected 6 arg-name anchors, found {count}")
text = text.replace(old_map_a, new_map).replace(old_map_b, new_map)

# All six derivation paths build their temporary relation-argument context from
# argNamesTypes.  Route the same body through the mixed decl helper instead.
paren_old = 'withLocalDeclsDND argNamesTypes (fun _ => do'
paren_new = 'withPreservedFixedArgumentDecls argDecls (do'
bare_old = 'withLocalDeclsDND argNamesTypes fun _ => do'
bare_new = 'withPreservedFixedArgumentDecls argDecls do'
replaced = text.count(paren_old) + text.count(bare_old)
if replaced < 6:
    raise SystemExit(f"V140 expected at least 6 context anchors, found {replaced}")
text = text.replace(paren_old, paren_new).replace(bare_old, bare_new)

path.write_text(text)
print(f"V140 K6 applied: arg-name anchors={count}, context anchors={replaced}")
