from pathlib import Path

# V156B apparatus-only representation adapter.
# DeriveChecker consumes advisory requirement terms exactly as before; the new
# provenance record is projected back to its original `.term` at this boundary.

path = Path("Specimen/DeriveChecker.lean")
src = path.read_text()
old = '''      if (not requiredInstances.isEmpty) then
        let deduplicatedInstances := List.eraseDups requiredInstances.toList
        trace[plausible.deriving.arbitrary] m!"Required typeclass instances (please derive these first if they aren't already defined):\\n{deduplicatedInstances}"
'''
new = '''      if (not requiredInstances.isEmpty) then
        let deduplicatedInstances := List.eraseDups (requiredInstances.toList.map (·.term))
        trace[plausible.deriving.arbitrary] m!"Required typeclass instances (please derive these first if they aren't already defined):\\n{deduplicatedInstances}"
'''
if src.count(old) != 1:
    raise SystemExit(f"V156B DeriveChecker adapter anchor count != 1: {src.count(old)}")
src = src.replace(old, new, 1)
path.write_text(src)

if "List.eraseDups (requiredInstances.toList.map (·.term))" not in path.read_text():
    raise SystemExit("V156B post-apply adapter assertion failed")

print("V156B_CHECKER_CONSUMER_COMPAT_APPLIED")
