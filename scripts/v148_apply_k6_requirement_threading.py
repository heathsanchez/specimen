from pathlib import Path

# K6 is deliberately generic: thread already-discovered required typeclass
# premises into the generated constrained-producer instance.  No fixture names
# or concrete types occur in this intervention.

emit_path = Path("Specimen/MakeConstrainedProducerInstance.lean")
emit = emit_path.read_text()

old_sig = '''  (targetTypes : List Expr)
  (producerSort : ProducerSort)
  (topLevelLocalCtx : LocalContext) : TermElabM (TSyntax `command) := do
'''
new_sig = '''  (targetTypes : List Expr)
  (producerSort : ProducerSort)
  (topLevelLocalCtx : LocalContext)
  (requiredInstances : TSyntaxArray `term := #[]) : TermElabM (TSyntax `command) := do
'''
if emit.count(old_sig) != 1:
    raise SystemExit(f"K6 emitter signature anchor count != 1: {emit.count(old_sig)}")
emit = emit.replace(old_sig, new_sig, 1)

old_binders = '''    let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[producerUnconstrainedClass, ``DecidableEq]

    let fuelVal := Lean.Option.get (← getOptions) specimen.fuel
'''
new_binders = '''    let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[producerUnconstrainedClass, ``DecidableEq]

    -- V148 K6_DEPENDENT_REQUIREMENT_THREADING:
    -- schedule compilation already records every unconstrained typeclass premise
    -- it needs.  Preserve those premises in the generated producer's context
    -- instead of merely tracing them and elaborating the body without them.
    let requiredInstanceBinders : TSyntaxArray `Lean.Parser.Term.bracketedBinder ←
      requiredInstances.mapM fun inst =>
        `(Lean.Parser.Term.bracketedBinder| [$inst])

    let fuelVal := Lean.Option.get (← getOptions) specimen.fuel
'''
if emit.count(old_binders) != 1:
    raise SystemExit(f"K6 emitter binder anchor count != 1: {emit.count(old_binders)}")
emit = emit.replace(old_binders, new_binders, 1)

old_quote = '''    `(instance $arbitraryTypeParamInstances:bracketedBinder* : $producerTypeClass $targetTypeSyntax (fun $targetVarPattern => @$(mkIdent inductiveName) $args*) where
        $producerTypeClassFunction:ident :=
          let rec $innerFunctionIdent:ident $innerParams* $arbitraryTypeParamInstances:bracketedBinder* : $optionTProducerType :=
            $matchExpr
          fun $freshSizeIdent => $innerFunctionIdent $fuelLit $freshSizeIdent $freshSizeIdent $outerParams*)
'''
new_quote = '''    `(instance $arbitraryTypeParamInstances:bracketedBinder* $requiredInstanceBinders:bracketedBinder* : $producerTypeClass $targetTypeSyntax (fun $targetVarPattern => @$(mkIdent inductiveName) $args*) where
        $producerTypeClassFunction:ident :=
          let rec $innerFunctionIdent:ident $innerParams* $arbitraryTypeParamInstances:bracketedBinder* $requiredInstanceBinders:bracketedBinder* : $optionTProducerType :=
            $matchExpr
          fun $freshSizeIdent => $innerFunctionIdent $fuelLit $freshSizeIdent $freshSizeIdent $outerParams*)
'''
if emit.count(old_quote) != 1:
    raise SystemExit(f"K6 emitter quote anchor count != 1: {emit.count(old_quote)}")
emit = emit.replace(old_quote, new_quote, 1)
emit_path.write_text(emit)

src_path = Path("Specimen/DeriveConstrainedProducer.lean")
src = src_path.read_text()

old_tuple = '''  let (baseProducers, inductiveProducers, freshenedOutputNames, freshArgIdents, localCtx) ←
'''
new_tuple = '''  let (baseProducers, inductiveProducers, freshenedOutputNames, freshArgIdents, localCtx, requiredInstances) ←
'''
if src.count(old_tuple) < 1:
    raise SystemExit("K6 producer tuple anchor not found")
# The first occurrence is deriveConstrainedProducer; later similar functions are
# intentionally left unchanged for this smallest candidate.
src = src.replace(old_tuple, new_tuple, 1)

old_return = '''      return (baseProducers, inductiveProducers, freshenedOutputNames, Lean.mkIdent <$> freshUnknowns, localCtx))

  -- Create an instance of the appropriate producer typeclass
  mkConstrainedProducerTypeClassInstance baseProducers inductiveProducers
    constrainingInductive inductiveLevels freshArgIdents freshenedOutputNames.toList
    outputTypes.toList producerSort localCtx
'''
new_return = '''      let threadedRequiredInstances := (List.eraseDups requiredInstances.toList).toArray
      return (baseProducers, inductiveProducers, freshenedOutputNames, Lean.mkIdent <$> freshUnknowns, localCtx, threadedRequiredInstances))

  -- Create an instance of the appropriate producer typeclass, retaining the
  -- exact dependent premises discovered during schedule compilation.
  mkConstrainedProducerTypeClassInstance baseProducers inductiveProducers
    constrainingInductive inductiveLevels freshArgIdents freshenedOutputNames.toList
    outputTypes.toList producerSort localCtx requiredInstances
'''
if src.count(old_return) != 1:
    raise SystemExit(f"K6 producer return anchor count != 1: {src.count(old_return)}")
src = src.replace(old_return, new_return, 1)
src_path.write_text(src)

# Static anti-special-case audit.
combined = emit_path.read_text() + src_path.read_text()
for forbidden in ("V148P", "V148Q", "V148P0", "V148Q0"):
    if forbidden in combined:
        raise SystemExit(f"fixture-specific token leaked into K6 implementation: {forbidden}")

print("K6_DEPENDENT_REQUIREMENT_THREADING_APPLIED")
