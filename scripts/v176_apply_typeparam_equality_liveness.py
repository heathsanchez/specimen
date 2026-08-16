from pathlib import Path

# V176 — standalone type-parameter equality liveness.
# Closure/composition of existing schedule dependency information + admitted K6.

src_path = Path('Specimen/DeriveConstrainedProducer.lean')
src = src_path.read_text()

# Minimal extractor adapted from the pre-existing fix-polymorphic-dep-constraints line.
helper_anchor = 'def deriveConstrainedProducer\n'
helper = '''/-- V176: collect type-parameter names referenced by a schedule ConstructorExpr. -/\ndef v176ExtractTypeParamRefs (typeParams : Std.HashSet Name) : ConstructorExpr → Std.HashSet Name\n  | .Unknown n => if typeParams.contains n then Std.HashSet.ofList [n] else {}\n  | .Ctor _ args | .TyCtor _ args | .FuncApp _ args =>\n    args.foldl (fun acc a => acc.union (v176ExtractTypeParamRefs typeParams a)) {}\n  | .Lit _ | .CSort _ | .Hole => {}\n\ndef deriveConstrainedProducer\n'''
if src.count(helper_anchor) != 1:
    raise SystemExit(f'V176_HELPER_ANCHOR_COUNT:{src.count(helper_anchor)}')
src = src.replace(helper_anchor, helper, 1)

# Add fresh type-parameter inventory + live equality set after argument freshening.
fresh_anchor = '''      let freshenedOutputNames := outputIdxs.map (fun idx => freshUnknowns[idx]!)\n\n      -- Each argument to the inductive relation (except those at output indices)\n'''
fresh_new = '''      let freshenedOutputNames := outputIdxs.map (fun idx => freshUnknowns[idx]!)\n\n      -- V176: identify freshened Sort-valued type parameters once, before schedule scanning.\n      let mut v176TypeParamNames : Array Name := #[]\n      for i in [:argTypes.size] do\n        if argTypes[i]!.isSort then\n          v176TypeParamNames := v176TypeParamNames.push freshUnknowns[i]!\n      let v176TypeParamSet := Std.HashSet.ofArray v176TypeParamNames\n      let mut v176EqualityLiveTypeParams : Array Name := #[]\n\n      -- Each argument to the inductive relation (except those at output indices)\n'''
if src.count(fresh_anchor) != 1:
    raise SystemExit(f'V176_FRESH_ANCHOR_COUNT:{src.count(fresh_anchor)}')
src = src.replace(fresh_anchor, fresh_new, 1)

# Inspect already-derived schedules only; no search/routing changes.
schedule_anchor = '''        | some result =>\n          let schedule := result.schedule\n          -- Obtain a sub-producer for this constructor, along with an array of all typeclass instances that need to be defined beforehand.\n'''
schedule_new = '''        | some result =>\n          let schedule := result.schedule\n          -- V176: equality liveness comes from existing non-recursive Eq checks.\n          -- This mirrors the pre-existing bottom-up dependency principle: retain\n          -- DecidableEq only for type parameters actually referenced by such checks.\n          let (v176Steps, _) := schedule\n          for step in v176Steps do\n            match step with\n            | .Check (.NonRec (depName, depArgs)) _ =>\n              if depName == ``Eq then\n                let refs := depArgs.foldl\n                  (fun acc a => acc.union (v176ExtractTypeParamRefs v176TypeParamSet a))\n                  ({} : Std.HashSet Name)\n                for tp in v176TypeParamNames do\n                  if refs.contains tp && !v176EqualityLiveTypeParams.contains tp then\n                    v176EqualityLiveTypeParams := v176EqualityLiveTypeParams.push tp\n            | _ => pure ()\n          -- Obtain a sub-producer for this constructor, along with an array of all typeclass instances that need to be defined beforehand.\n'''
if src.count(schedule_anchor) != 1:
    raise SystemExit(f'V176_SCHEDULE_ANCHOR_COUNT:{src.count(schedule_anchor)}')
src = src.replace(schedule_anchor, schedule_new, 1)

# Post-V156/V158 tuple carries K6 promotable requirements. Add equality-live names.
tuple_anchor = '''  let (baseProducers, inductiveProducers, freshenedOutputNames, freshArgIdents, localCtx, promotableInstances) ←\n'''
tuple_new = '''  let (baseProducers, inductiveProducers, freshenedOutputNames, freshArgIdents, localCtx, promotableInstances, v176EqualityLiveTypeParams) ←\n'''
if src.count(tuple_anchor) != 1:
    raise SystemExit(f'V176_TUPLE_ANCHOR_COUNT:{src.count(tuple_anchor)}')
src = src.replace(tuple_anchor, tuple_new, 1)

return_anchor = '''      let promotableInstances := (List.eraseDups unconstrainedTerms).toArray\n      return (baseProducers, inductiveProducers, freshenedOutputNames, Lean.mkIdent <$> freshUnknowns, localCtx, promotableInstances))\n\n  -- Promote only requirements whose provenance is an unconstrained producer.\n  mkConstrainedProducerTypeClassInstance baseProducers inductiveProducers\n    constrainingInductive inductiveLevels freshArgIdents freshenedOutputNames.toList\n    outputTypes.toList producerSort localCtx promotableInstances\n'''
return_new = '''      let promotableInstances := (List.eraseDups unconstrainedTerms).toArray\n      return (baseProducers, inductiveProducers, freshenedOutputNames, Lean.mkIdent <$> freshUnknowns, localCtx, promotableInstances, v176EqualityLiveTypeParams))\n\n  -- K6 supplies actual generation requirements; V176 retains equality capability\n  -- only for type parameters live in existing equality-check schedule steps.\n  mkConstrainedProducerTypeClassInstance baseProducers inductiveProducers\n    constrainingInductive inductiveLevels freshArgIdents freshenedOutputNames.toList\n    outputTypes.toList producerSort localCtx promotableInstances v176EqualityLiveTypeParams\n'''
if src.count(return_anchor) != 1:
    raise SystemExit(f'V176_RETURN_ANCHOR_COUNT:{src.count(return_anchor)}')
src = src.replace(return_anchor, return_new, 1)
src_path.write_text(src)

emit_path = Path('Specimen/MakeConstrainedProducerInstance.lean')
emit = emit_path.read_text()

sig_anchor = '''  (producerSort : ProducerSort)\n  (topLevelLocalCtx : LocalContext)\n  (requiredInstances : TSyntaxArray `term := #[]) : TermElabM (TSyntax `command) := do\n'''
sig_new = '''  (producerSort : ProducerSort)\n  (topLevelLocalCtx : LocalContext)\n  (requiredInstances : TSyntaxArray `term := #[])\n  (equalityLiveTypeParams : Array Name := #[]) : TermElabM (TSyntax `command) := do\n'''
if emit.count(sig_anchor) != 1:
    raise SystemExit(f'V176_EMITTER_SIG_COUNT:{emit.count(sig_anchor)}')
emit = emit.replace(sig_anchor, sig_new, 1)

binder_anchor = '''    let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[producerUnconstrainedClass, ``DecidableEq]\n'''
binder_new = '''    -- V176: no blanket producer/equality constraints. K6 supplies real\n    -- unconstrained-generation premises; only equality-live type params retain DecidableEq.\n    let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders equalityLiveTypeParams #[``DecidableEq]\n'''
if emit.count(binder_anchor) != 1:
    raise SystemExit(f'V176_BINDER_ANCHOR_COUNT:{emit.count(binder_anchor)}')
emit = emit.replace(binder_anchor, binder_new, 1)
emit_path.write_text(emit)

combined = src_path.read_text() + emit_path.read_text()
checks = {
    'extractor': 'def v176ExtractTypeParamRefs' in combined,
    'schedule Eq gate': 'depName == ``Eq' in combined,
    'K6 promotable preserved': 'promotableInstances' in combined,
    'equality live binder': 'equalityLiveTypeParams #[``DecidableEq]' in combined,
}
missing = [k for k,v in checks.items() if not v]
if missing:
    raise SystemExit('V176_POST_APPLY_ASSERTION:' + ','.join(missing))
for forbidden in ['V170Fixed','V176EqLive','NEqGenerator','ISSUE19','Issue19','fixtures/','Bool']:
    if forbidden in combined:
        raise SystemExit(f'V176_TARGET_TOKEN_LEAK:{forbidden}')
print('V176_TYPEPARAM_EQUALITY_LIVENESS_APPLIED')
