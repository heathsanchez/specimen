from pathlib import Path

p = Path('Specimen/MakeConstrainedProducerInstance.lean')
lines = p.read_text().splitlines(keepends=True)

exact = {
    '    let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[producerUnconstrainedClass, ``DecidableEq]\n':
        '    let arbitraryTypeParamInstances : TSyntaxArray `Lean.Parser.Term.bracketedBinder := #[]\n',
    '    let defTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[producerUnconstrainedClass, ``DecidableEq]\n':
        '    let defTypeParamInstances : TSyntaxArray `Lean.Parser.Term.bracketedBinder := #[]\n',
    '        let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[``Enum, ``DecidableEq]\n':
        '        let arbitraryTypeParamInstances : TSyntaxArray `Lean.Parser.Term.bracketedBinder := #[]\n',
    '        let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[producerUnconstrainedClass, ``DecidableEq]\n':
        '        let arbitraryTypeParamInstances : TSyntaxArray `Lean.Parser.Term.bracketedBinder := #[]\n',
}
counts = {k: 0 for k in exact}
out = []
for line in lines:
    if line in exact:
        counts[line] += 1
        out.append(exact[line])
    else:
        out.append(line)

bad = {k.strip(): v for k,v in counts.items() if v != 1}
if bad:
    raise SystemExit('V171_EXACT_ANCHOR_COUNTS:' + repr(bad))

s = ''.join(out)
remaining = [line for line in s.splitlines() if 'mkTypeClassInstanceBinders typeParams' in line]
if remaining:
    raise SystemExit('V171_INCOMPLETE_DELETION:' + ' | '.join(remaining))

for forbidden in ['V170Fixed','V171Gen','V171EqRel','ISSUE19','Issue19','fixtures/']:
    if forbidden in s:
        raise SystemExit(f'V171_TARGET_TOKEN_LEAK:{forbidden}')

p.write_text(s)
print('V171_DEFAULT_TYPEPARAM_CONSTRAINTS_DELETED_ALL_EMITTERS')
