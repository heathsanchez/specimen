from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()

old = '''def linearizeAndFlatten
  (hypotheses : Array Expr) (conclusion : Expr) (outputIndices : List Nat) (localCtx : LocalContext) :
  UnifyM (Array Expr × Expr × List (Name × Expr) × LocalContext) := do
  -- Phase 1: flatten function calls into fresh unknowns with equality hypotheses
  let funcAppExprs ← collectUnmatchableProperSubterms conclusion
'''

new = '''def linearizeAndFlatten
  (hypotheses : Array Expr) (conclusion : Expr) (outputIndices : List Nat) (localCtx : LocalContext) :
  UnifyM (Array Expr × Expr × List (Name × Expr) × LocalContext) := do
  -- Phase 1: flatten function calls into fresh unknowns with equality hypotheses.
  -- V128 PRESERVE_INPUT_POSITION_COMPUTED_PARAMETER: constructor-local names
  -- are not yet the top-level producer input names at this stage.  Use the
  -- invariant coordinate available before unification instead: relation input
  -- positions in the constructor conclusion.  A proper application whose free
  -- variables all occur in input positions is already determined by those
  -- inputs, so preserve it symbolically rather than manufacturing a fresh
  -- independently-produced unknown plus equality obligation.
  let candidateFuncAppExprs ← collectUnmatchableProperSubterms conclusion
  let rec collectFVarIds (e : Expr) : List FVarId :=
    match e with
    | .fvar id => [id]
    | .app f a => collectFVarIds f ++ collectFVarIds a
    | .lam _ ty body _ | .forallE _ ty body _ => collectFVarIds ty ++ collectFVarIds body
    | .letE _ ty val body _ => collectFVarIds ty ++ collectFVarIds val ++ collectFVarIds body
    | .mdata _ body => collectFVarIds body
    | .proj _ _ body => collectFVarIds body
    | _ => []
  let conclusionArgs := conclusion.getAppArgs
  let mut inputPositionFVars : List FVarId := []
  for i in [:conclusionArgs.size] do
    if i ∉ outputIndices then
      inputPositionFVars := inputPositionFVars ++ collectFVarIds conclusionArgs[i]!
  let fixedInputFVars := List.eraseDups inputPositionFVars
  let funcAppExprs := candidateFuncAppExprs.filter (fun e =>
    let deps := List.eraseDups (collectFVarIds e)
    !(deps.all (fun id => fixedInputFVars.contains id)))
'''

if old not in text:
    raise SystemExit("V128 linearize anchor not found")
if text.count(old) != 1:
    raise SystemExit(f"V128 linearize anchor count != 1: {text.count(old)}")
path.write_text(text.replace(old, new, 1))
