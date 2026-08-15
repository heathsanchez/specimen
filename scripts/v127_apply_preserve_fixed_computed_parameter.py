from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()

old_sig = '''def linearizeAndFlatten
  (hypotheses : Array Expr) (conclusion : Expr) (outputIndices : List Nat) (localCtx : LocalContext) :
  UnifyM (Array Expr × Expr × List (Name × Expr) × LocalContext) := do
  -- Phase 1: flatten function calls into fresh unknowns with equality hypotheses
  let funcAppExprs ← collectUnmatchableProperSubterms conclusion
'''

new_sig = '''def linearizeAndFlatten
  (hypotheses : Array Expr) (conclusion : Expr) (outputIndices : List Nat)
  (inputNames : List Name) (localCtx : LocalContext) :
  UnifyM (Array Expr × Expr × List (Name × Expr) × LocalContext) := do
  -- Phase 1: flatten function calls into fresh unknowns with equality hypotheses.
  -- V127 PRESERVE_FIXED_COMPUTED_PARAMETER: if a proper function application
  -- depends only on already-fixed top-level inputs, it is a deterministic
  -- carried parameter rather than a new value to discover.  Preserve it
  -- symbolically through conclusion unification instead of manufacturing a
  -- fresh output plus an equality producer obligation.
  let candidateFuncAppExprs ← collectUnmatchableProperSubterms conclusion
  let rec allFVarsAreFixedInputs (e : Expr) : MetaM Bool := do
    match e with
    | .fvar id =>
      let decl ← id.getDecl
      pure (decl.userName ∈ inputNames)
    | .app f a =>
      pure ((← allFVarsAreFixedInputs f) && (← allFVarsAreFixedInputs a))
    | .lam _ ty body _ | .forallE _ ty body _ =>
      pure ((← allFVarsAreFixedInputs ty) && (← allFVarsAreFixedInputs body))
    | .letE _ ty val body _ =>
      pure ((← allFVarsAreFixedInputs ty) &&
            (← allFVarsAreFixedInputs val) &&
            (← allFVarsAreFixedInputs body))
    | .mdata _ body => allFVarsAreFixedInputs body
    | .proj _ _ body => allFVarsAreFixedInputs body
    | _ => pure true
  let mut funcAppExprs := []
  for e in candidateFuncAppExprs do
    if !(← allFVarsAreFixedInputs e) then
      funcAppExprs := funcAppExprs ++ [e]
'''

if old_sig not in text:
    raise SystemExit("V127 signature/phase anchor not found")
if text.count(old_sig) != 1:
    raise SystemExit(f"V127 signature/phase anchor count != 1: {text.count(old_sig)}")
text = text.replace(old_sig, new_sig, 1)

old_call = '''      linearizeAndFlatten hypotheses conclusion outputIndices (← getLCtx)
'''
new_call = '''      linearizeAndFlatten hypotheses conclusion outputIndices inputNames (← getLCtx)
'''
if old_call not in text:
    raise SystemExit("V127 call anchor not found")
if text.count(old_call) != 1:
    raise SystemExit(f"V127 call anchor count != 1: {text.count(old_call)}")
text = text.replace(old_call, new_call, 1)

path.write_text(text)
