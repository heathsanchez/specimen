from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()
old = '''    let (ctorName, args) := e.getAppFnArgs
    let mut actualArgs := #[]
    for arg in args do
'''
new = '''    let (ctorName, args) := e.getAppFnArgs
    -- V120 CARRY_IMPLICIT_FIXED_PARAMETER: distinguish a uniform parameter
    -- carried implicitly by the inductive family from a genuinely explicit
    -- constructor/index argument.  `numParams` alone is insufficient: V119
    -- repaired the implicit arm but regressed the matched explicit control.
    let (fixedParamCount, fixedParamBinderInfos) ←
      match (← getConstInfo ctorName) with
      | .ctorInfo info =>
        let rec collectBinderInfos (ty : Expr) (n : Nat) : List BinderInfo :=
          if n = 0 then []
          else
            match ty with
            | .forallE _ _ body bi => bi :: collectBinderInfos body (n - 1)
            | _ => []
        pure (info.numParams, collectBinderInfos info.type info.numParams)
      | _ => pure (0, [])
    let mut actualArgs := #[]
    for i in [:args.size] do
      let arg := args[i]!
      let dropImplicitFixedParam :=
        if i < fixedParamCount then
          match fixedParamBinderInfos[i]? with
          | some .implicit | some .strictImplicit | some .instImplicit => true
          | _ => false
        else false
      if dropImplicitFixedParam then
        continue
'''
if old not in text:
    raise SystemExit("V120 patch anchor not found")
if text.count(old) != 1:
    raise SystemExit(f"V120 patch anchor count != 1: {text.count(old)}")
path.write_text(text.replace(old, new, 1))
