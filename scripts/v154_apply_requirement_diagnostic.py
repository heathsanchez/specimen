from pathlib import Path

p = Path('Specimen/DeriveConstrainedProducer.lean')
s = p.read_text()
old = '''      if (not requiredInstances.isEmpty) then
        let deduplicatedInstances := List.eraseDups requiredInstances.toList
        trace[plausible.deriving.arbitrary]  m!"Required typeclass instances (please derive these first if they aren't already defined):\\n{deduplicatedInstances}"
'''
new = '''      if (not requiredInstances.isEmpty) then
        let deduplicatedInstances := List.eraseDups requiredInstances.toList
        logInfo m!"V154_REQUIRED_INSTANCES count={deduplicatedInstances.length} values={deduplicatedInstances}"
        trace[plausible.deriving.arbitrary]  m!"Required typeclass instances (please derive these first if they aren't already defined):\\n{deduplicatedInstances}"
'''
if s.count(old) != 1:
    raise SystemExit(f'V154 anchor count != 1: {s.count(old)}')
p.write_text(s.replace(old,new,1))
print('V154_DIAGNOSTIC_ONLY_LOGGER_APPLIED')
