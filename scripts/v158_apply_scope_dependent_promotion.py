from pathlib import Path

# V158 / V158A SCOPE_DEPENDENT_REQUIREMENT_PROMOTION
# Runs after V156 provenance transform + V156B checker compatibility.
# It does NOT use the invalid V157 creation-site synth query. Instead it narrows
# promotion to unconstrained requirements whose syntax depends on an actual
# generated input binder. Closed/global requirements retain baseline use-site
# synthesis behavior.

src_path = Path("Specimen/DeriveConstrainedProducer.lean")
src = src_path.read_text()

old_selector = '''      let unconstrainedTerms := requiredInstances.toList.filterMap fun req =>
        if req.origin == .unconstrained then some req.term else none
      let promotableInstances := (List.eraseDups unconstrainedTerms).toArray
'''
new_selector = '''      -- V158: only promote unconstrained requirements that actually depend on
      -- a generated producer input. This is a scope rule, not a name/type filter.
      let rec syntaxMentionsInput (s : Syntax) (inputNames : List Name) : Bool :=
        if s.isIdent then
          inputNames.contains s.getId
        else
          s.getArgs.any (fun child => syntaxMentionsInput child inputNames)
      let unconstrainedTerms := requiredInstances.toList.filterMap fun req =>
        if req.origin == .unconstrained &&
           syntaxMentionsInput req.term.raw freshenedInputNamesExcludingOutput then
          some req.term
        else none
      let promotableInstances := (List.eraseDups unconstrainedTerms).toArray
'''
if src.count(old_selector) != 1:
    raise SystemExit(f"V158 promotion selector anchor count != 1: {src.count(old_selector)}")
src = src.replace(old_selector, new_selector, 1)
src_path.write_text(src)

checks = {
    "scope helper": "syntaxMentionsInput" in src_path.read_text(),
    "input dependency": "freshenedInputNamesExcludingOutput" in src_path.read_text(),
    "provenance retained": "req.origin == .unconstrained" in src_path.read_text(),
    "syntax dependency retained": "syntaxMentionsInput req.term.raw" in src_path.read_text(),
}
missing = [name for name, ok in checks.items() if not ok]
if missing:
    raise SystemExit("V158 post-apply assertion failed: " + ", ".join(missing))

combined = src_path.read_text()
for forbidden in (
    "V153P", "V153Q", "V156Pair", "MemNat", "ScheduleQualityRegressionTest",
    "DependentArgs", "DeriveSTLCGenerator", "StrataLexprGen", "Cedar",
    "Unit", "Bool"
):
    if forbidden in combined:
        raise SystemExit(f"fixture/domain token leaked into V158 implementation: {forbidden}")

print("SCOPE_DEPENDENT_REQUIREMENT_PROMOTION_APPLIED")
