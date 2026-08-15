from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()
old = '''  -- Phase 1: flatten function calls into fresh unknowns with equality hypotheses
  let funcAppExprs ← collectUnmatchableProperSubterms conclusion
  trace[plausible.deriving.arbitrary] m!"Unmatchable exprs: {funcAppExprs} In conclusion: {conclusion}"
'''
new = '''  -- Phase 1: flatten function calls into fresh unknowns with equality hypotheses
  let funcAppExprs ← collectUnmatchableProperSubterms conclusion
  -- V130 diagnostic only: classify which original flattening candidates occur
  -- inside a constructor's fixed parameter arguments.  This does not alter
  -- `funcAppExprs` or generation semantics.
  let rec collectCtorParamApps (e : Expr) : MetaM (List Expr) := do
    let mut out : List Expr := []
    if e.isApp then
      let (fnName, args) := e.getAppFnArgs
      match (← getConstInfo fnName) with
      | .ctorInfo info =>
        for i in [:min info.numParams args.size] do
          let xs ← collectUnmatchableProperSubterms args[i]!
          out := out ++ xs
      | _ => pure ()
      for arg in args do
        out := out ++ (← collectCtorParamApps arg)
    else
      match e with
      | .lam _ ty body _ | .forallE _ ty body _ =>
        out := out ++ (← collectCtorParamApps ty)
        out := out ++ (← collectCtorParamApps body)
      | .letE _ ty val body _ =>
        out := out ++ (← collectCtorParamApps ty)
        out := out ++ (← collectCtorParamApps val)
        out := out ++ (← collectCtorParamApps body)
      | .mdata _ body | .proj _ _ body =>
        out := out ++ (← collectCtorParamApps body)
      | _ => pure ()
    pure out
  let ctorParamApps ← collectCtorParamApps conclusion
  for e in funcAppExprs do
    let inCtorParam := ctorParamApps.any (fun x => x == e)
    logInfo m!"V130_ROLE candidate={e} ctor_fixed_parameter={inCtorParam}"
  trace[plausible.deriving.arbitrary] m!"Unmatchable exprs: {funcAppExprs} In conclusion: {conclusion}"
'''
if old not in text:
    raise SystemExit("V130 instrumentation anchor not found")
if text.count(old) != 1:
    raise SystemExit(f"V130 instrumentation anchor count != 1: {text.count(old)}")
path.write_text(text.replace(old,new,1))
