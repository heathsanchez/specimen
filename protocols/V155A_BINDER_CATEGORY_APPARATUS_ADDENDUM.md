# V155A — Binder Category Apparatus Addendum

V155 attempt 1 did not reach any intervention or protected scientific arm. It failed while compiling the intervention because the generated binder arrays had syntax category `Lean.Elab.Deriving.instBinderF`, while the splice point requires `Lean.Parser.Term.bracketedBinder`.

Classification: R10 apparatus / parser-category mismatch.

The only licensed repair is to construct the same uniquely named `[name : requiredInstance]` binders directly in the `Term.bracketedBinder` parser category (with explicit `TSyntaxArray bracketedBinder` typing if necessary). No change is permitted to:
- the frozen V155 question or gates,
- the requirement array,
- deduplication,
- outer/inner placement,
- fixtures,
- schedules/search/scoring,
- protected tests,
- filtering or special cases.

After this apparatus repair, rerun the full frozen V155 protocol from baseline.
