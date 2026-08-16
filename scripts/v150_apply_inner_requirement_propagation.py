from pathlib import Path

# V150 refinement is intentionally narrow. V148 has already threaded the exact
# singleton dependent requirement into the generated outer instance. This patch
# makes that same already-discovered requirement an instance binder of the inner
# producer function so the generated body can synthesize it while elaborating.

path = Path("Specimen/MakeConstrainedProducerInstance.lean")
src = path.read_text()

old = '''    | [requiredInstance] =>
      `(instance [k6_required : $requiredInstance] $arbitraryTypeParamInstances:bracketedBinder* : $producerTypeClass $targetTypeSyntax (fun $targetVarPattern => @$(mkIdent inductiveName) $args*) where
          $producerTypeClassFunction:ident :=
            let rec $innerFunctionIdent:ident $innerParams* $arbitraryTypeParamInstances:bracketedBinder* : $optionTProducerType :=
              $matchExpr
            fun $freshSizeIdent => $innerFunctionIdent $fuelLit $freshSizeIdent $freshSizeIdent $outerParams*)
'''
new = '''    | [requiredInstance] =>
      `(instance [k6_required : $requiredInstance] $arbitraryTypeParamInstances:bracketedBinder* : $producerTypeClass $targetTypeSyntax (fun $targetVarPattern => @$(mkIdent inductiveName) $args*) where
          $producerTypeClassFunction:ident :=
            let rec $innerFunctionIdent:ident $innerParams* [k6_required_inner : $requiredInstance] $arbitraryTypeParamInstances:bracketedBinder* : $optionTProducerType :=
              $matchExpr
            fun $freshSizeIdent => $innerFunctionIdent $fuelLit $freshSizeIdent $freshSizeIdent $outerParams*)
'''

if src.count(old) != 1:
    raise SystemExit(f"V150 intended V148 singleton branch anchor count != 1: {src.count(old)}")
src = src.replace(old, new, 1)
path.write_text(src)

combined = Path("Specimen/MakeConstrainedProducerInstance.lean").read_text() + Path("Specimen/DeriveConstrainedProducer.lean").read_text()
for forbidden in ("V150P", "V150Q", "V150P0", "V150Q0"):
    if forbidden in combined:
        raise SystemExit(f"fixture-specific token leaked into V150 implementation: {forbidden}")

print("K6_INNER_REQUIREMENT_PROPAGATION_APPLIED")
