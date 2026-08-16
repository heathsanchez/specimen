from pathlib import Path

# V157 MISSING_ONLY_REQUIREMENT_PROMOTION
# Runs after the frozen V156 provenance transform. It adds one semantic bit:
# whether Lean can already synthesize an unconstrained requirement in the exact
# creation-site local context. Only missing unconstrained requirements remain
# promotable.

mexp_path = Path("Specimen/MExp.lean")
mexp = mexp_path.read_text()

old_record = '''structure RequiredInstance where
  term : TSyntax `term
  origin : RequirementOrigin
'''
new_record = '''structure RequiredInstance where
  term : TSyntax `term
  origin : RequirementOrigin
  needsPromotion : Bool
'''
if mexp.count(old_record) != 1:
    raise SystemExit(f"V157 RequiredInstance record anchor count != 1: {mexp.count(old_record)}")
mexp = mexp.replace(old_record, new_record, 1)

old_uncon = '''  let typeClassInstance ← `( $(Lean.mkIdent typeClassName) $ty:term )

  -- Add the `typeClassInstance` for the unconstrained producer to the state,
  -- then obtain the `MExp` representing the unconstrained producer
  StateT.modifyGet $ fun instances =>
    let producerMExp :=
      match prodSort with
      | .Enumerator => .MConst ``Enum.enum
      | .Generator => .MConst ``Arbitrary.arbitrary
    (producerMExp, instances.push { term := typeClassInstance, origin := .unconstrained })
'''
new_uncon = '''  let typeClassInstance ← `( $(Lean.mkIdent typeClassName) $ty:term )

  -- V157: ask Lean itself whether this exact requirement is already available
  -- in the creation-site local context. Existing requirements must not become
  -- new prerequisites merely because a schedule used an unconstrained producer.
  let typeClassType ← Term.elabType typeClassInstance
  let alreadyAvailable ← Meta.withNewMCtxDepth do
    let result ← Meta.synthInstance? typeClassType
    pure result.isSome
  let needsPromotion := !alreadyAvailable

  -- Add the requirement together with provenance and actual availability.
  StateT.modifyGet $ fun instances =>
    let producerMExp :=
      match prodSort with
      | .Enumerator => .MConst ``Enum.enum
      | .Generator => .MConst ``Arbitrary.arbitrary
    (producerMExp, instances.push { term := typeClassInstance, origin := .unconstrained, needsPromotion := needsPromotion })
'''
if mexp.count(old_uncon) != 1:
    raise SystemExit(f"V157 unconstrained availability anchor count != 1: {mexp.count(old_uncon)}")
mexp = mexp.replace(old_uncon, new_uncon, 1)

old_con = '''        (producerMExp, instances.push { term := typeClassInstance, origin := .constrained })
'''
new_con = '''        (producerMExp, instances.push { term := typeClassInstance, origin := .constrained, needsPromotion := false })
'''
if mexp.count(old_con) != 1:
    raise SystemExit(f"V157 constrained record anchor count != 1: {mexp.count(old_con)}")
mexp = mexp.replace(old_con, new_con, 1)
mexp_path.write_text(mexp)

src_path = Path("Specimen/DeriveConstrainedProducer.lean")
src = src_path.read_text()
old_selector = '''      let unconstrainedTerms := requiredInstances.toList.filterMap fun req =>
        if req.origin == .unconstrained then some req.term else none
'''
new_selector = '''      let unconstrainedTerms := requiredInstances.toList.filterMap fun req =>
        if req.origin == .unconstrained && req.needsPromotion then some req.term else none
'''
if src.count(old_selector) != 1:
    raise SystemExit(f"V157 promotion selector anchor count != 1: {src.count(old_selector)}")
src = src.replace(old_selector, new_selector, 1)
src_path.write_text(src)

checks = {
    "availability field": "needsPromotion : Bool" in mexp_path.read_text(),
    "Lean synthesis query": "Meta.synthInstance? typeClassType" in mexp_path.read_text(),
    "unconstrained availability record": "origin := .unconstrained, needsPromotion := needsPromotion" in mexp_path.read_text(),
    "constrained never promoted": "origin := .constrained, needsPromotion := false" in mexp_path.read_text(),
    "missing-only selector": "req.origin == .unconstrained && req.needsPromotion" in src_path.read_text(),
}
missing = [name for name, ok in checks.items() if not ok]
if missing:
    raise SystemExit("V157 post-apply assertion failed: " + ", ".join(missing))

combined = mexp_path.read_text() + src_path.read_text()
for forbidden in ("MemNat", "ScheduleQualityRegressionTest", "V153P", "V153Q", "V156Pair", "Cedar"):
    if forbidden in combined:
        raise SystemExit(f"fixture/domain token leaked into V157 implementation: {forbidden}")

print("MISSING_ONLY_REQUIREMENT_PROMOTION_APPLIED")
