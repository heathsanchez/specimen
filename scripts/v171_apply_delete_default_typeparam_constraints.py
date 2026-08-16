from pathlib import Path

p = Path('Specimen/MakeConstrainedProducerInstance.lean')
s = p.read_text()

repls = {
'''    let defTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[producerUnconstrainedClass, ``DecidableEq]
''': '''    let defTypeParamInstances : TSyntaxArray `Lean.Parser.Term.bracketedBinder := #[]
''',
'''        let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[``Enum, ``DecidableEq]
''': '''        let arbitraryTypeParamInstances : TSyntaxArray `Lean.Parser.Term.bracketedBinder := #[]
''',
'''        let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[producerUnconstrainedClass, ``DecidableEq]
''': '''        let arbitraryTypeParamInstances : TSyntaxArray `Lean.Parser.Term.bracketedBinder := #[]
'''
}
for old,new in repls.items():
    if s.count(old) != 1:
        raise SystemExit(f'V171_ANCHOR_COUNT:{s.count(old)}')
    s = s.replace(old,new,1)

for forbidden in ['V170Fixed','V171Gen','V171EqRel','ISSUE19','Issue19','fixtures/']:
    if forbidden in s:
        raise SystemExit(f'V171_TARGET_TOKEN_LEAK:{forbidden}')

p.write_text(s)
print('V171_DEFAULT_TYPEPARAM_CONSTRAINTS_DELETED')
