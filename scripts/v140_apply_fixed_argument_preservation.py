from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()

# Generic helper: ordinary arguments remain local declarations; a concrete
# non-output argument becomes a let-bound fvar whose value is the original
# elaborated expression. This preserves definitional equality rather than
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
  let argDecls : List (Name × Expr × Option Expr) :=
    (argNamesTypes.zip constrArgs).toList.mapIdx (fun i x =>
      let ((n, ty), (original : Expr)) := x
      let preserve : Option Expr := if Expr.isFVar original || outputIdxs.contains i then none else some original
      (n, ty, preserve))
'''
count = text.count(old_map_a) + text.count(old_map_b)
if count != 3:
    raise SystemExit(f"V140 expected 3 arg-name anchors in pinned source, found {count}")
text = text.replace(old_map_a, new_map).replace(old_map_b, new_map)

# Exactly four textual context anchors exist in the pinned source, but one is
# the memoized deriveBestInductiveSchedule path and has no constrArgs/argDecls.
# Preserve that path unchanged; rewrite only the three acquisition/codegen paths
# that contain the frozen applicability guard above.
paren_old = 'withLocalDeclsDND argNamesTypes (fun _ => do'
paren_new = 'withPreservedFixedArgumentDecls argDecls (do'
bare_old = 'withLocalDeclsDND argNamesTypes fun _ => do'
bare_new = 'withPreservedFixedArgumentDecls argDecls do'
text = text.replace(paren_old, paren_new).replace(bare_old, bare_new)
# Restore the one unrelated memoized-schedule context verbatim.
memo_patched = 'let results ← withPreservedFixedArgumentDecls argDecls do'
memo_original = 'let results ← withLocalDeclsDND argNamesTypes fun _ => do'
if memo_patched not in text:
    raise SystemExit("V140 memo-context separator not found")
text = text.replace(memo_patched, memo_original, 1)

remaining = text.count('withPreservedFixedArgumentDecls argDecls')
if remaining != 3:
    raise SystemExit(f"V140 expected exactly 3 preserved-fixed contexts, found {remaining}")

path.write_text(text)
print(f"V140 K6 applied: arg-name anchors={count}, preserved contexts={remaining}")
