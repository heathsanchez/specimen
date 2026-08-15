from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()
old = '''  -- Phase 1: flatten function calls into fresh unknowns with equality hypotheses
  let funcAppExprs ← collectUnmatchableProperSubterms conclusion
  trace[plausible.deriving.arbitrary] m!"Unmatchable exprs: {funcAppExprs} In conclusion: {conclusion}"
'''
new = '''  -- Phase 1: flatten function calls into fresh unknowns with equality hypotheses
  let funcAppExprs ← collectUnmatchableProperSubterms conclusion
  -- V131 diagnostic only: distinguish computed applications that occur in the
  -- dependent type/family index of an output-position term from ordinary
  -- computed value expressions. This leaves `funcAppExprs` unchanged.
  let rec occursExpr (needle haystack : Expr) : Bool :=
    if needle == haystack then true
    else
      match haystack with
      | .app f a => occursExpr needle f || occursExpr needle a
      | .lam _ ty body _ | .forallE _ ty body _ =>
        occursExpr needle ty || occursExpr needle body
      | .letE _ ty val body _ =>
        occursExpr needle ty || occursExpr needle val || occursExpr needle body
      | .mdata _ body | .proj _ _ body => occursExpr needle body
      | _ => false
  let conclusionArgs := conclusion.getAppArgs
  for e in funcAppExprs do
    let mut inOutputType := false
    let mut inOutputValue := false
    for i in outputIndices do
      if h : i < conclusionArgs.size then
        let arg := conclusionArgs[i]
        if occursExpr e arg then
          inOutputValue := true
        let argType ← inferType arg
        if occursExpr e argType then
          inOutputType := true
    logInfo m!"V131_ROLE candidate={e} output_dependent_type={inOutputType} output_value={inOutputValue}"
  trace[plausible.deriving.arbitrary] m!"Unmatchable exprs: {funcAppExprs} In conclusion: {conclusion}"
'''
if old not in text:
    raise SystemExit("V131 instrumentation anchor not found")
if text.count(old) != 1:
    raise SystemExit(f"V131 instrumentation anchor count != 1: {text.count(old)}")
path.write_text(text.replace(old,new,1))
