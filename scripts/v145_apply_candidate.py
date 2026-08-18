from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["none", "input", "output", "both", "all"])
args = parser.parse_args()

if args.mode == "none":
    raise SystemExit(0)

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()
old = '''def linearizeAndFlatten
  (hypotheses : Array Expr) (conclusion : Expr) (outputIndices : List Nat) (localCtx : LocalContext) :
  UnifyM (Array Expr × Expr × List (Name × Expr) × LocalContext) := do
  -- Phase 1: flatten function calls into fresh unknowns with equality hypotheses
  let funcAppExprs ← collectUnmatchableProperSubterms conclusion
'''

condition = {
    "input": "inputDetermined",
    "output": "inOutputType",
    "both": "inputDetermined && inOutputType",
    "all": "true",
}[args.mode]

new = f'''def linearizeAndFlatten
  (hypotheses : Array Expr) (conclusion : Expr) (outputIndices : List Nat) (localCtx : LocalContext) :
  UnifyM (Array Expr × Expr × List (Name × Expr) × LocalContext) := do
  -- V145 anonymous candidate policy. Candidate identity is not used by the verifier.
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
  let rec occursExpr (needle haystack : Expr) : Bool :=
    if needle == haystack then true
    else
      match haystack with
      | .app f a => occursExpr needle f || occursExpr needle a
      | .lam _ ty body _ | .forallE _ ty body _ => occursExpr needle ty || occursExpr needle body
      | .letE _ ty val body _ => occursExpr needle ty || occursExpr needle val || occursExpr needle body
      | .mdata _ body | .proj _ _ body => occursExpr needle body
      | _ => false
  let conclusionArgs := conclusion.getAppArgs
  let mut inputPositionFVars : List FVarId := []
  for i in [:conclusionArgs.size] do
    if i ∉ outputIndices then
      inputPositionFVars := inputPositionFVars ++ collectFVarIds conclusionArgs[i]!
  let fixedInputFVars := List.eraseDups inputPositionFVars
  let mut funcAppExprs : List Expr := []
  for e in candidateFuncAppExprs do
    let deps := List.eraseDups (collectFVarIds e)
    let inputDetermined := deps.all (fun id => fixedInputFVars.contains id)
    let mut inOutputType := false
    for i in outputIndices do
      if h : i < conclusionArgs.size then
        let argType ← inferType conclusionArgs[i]
        if occursExpr e argType then
          inOutputType := true
    if !({condition}) then
      funcAppExprs := funcAppExprs ++ [e]
'''

if old not in text:
    raise SystemExit("V145 linearize anchor not found")
if text.count(old) != 1:
    raise SystemExit(f"V145 linearize anchor count != 1: {text.count(old)}")
path.write_text(text.replace(old, new, 1))
