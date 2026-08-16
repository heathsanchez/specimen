from pathlib import Path

# V158 / V158A SCOPE_DEPENDENT_REQUIREMENT_PROMOTION
# V158B apparatus repair: the syntax dependency predicate is a top-level
# partial def so Lean need not infer structural termination over Syntax.getArgs.
# Scientific semantics are unchanged.

src_path = Path("Specimen/DeriveConstrainedProducer.lean")
src = src_path.read_text()

helper_anchor = '''open Idents Schedules ProofWidgets

'''
helper_block = '''open Idents Schedules ProofWidgets

/-- V158: does requirement syntax depend on one of the generated producer inputs? -/
partial def v158SyntaxMentionsInput (s : Syntax) (inputNames : List Name) : Bool :=
  if s.isIdent then
    inputNames.contains s.getId
  else
    s.getArgs.any (fun child => v158SyntaxMentionsInput child inputNames)

'''
if src.count(helper_anchor) != 1:
    raise SystemExit(f"V158 helper anchor count != 1: {src.count(helper_anchor)}")
src = src.replace(helper_anchor, helper_block, 1)

old_selector = '''      let unconstrainedTerms := requiredInstances.toList.filterMap fun req =>
        if req.origin == .unconstrained then some req.term else none
      let promotableInstances := (List.eraseDups unconstrainedTerms).toArray
'''
new_selector = '''      -- V158: only promote unconstrained requirements that actually depend on
      -- a generated producer input. This is a scope rule, not a name/type filter.
      let unconstrainedTerms := requiredInstances.toList.filterMap fun req =>
        if req.origin == .unconstrained &&
           v158SyntaxMentionsInput req.term.raw freshenedInputNamesExcludingOutput then
          some req.term
        else none
      let promotableInstances := (List.eraseDups unconstrainedTerms).toArray
'''
if src.count(old_selector) != 1:
    raise SystemExit(f"V158 promotion selector anchor count != 1: {src.count(old_selector)}")
src = src.replace(old_selector, new_selector, 1)
src_path.write_text(src)

checks = {
    "scope helper": "partial def v158SyntaxMentionsInput" in src_path.read_text(),
    "input dependency": "freshenedInputNamesExcludingOutput" in src_path.read_text(),
    "provenance retained": "req.origin == .unconstrained" in src_path.read_text(),
    "syntax dependency retained": "v158SyntaxMentionsInput req.term.raw" in src_path.read_text(),
}
missing = [name for name, ok in checks.items() if not ok]
if missing:
    raise SystemExit("V158 post-apply assertion failed: " + ", ".join(missing))

combined = src_path.read_text()
for forbidden in (
    "V153P", "V153Q", "V156Pair", "MemNat", "ScheduleQualityRegressionTest",
    "DependentArgs", "DeriveSTLCGenerator", "StrataLexprGen", "Cedar"
):
    if forbidden in combined:
        raise SystemExit(f"fixture/domain token leaked into V158 implementation: {forbidden}")

print("SCOPE_DEPENDENT_REQUIREMENT_PROMOTION_APPLIED")
