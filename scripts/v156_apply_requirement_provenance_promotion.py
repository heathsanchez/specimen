from pathlib import Path

# V156 REQUIREMENT_PROVENANCE_PROMOTION
# Preserve origin at the existing MExp requirement creation sites and promote
# only unconstrained producer requirements into outer+inner prerequisites.

mexp_path = Path("Specimen/MExp.lean")
mexp = mexp_path.read_text()

old_state = '''/-- `CompileScheduleM` is a monad for compiling `Schedule`s to `TSyntax term`s.
    Under the hood, this is just a `State` monad stacked on top of `TermElabM`,
    where the state is an `Array` of `TSyntax term`s, representing any auxiliary typeclass
    instances that need to derived beforehand.  -/
abbrev CompileScheduleM (α : Type) := StateT (TSyntaxArray `term) TermElabM α
'''
new_state = '''/-- Provenance of a typeclass requirement discovered while compiling a schedule. -/
inductive RequirementOrigin where
  | unconstrained
  | constrained
  deriving Repr, BEq

/-- A discovered typeclass requirement together with the producer form that created it. -/
structure RequiredInstance where
  term : TSyntax `term
  origin : RequirementOrigin

/-- `CompileScheduleM` is a monad for compiling `Schedule`s to `TSyntax term`s.
    Its state preserves requirement provenance instead of flattening all discovered
    requirements into an indistinguishable syntax array. -/
abbrev CompileScheduleM (α : Type) := StateT (Array RequiredInstance) TermElabM α
'''
if mexp.count(old_state) != 1:
    raise SystemExit(f"V156 CompileScheduleM anchor count != 1: {mexp.count(old_state)}")
mexp = mexp.replace(old_state, new_state, 1)

old_uncon = '''    (producerMExp, instances.push typeClassInstance)
'''
new_uncon = '''    (producerMExp, instances.push { term := typeClassInstance, origin := .unconstrained })
'''
if mexp.count(old_uncon) != 1:
    raise SystemExit(f"V156 unconstrained push anchor count != 1: {mexp.count(old_uncon)}")
mexp = mexp.replace(old_uncon, new_uncon, 1)

old_con = '''        (producerMExp, instances.push typeClassInstance)
'''
new_con = '''        (producerMExp, instances.push { term := typeClassInstance, origin := .constrained })
'''
if mexp.count(old_con) != 1:
    raise SystemExit(f"V156 constrained push anchor count != 1: {mexp.count(old_con)}")
mexp = mexp.replace(old_con, new_con, 1)
mexp_path.write_text(mexp)

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
new_quote = '''    -- V156: promote only provenance-approved requirements into both scopes.
    let requiredOuterBinderSyntax ← requiredInstances.mapIdxM fun i requiredInstance => do
      let binderName := mkIdent (Name.mkSimple s!"k6_required_outer_{i}")
      `(Lean.Elab.Deriving.instBinderF| [$binderName : $requiredInstance])
    let requiredInnerBinderSyntax ← requiredInstances.mapIdxM fun i requiredInstance => do
      let binderName := mkIdent (Name.mkSimple s!"k6_required_inner_{i}")
      `(Lean.Elab.Deriving.instBinderF| [$binderName : $requiredInstance])
    let requiredOuterBinders : TSyntaxArray `Lean.Parser.Term.bracketedBinder := TSyntaxArray.mk requiredOuterBinderSyntax
    let requiredInnerBinders : TSyntaxArray `Lean.Parser.Term.bracketedBinder := TSyntaxArray.mk requiredInnerBinderSyntax
    `(instance $requiredOuterBinders:bracketedBinder* $arbitraryTypeParamInstances:bracketedBinder* : $producerTypeClass $targetTypeSyntax (fun $targetVarPattern => @$(mkIdent inductiveName) $args*) where
        $producerTypeClassFunction:ident :=
          let rec $innerFunctionIdent:ident $innerParams* $requiredInnerBinders:bracketedBinder* $arbitraryTypeParamInstances:bracketedBinder* : $optionTProducerType :=
            $matchExpr
          fun $freshSizeIdent => $innerFunctionIdent $fuelLit $freshSizeIdent $freshSizeIdent $outerParams*)
'''
if emit.count(old_quote) != 1:
    raise SystemExit(f"V156 emitter quote anchor count != 1: {emit.count(old_quote)}")
emit = emit.replace(old_quote, new_quote, 1)
emit_path.write_text(emit)

src_path = Path("Specimen/DeriveConstrainedProducer.lean")
src = src_path.read_text()

# Existing advisory trace in the standalone path must keep showing terms, not records.
old_trace = '''      if (not requiredInstances.isEmpty) then
        let deduplicatedInstances := List.eraseDups requiredInstances.toList
        trace[plausible.deriving.arbitrary]  m!"Required typeclass instances (please derive these first if they aren't already defined):\\n{deduplicatedInstances}"
'''
new_trace = '''      if (not requiredInstances.isEmpty) then
        let deduplicatedInstances := List.eraseDups (requiredInstances.toList.map (·.term))
        trace[plausible.deriving.arbitrary]  m!"Required typeclass instances (please derive these first if they aren't already defined):\\n{deduplicatedInstances}"
'''
if src.count(old_trace) != 1:
    raise SystemExit(f"V156 standalone trace anchor count != 1: {src.count(old_trace)}")
src = src.replace(old_trace, new_trace, 1)

# Existing diagnostic trace in the parts path likewise prints only the original terms.
old_parts_trace = '''          if !requiredInsts.isEmpty then
            let outputIdxsStr := outputNamesTypesIndices.map (fun (n, _, i) => s!"{n}@{i}")
            trace[plausible.deriving.arbitrary] m!"[{repr deriveSort}] {inductiveName} (outputs: {outputIdxsStr}) constructor {ctorName} requires: {requiredInsts}"
'''
new_parts_trace = '''          if !requiredInsts.isEmpty then
            let outputIdxsStr := outputNamesTypesIndices.map (fun (n, _, i) => s!"{n}@{i}")
            let requiredInstTerms := requiredInsts.map (·.term)
            trace[plausible.deriving.arbitrary] m!"[{repr deriveSort}] {inductiveName} (outputs: {outputIdxsStr}) constructor {ctorName} requires: {requiredInstTerms}"
'''
if src.count(old_parts_trace) != 1:
    raise SystemExit(f"V156 parts trace anchor count != 1: {src.count(old_parts_trace)}")
src = src.replace(old_parts_trace, new_parts_trace, 1)

old_tuple = '''  let (baseProducers, inductiveProducers, freshenedOutputNames, freshArgIdents, localCtx) ←
'''
new_tuple = '''  let (baseProducers, inductiveProducers, freshenedOutputNames, freshArgIdents, localCtx, promotableInstances) ←
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
new_return = '''      let unconstrainedTerms := requiredInstances.toList.filterMap fun req =>
        if req.origin == .unconstrained then some req.term else none
      let promotableInstances := (List.eraseDups unconstrainedTerms).toArray
      return (baseProducers, inductiveProducers, freshenedOutputNames, Lean.mkIdent <$> freshUnknowns, localCtx, promotableInstances))

  -- Promote only requirements whose provenance is an unconstrained producer.
  mkConstrainedProducerTypeClassInstance baseProducers inductiveProducers
    constrainingInductive inductiveLevels freshArgIdents freshenedOutputNames.toList
    outputTypes.toList producerSort localCtx promotableInstances
'''
if src.count(old_return) != 1:
    raise SystemExit(f"V156 producer return anchor count != 1: {src.count(old_return)}")
src = src.replace(old_return, new_return, 1)
src_path.write_text(src)

combined = mexp_path.read_text() + emit_path.read_text() + src_path.read_text()
for forbidden in ("V153P", "V153Q", "V156Pair", "Cedar", "MyRel", "InstanceParameterTest", "MutuallyRecursiveRelationsTest"):
    if forbidden in combined:
        raise SystemExit(f"fixture/domain token leaked into V156 implementation: {forbidden}")
for forbidden_filter in ("toString.contains", "String.contains", "ArbitrarySizedSuchThat`", "EnumSizedSuchThat`"):
    if forbidden_filter in combined:
        raise SystemExit(f"syntactic filtering leaked into V156 implementation: {forbidden_filter}")

print("REQUIREMENT_PROVENANCE_PROMOTION_APPLIED")
