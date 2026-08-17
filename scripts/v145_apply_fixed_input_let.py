from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()

anchor = '''/-- Parses the user-supplied derivation constraint, extracting the input args, output vars, output types,
    constraining inductive name, its levels, and its arguments. Supports multiple existential outputs. -/
private def withParsedDerivingArgs (input : Expr)
'''

helper = r'''/-- V145 K6: true only when an elaborated expression still depends on local
    variables/metavariables/bound variables. A fixed-input let is introduced only
    for relation arguments that are fully closed at this boundary. -/
private partial def v145HasLocalDependency : Expr → Bool
  | .bvar _ => true
  | .fvar _ => true
  | .mvar _ => true
  | .sort _ => false
  | .const _ _ => false
  | .app f a => v145HasLocalDependency f || v145HasLocalDependency a
  | .lam _ ty body _ => v145HasLocalDependency ty || v145HasLocalDependency body
  | .forallE _ ty body _ => v145HasLocalDependency ty || v145HasLocalDependency body
  | .letE _ ty val body _ =>
      v145HasLocalDependency ty || v145HasLocalDependency val || v145HasLocalDependency body
  | .lit _ => false
  | .mdata _ body => v145HasLocalDependency body
  | .proj _ _ body => v145HasLocalDependency body

private def v145IsOutputFVar (outVars : Array Expr) (arg : Expr) : Bool :=
  arg.isFVar && outVars.any (fun out => out.isFVar && out.fvarId! == arg.fvarId!)

/-- Preserve a closed non-output relation argument by introducing a local let
    whose value is exactly the already-elaborated argument. The continuation is
    TermElabM, so downstream schedule compilation retains its native monad stack. -/
private partial def withV145FixedInputLetsAux
    (outVars : Array Expr) (remaining : List Expr) (acc : Array Expr) (idx : Nat)
    (action : Array Expr → TermElabM α) : TermElabM α := do
  match remaining with
  | [] => action acc
  | arg :: rest =>
    if !v145IsOutputFVar outVars arg && !v145HasLocalDependency arg then
      let ty ← inferType arg
      let localCtx ← getLCtx
      let name := localCtx.getUnusedName ((`fixedInput).appendAfter s!"_{idx}")
      withLetDecl name ty arg fun fixedArg =>
        withV145FixedInputLetsAux outVars rest (acc.push fixedArg) (idx + 1) action
    else
      withV145FixedInputLetsAux outVars rest (acc.push arg) (idx + 1) action

private def withV145FixedInputLets (outVars : Array Expr) (indArgs : Array Expr)
    (action : Array Expr → TermElabM α) : TermElabM α :=
  withV145FixedInputLetsAux outVars indArgs.toList #[] 0 action

'''

if "private partial def v145HasLocalDependency" not in text:
    if anchor not in text:
        raise SystemExit("V145 helper anchor not found")
    text = text.replace(anchor, helper + anchor, 1)

old = '''  action args outVars outTypes indName indLevels indArgs
'''
new = '''  withV145FixedInputLets outVars indArgs fun fixedIndArgs =>
    action args outVars outTypes indName indLevels fixedIndArgs
'''

count = text.count(old)
if count != 1:
    raise SystemExit(f"V145 expected exactly one parsed-action anchor, found {count}")
text = text.replace(old, new, 1)

path.write_text(text)
print("V145 K6_FIXED_INPUT_LET applied at parsed relation-argument boundary")
