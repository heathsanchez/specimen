from pathlib import Path

p = Path('Specimen/MakeConstrainedProducerInstance.lean')
s = p.read_text()
old = '    let arbitraryTypeParamInstances ← mkTypeClassInstanceBinders typeParams #[producerUnconstrainedClass, ``DecidableEq]\n'
new = '    let arbitraryTypeParamInstances : TSyntaxArray `Lean.Parser.Term.bracketedBinder := #[]\n'
# Exact standalone emitter only: require exactly one line at four-space indentation.
lines = s.splitlines(keepends=True)
hits = [i for i,line in enumerate(lines) if line == old]
if len(hits) != 1:
    raise SystemExit(f'V173_STANDALONE_ANCHOR_COUNT:{len(hits)}')
lines[hits[0]] = new
s = ''.join(lines)
# Mutual/checker emitter constructions must remain; this intervention is intentionally scoped.
remaining = [line for line in s.splitlines() if 'mkTypeClassInstanceBinders typeParams' in line]
if len(remaining) != 3:
    raise SystemExit(f'V173_UNEXPECTED_REMAINING_EMITTERS:{len(remaining)}:' + ' | '.join(remaining))
for forbidden in ['V170Fixed','V171Gen','V171EqRel','ISSUE19','Issue19','fixtures/']:
    if forbidden in s:
        raise SystemExit(f'V173_TARGET_TOKEN_LEAK:{forbidden}')
p.write_text(s)
print('V173_STANDALONE_PRODUCER_TYPEPARAM_PRUNING_APPLIED')
