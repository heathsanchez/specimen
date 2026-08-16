from pathlib import Path

# V156 is additive and opt-in. The legacy derive_generator path keeps the old
# default (no discovered dependent requirements threaded into emitted code).
# The new command enables the already-computed singleton requirement in both
# the outer generated instance and inner producer function.

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
    raise SystemExit(f"V156 emitter signature anchor count != 1: {emit.count(old_sig)}")
emit = emit.replace(old_sig, new_sig, 1)

old_quote = '''    -- Produce an instance of the appropriate typeclass containing the definition for the derived producer
    `(instance $arbitraryTypeParamInstances:bracketedBinder* : $producerTypeClass $targetTypeSyntax (fun $targetVarPattern => @$(mkIdent inductiveName) $args*) where
        $producerTypeClassFunction:ident :=
          let rec $innerFunctionIdent:ident $innerParams* $arbitraryTypeParamInstances:bracketedBinder* : $optionTProducerType :=
            $matchExpr
          fun $freshSizeIdent => $innerFunctionIdent $fuelLit $freshSizeIdent $freshSizeIdent $outerParams*)
'''
new_quote = '''    -- V156 opt-in requirement-aware assembly. Empty requirements are exactly
    -- legacy behavior. The bounded admitted candidate supports one discovered
    -- dependent premise; wider arity requires a separate experiment.
    match requiredInstances.toList with
    | [] =>
      `(instance $arbitraryTypeParamInstances:bracketedBinder* : $producerTypeClass $targetTypeSyntax (fun $targetVarPattern => @$(mkIdent inductiveName) $args*) where
          $producerTypeClassFunction:ident :=
            let rec $innerFunctionIdent:ident $innerParams* $arbitraryTypeParamInstances:bracketedBinder* : $optionTProducerType :=
              $matchExpr
            fun $freshSizeIdent => $innerFunctionIdent $fuelLit $freshSizeIdent $freshSizeIdent $outerParams*)
    | [requiredInstance] =>
      `(instance [v156_required : $requiredInstance] $arbitraryTypeParamInstances:bracketedBinder* : $producerTypeClass $targetTypeSyntax (fun $targetVarPattern => @$(mkIdent inductiveName) $args*) where
          $producerTypeClassFunction:ident :=
            let rec $innerFunctionIdent:ident $innerParams* [v156_required_inner : $requiredInstance] $arbitraryTypeParamInstances:bracketedBinder* : $optionTProducerType :=
              $matchExpr
            fun $freshSizeIdent => $innerFunctionIdent $fuelLit $freshSizeIdent $freshSizeIdent $outerParams*)
    | _ => throwError m!"requirement-aware deriver currently supports one independent dependent requirement; discovered {requiredInstances.size}"
'''
if emit.count(old_quote) != 1:
    raise SystemExit(f"V156 emitter quote anchor count != 1: {emit.count(old_quote)}")
emit = emit.replace(old_quote, new_quote, 1)
emit_path.write_text(emit)

src_path = Path("Specimen/DeriveConstrainedProducer.lean")
src = src_path.read_text()

old_sig2 = '''def deriveConstrainedProducer
  (_args : Array Expr)
  (outputVars : Array Expr)
  (outputTypes : Array Expr)
  (constrainingInductive : Name)
  (inductiveLevels : List Level)
  (constrArgs : Array Expr)
  (deriveSort : DeriveSort) : TermElabM (TSyntax `command) := do
'''
new_sig2 = '''def deriveConstrainedProducer
  (_args : Array Expr)
  (outputVars : Array Expr)
  (outputTypes : Array Expr)
  (constrainingInductive : Name)
  (inductiveLevels : List Level)
  (constrArgs : Array Expr)
  (deriveSort : DeriveSort)
  (threadRequirements : Bool := false) : TermElabM (TSyntax `command) := do
'''
if src.count(old_sig2) != 1:
    raise SystemExit(f"V156 producer signature anchor count != 1: {src.count(old_sig2)}")
src = src.replace(old_sig2, new_sig2, 1)

old_tuple = '''  let (baseProducers, inductiveProducers, freshenedOutputNames, freshArgIdents, localCtx) ←
'''
new_tuple = '''  let (baseProducers, inductiveProducers, freshenedOutputNames, freshArgIdents, localCtx, requiredInstances) ←
'''
if src.count(old_tuple) < 1:
    raise SystemExit("V156 producer tuple anchor not found")
src = src.replace(old_tuple, new_tuple, 1)

old_return = '''      return (baseProducers, inductiveProducers, freshenedOutputNames, Lean.mkIdent <$> freshUnknowns, localCtx))

  -- Create an instance of the appropriate producer typeclass
  mkConstrainedProducerTypeClassInstance baseProducers inductiveProducers
    constrainingInductive inductiveLevels freshArgIdents freshenedOutputNames.toList
    outputTypes.toList producerSort localCtx
'''
new_return = '''      let discoveredRequiredInstances := (List.eraseDups requiredInstances.toList).toArray
      return (baseProducers, inductiveProducers, freshenedOutputNames, Lean.mkIdent <$> freshUnknowns, localCtx, discoveredRequiredInstances))

  let activeRequiredInstances ←
    if threadRequirements then
      match requiredInstances.toList with
      | [] => pure #[]
      | [requiredInstance] => pure #[requiredInstance]
      | _ => throwError m!"requirement-aware deriver currently supports one independent dependent requirement; discovered {requiredInstances.size}"
    else pure #[]

  -- Existing callers receive the old empty-requirement behavior. Only the new
  -- opt-in command passes the discovered premise into assembly.
  mkConstrainedProducerTypeClassInstance baseProducers inductiveProducers
    constrainingInductive inductiveLevels freshArgIdents freshenedOutputNames.toList
    outputTypes.toList producerSort localCtx activeRequiredInstances
'''
if src.count(old_return) != 1:
    raise SystemExit(f"V156 producer return anchor count != 1: {src.count(old_return)}")
src = src.replace(old_return, new_return, 1)

old_public = '''def deriveArbitrarySuchThatInstance (tm : Term) : TermElabM Command := do
  let e ← elabTerm tm .none
  withParsedDerivingArgs e deriveArbitrarySuchThatInstance'
'''
new_public = old_public + '''
private def deriveArbitrarySuchThatInstanceWithRequirements'
  (args : Array Expr)
  (outVars : Array Expr)
  (outTypes : Array Expr)
  (constrainingInductive : Name)
  (inductiveLevels : List Level)
  (constrArgs : Array Expr) : TermElabM (TSyntax `command) := do
  deriveConstrainedProducer args outVars outTypes constrainingInductive inductiveLevels constrArgs
    (deriveSort := .Generator) (threadRequirements := true)

def deriveArbitrarySuchThatInstanceWithRequirements (tm : Term) : TermElabM Command := do
  let e ← elabTerm tm .none
  withParsedDerivingArgs e deriveArbitrarySuchThatInstanceWithRequirements'
'''
if src.count(old_public) != 1:
    raise SystemExit(f"V156 public wrapper anchor count != 1: {src.count(old_public)}")
src = src.replace(old_public, new_public, 1)

anchor = '''/-- Command for deriving a constrained generator with multi-output hypothesis steps -/
syntax (name := generator_multi_deriver) "derive_generator_multi" term : command
'''
new_command = '''/-- Opt-in constrained-generator deriver that retains the singleton dependent
    typeclass requirement already discovered during MExp compilation. -/
syntax (name := generator_requirement_deriver) "derive_generator_with_requirements" term : command

@[command_elab generator_requirement_deriver]
def elabDeriveGeneratorWithRequirements : CommandElab := fun stx => do
  match stx with
  | `(derive_generator_with_requirements $descr:term) => do
    let typeClassInstance ← liftTermElabM <| deriveArbitrarySuchThatInstanceWithRequirements descr
    let genFormat ← liftCoreM (PrettyPrinter.ppCommand typeClassInstance)
    liftTermElabM $ Tactic.TryThis.addSuggestion stx
      (Format.pretty genFormat) (header := "Try this requirement-aware generator: ")
    elabCommand typeClassInstance
  | _ => throwUnsupportedSyntax

''' + anchor
if src.count(anchor) != 1:
    raise SystemExit(f"V156 command anchor count != 1: {src.count(anchor)}")
src = src.replace(anchor, new_command, 1)
src_path.write_text(src)

combined = emit_path.read_text() + src_path.read_text()
for forbidden in ("V156P", "V156Q", "V156P0", "V156Q0", "Unit", "Bool", "Meta", "Carrier"):
    # Unit/Bool/field names are forbidden only in newly introduced source text;
    # existing project source may already contain these generic Lean names.
    if forbidden.startswith("V156") and forbidden in combined:
        raise SystemExit(f"fixture-specific token leaked into V156 implementation: {forbidden}")

print("V156_REQUIREMENT_AWARE_DERIVER_APPLIED")
