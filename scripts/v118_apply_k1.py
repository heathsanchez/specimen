#!/usr/bin/env python3
from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()
old = '''    let (ctorName, args) := e.getAppFnArgs
    let mut actualArgs := #[]
    for arg in args do
'''
new = '''    let (ctorName, args) := e.getAppFnArgs
    -- V118 K1b: preserve the binder-role distinction for uniform inductive
    -- parameters. An implicit uniform parameter is supplied by elaboration from
    -- the expected family context and must not be emitted as an ordinary
    -- constructor argument. An explicit uniform parameter remains a genuine
    -- argument and must be preserved.
    let ctorArgs ←
      match (← getConstInfo ctorName) with
      | .ctorInfo info => do
        let mut ctorTy := info.type
        let mut kept := #[]
        for h : i in [:args.size] do
          if i < info.numParams then
            match ctorTy with
            | .forallE _ _ body binderInfo =>
              if binderInfo == .default then
                kept := kept.push args[i]
              ctorTy := body
            | _ =>
              kept := kept.push args[i]
          else
            kept := kept.push args[i]
        pure kept
      | _ => pure args
    let mut actualArgs := #[]
    for arg in ctorArgs do
'''
if text.count(old) != 1:
    raise SystemExit(f"expected exactly one patch site, found {text.count(old)}")
path.write_text(text.replace(old, new))
print("V118 K1b applied: omit only implicit uniform constructor parameters; preserve explicit uniform binders")
