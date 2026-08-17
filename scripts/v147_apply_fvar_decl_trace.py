from pathlib import Path

path = Path("Specimen/Schedules.lean")
text = path.read_text()
old = '''  | .fvar id =>
    let localDecl ← FVarId.getDecl id
    return ConstructorExpr.Unknown localDecl.userName
'''
new = '''  | .fvar id =>
    let localDecl ← FVarId.getDecl id
    -- V147 trace-only discriminator: preserve behavior exactly while exposing
    -- declaration kind/value immediately before name-only IR conversion.
    match localDecl.value? with
    | some value =>
      trace[plausible.deriving.arbitrary] m!"V147_FVAR_DECL name={localDecl.userName}; isLet={localDecl.isLet}; value={value}"
    | none =>
      trace[plausible.deriving.arbitrary] m!"V147_FVAR_DECL name={localDecl.userName}; isLet={localDecl.isLet}; value=NONE"
    return ConstructorExpr.Unknown localDecl.userName
'''
count = text.count(old)
if count != 1:
    raise SystemExit(f"V147 expected exactly one fvar classifier anchor, found {count}")
path.write_text(text.replace(old, new, 1))
print("V147 trace-only fvar declaration probe applied")
