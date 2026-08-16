from pathlib import Path

p = Path('Specimen/MakeConstrainedProducerInstance.lean')
s = p.read_text()

# Source-structural helper only: identify whether a relation type parameter is
# mentioned in one of the generated output type syntaxes.
anchor = '''def mkTypeClassInstanceBinders (typeParams : Array Name) (typeClasses : Array Name) : TermElabM (TSyntaxArray `Lean.Parser.Term.bracketedBinder) := do
  let instances ← typeParams.flatMapM fun param =>
    typeClasses.mapM fun tc =>
      `(Lean.Elab.Deriving.instBinderF| [$(mkIdent tc) $(mkIdent param)])
  return TSyntaxArray.mk instances
'''
replacement = anchor + '''\npartial def syntaxMentionsIdent (stx : Syntax) (n : Name) : Bool :=
  if stx.isIdent then
    stx.getId == n
  else
    stx.getArgs.any (fun arg => syntaxMentionsIdent arg n)

'''
if s.count(anchor) != 1:
    raise SystemExit(f'V174_HELPER_ANCHOR_COUNT:{s.count(anchor)}')
s = s.replace(anchor, replacement, 1)

# In both standalone and mutual emitters, `outputTypeSyntaxes` has already been
# populated from target variables before the default type-parameter binders are
# created. Keep the old producer+equality pair only for parameters occurring in
# an output type. Fixed-input-only parameters receive no default capability.
old_standalone = '''    let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[producerUnconstrainedClass, ``DecidableEq]
'''
new_standalone = '''    let outputLiveTypeParams := typeParams.filter fun typeParam =>
      outputTypeSyntaxes.any (fun outputTy => syntaxMentionsIdent outputTy.raw typeParam)
    let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders outputLiveTypeParams #[producerUnconstrainedClass, ``DecidableEq]
'''
if s.count(old_standalone) != 3:
    raise SystemExit(f'V174_PRODUCER_ANCHOR_COUNT:{s.count(old_standalone)}')
# First occurrence = standalone instance, second = mutual def, third = mutual producer instance.
s = s.replace(old_standalone, new_standalone, 3)

# Mutual checker/theorem instances do not generate a value output. Their real
# Enum/DecidableEq needs must continue to arrive through the requirement path,
# as already demonstrated by V171 equality safety.
old_checker = '''        let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[``Enum, ``DecidableEq]
'''
new_checker = '''        let arbitraryTypeParamInstances : TSyntaxArray `Lean.Parser.Term.bracketedBinder := #[]
'''
if s.count(old_checker) != 1:
    raise SystemExit(f'V174_CHECKER_ANCHOR_COUNT:{s.count(old_checker)}')
s = s.replace(old_checker, new_checker, 1)

# Apparatus checks.
remaining = [line.strip() for line in s.splitlines()
             if 'mkTypeClassInstanceBinders typeParams' in line]
if remaining:
    raise SystemExit('V174_UNSCOPED_DEFAULT_BINDERS_REMAIN:' + ' | '.join(remaining))
for required in ['syntaxMentionsIdent', 'outputLiveTypeParams', 'mkTypeClassInstanceBinders outputLiveTypeParams']:
    if required not in s:
        raise SystemExit(f'V174_MISSING:{required}')
for forbidden in ['V172MapRel','V172SetRel','Diag','NEqGenerator','V171Gen','V171EqRel','fixtures/']:
    if forbidden in s:
        raise SystemExit(f'V174_TARGET_TOKEN_LEAK:{forbidden}')

p.write_text(s)
print('V174_OUTPUT_LIVE_TYPEPARAM_CAPABILITY_APPLIED')
