from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
src = path.read_text()

# Remove standalone construction of an output type from the original existential
# telescope. It will be reconstructed after fresh inductive arguments exist.
old_outer = '''  -- The output type for code generation — for multiple outputs, use a right-nested product type
  -- Build the output product type (e.g., α × β for two outputs)
  let outputType ← tupleOfListM (throwError "no output types")
    (fun t rest => do
      let u ← Meta.mkFreshLevelMVar
      let v ← Meta.mkFreshLevelMVar
      pure (Lean.mkApp2 (Lean.mkConst ``Prod [u, v]) t rest)) outputTypes.toList

'''
new_outer = '''  -- V164: output types are reconstructed below from fresh inductive arguments.
  -- The original existential telescope may contain stale term-level structure fvars.

'''
if src.count(old_outer) != 1:
    raise SystemExit(f"V164 outer outputType anchor count != 1: {src.count(old_outer)}")
src = src.replace(old_outer, new_outer, 1)

old_open = '''  let (baseProducers, inductiveProducers, freshenedOutputNames, freshArgIdents, localCtx) ←
  -- Freshen argument names to avoid capture, then derive schedules per constructor
    withLocalDeclsDND argNamesTypes (fun _ => do
      let mut localCtx ← getLCtx
      let mut freshUnknowns := #[]
'''
new_open = '''  let (baseProducers, inductiveProducers, freshenedOutputNames, freshArgIdents, localCtx, liveOutputTypes) ←
  -- Freshen argument names to avoid capture, then derive schedules per constructor
    withLocalDeclsDND argNamesTypes (fun allFVars => do
      let mut localCtx ← getLCtx
      let mut freshUnknowns := #[]
'''
if src.count(old_open) != 1:
    raise SystemExit(f"V164 standalone context anchor count != 1: {src.count(old_open)}")
src = src.replace(old_open, new_open, 1)

old_after_outputs = '''      -- Since the outputs also appear as arguments to the inductive relation,
      -- we also need to freshen their names
      let freshenedOutputNames := outputIdxs.map (fun idx => freshUnknowns[idx]!)

      -- Each argument to the inductive relation (except those at output indices)
'''
new_after_outputs = '''      -- Since the outputs also appear as arguments to the inductive relation,
      -- we also need to freshen their names
      let freshenedOutputNames := outputIdxs.map (fun idx => freshUnknowns[idx]!)

      -- V164 LIVE_OUTPUT_TYPE_RECONSTRUCTION: infer each argument type by
      -- sequentially applying the inductive to the fresh fvars. This rebases
      -- dependent types such as `Option p.A` onto the live `p` fvar.
      let liveArgTypes ← getCorrectTypes allFVars inductiveName inductiveLevels
      let liveOutputTypes := outputIdxs.filterMap (fun idx => liveArgTypes[idx]?)
      let outputType ← tupleOfListM (throwError "no live output types")
        (fun t rest => do
          let u ← Meta.mkFreshLevelMVar
          let v ← Meta.mkFreshLevelMVar
          pure (Lean.mkApp2 (Lean.mkConst ``Prod [u, v]) t rest)) liveOutputTypes.toList

      -- Each argument to the inductive relation (except those at output indices)
'''
if src.count(old_after_outputs) != 1:
    raise SystemExit(f"V164 fresh-output anchor count != 1: {src.count(old_after_outputs)}")
src = src.replace(old_after_outputs, new_after_outputs, 1)

old_triples = '''      let outputNamesTypesIndices : List (Name × Expr × Nat) :=
        (List.range outputIdxs.size).map (fun i =>
          (freshenedOutputNames[i]!, outputTypes[i]!, outputIdxs[i]!))
'''
new_triples = '''      let outputNamesTypesIndices : List (Name × Expr × Nat) :=
        (List.range outputIdxs.size).map (fun i =>
          (freshenedOutputNames[i]!, liveOutputTypes[i]!, outputIdxs[i]!))
'''
if src.count(old_triples) != 2:
    # One standalone and one parts path are expected in this repository; patch only first.
    raise SystemExit(f"V164 output triple anchor count != 2: {src.count(old_triples)}")
src = src.replace(old_triples, new_triples, 1)

old_return = '''      return (baseProducers, inductiveProducers, freshenedOutputNames, Lean.mkIdent <$> freshUnknowns, localCtx))

  -- Create an instance of the appropriate producer typeclass
  mkConstrainedProducerTypeClassInstance baseProducers inductiveProducers
    constrainingInductive inductiveLevels freshArgIdents freshenedOutputNames.toList
    outputTypes.toList producerSort localCtx
'''
new_return = '''      return (baseProducers, inductiveProducers, freshenedOutputNames, Lean.mkIdent <$> freshUnknowns, localCtx, liveOutputTypes))

  -- Create an instance using the output types rebased onto the live standalone context.
  mkConstrainedProducerTypeClassInstance baseProducers inductiveProducers
    constrainingInductive inductiveLevels freshArgIdents freshenedOutputNames.toList
    liveOutputTypes.toList producerSort localCtx
'''
if src.count(old_return) != 1:
    raise SystemExit(f"V164 standalone return anchor count != 1: {src.count(old_return)}")
src = src.replace(old_return, new_return, 1)

path.write_text(src)

for forbidden in ("V161P0", "V161P1", "V159SchemaS"):
    if forbidden in src:
        raise SystemExit(f"fixture token leaked into V164 core: {forbidden}")

print("V164_LIVE_OUTPUT_TYPE_RECONSTRUCTION_APPLIED")
