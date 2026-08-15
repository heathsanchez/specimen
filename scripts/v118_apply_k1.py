#!/usr/bin/env python3
from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()
old = '''    let (ctorName, args) := e.getAppFnArgs
    let mut actualArgs := #[]
    for arg in args do
'''
new = '''    let (ctorName, args) := e.getAppFnArgs
    -- V118 K1: constructor metadata distinguishes uniform inductive parameters
    -- from genuine constructor/index arguments. Uniform parameters are already
    -- supplied by the expected family context and must not be re-emitted as
    -- ordinary explicit constructor arguments.
    let ctorArgs ←
      match (← getConstInfo ctorName) with
      | .ctorInfo info => pure <| args.extract info.numParams args.size
      | _ => pure args
    let mut actualArgs := #[]
    for arg in ctorArgs do
'''
if text.count(old) != 1:
    raise SystemExit(f"expected exactly one patch site, found {text.count(old)}")
path.write_text(text.replace(old, new))
print("V118 K1 applied: drop metadata-declared uniform constructor parameters before ConstructorExpr emission")
