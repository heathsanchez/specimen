from pathlib import Path

# V162 is a strict delta on top of V156. The workflow must apply
# scripts/v156_apply_requirement_aware_deriver.py first. This patch changes only
# singleton arity -> the already-discovered deduplicated finite requirement set.

emit_path = Path("Specimen/MakeConstrainedProducerInstance.lean")
emit = emit_path.read_text()

old = '''    -- V156 opt-in requirement-aware assembly. Empty requirements are exactly
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

new = '''    -- V162 FINITE_REQUIREMENT_THREADING: V156 already computed and
    -- deduplicated the exact requirement array. Convert that array directly to
    -- unnamed instance binders for both the outer instance and inner producer.
    -- Empty arrays reproduce legacy assembly; singleton arrays reproduce V156.
    let finiteRequiredBinders ← requiredInstances.mapM fun req =>
      `(Lean.Elab.Deriving.instBinderF| [$req])
    `(instance $finiteRequiredBinders:bracketedBinder* $arbitraryTypeParamInstances:bracketedBinder* : $producerTypeClass $targetTypeSyntax (fun $targetVarPattern => @$(mkIdent inductiveName) $args*) where
        $producerTypeClassFunction:ident :=
          let rec $innerFunctionIdent:ident $innerParams* $finiteRequiredBinders:bracketedBinder* $arbitraryTypeParamInstances:bracketedBinder* : $optionTProducerType :=
            $matchExpr
          fun $freshSizeIdent => $innerFunctionIdent $fuelLit $freshSizeIdent $freshSizeIdent $outerParams*)
'''
if emit.count(old) != 1:
    raise SystemExit(f"V162 V156 emitter anchor count != 1: {emit.count(old)}")
emit = emit.replace(old, new, 1)
emit_path.write_text(emit)

src_path = Path("Specimen/DeriveConstrainedProducer.lean")
src = src_path.read_text()
old_guard = '''  let activeRequiredInstances ←
    if threadRequirements then
      match requiredInstances.toList with
      | [] => pure #[]
      | [requiredInstance] => pure #[requiredInstance]
      | _ => throwError m!"requirement-aware deriver currently supports one independent dependent requirement; discovered {requiredInstances.size}"
    else pure #[]
'''
new_guard = '''  let activeRequiredInstances ←
    if threadRequirements then
      pure requiredInstances
    else pure #[]
'''
if src.count(old_guard) != 1:
    raise SystemExit(f"V162 V156 arity-guard anchor count != 1: {src.count(old_guard)}")
src = src.replace(old_guard, new_guard, 1)
src_path.write_text(src)

combined = emit_path.read_text() + src_path.read_text()
for forbidden in ("V162P", "V162Q", "V162R", "TwoLeaf", "ThreeLeaf"):
    if forbidden in combined:
        raise SystemExit(f"fixture-specific token leaked into V162 implementation: {forbidden}")

print("V162_FINITE_REQUIREMENT_THREADING_APPLIED")
