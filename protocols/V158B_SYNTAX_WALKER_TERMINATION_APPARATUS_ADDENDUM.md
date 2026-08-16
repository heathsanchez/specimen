# V158B — Syntax Walker Termination Apparatus Addendum

The first V158 execution was `R10_V158_INCONCLUSIVE`: the intervention text applied, but Lean rejected the local recursive helper `syntaxMentionsInput` because structural termination over `Syntax.getArgs` could not be inferred. No V158 discriminator or protected scientific gate executed.

Apparatus-only repair: implement the byte-equivalent logical predicate as a top-level `partial def` over `Syntax`, preserving exactly the frozen criterion: return true iff any identifier in the requirement syntax is one of the frozen generated input names. No fixture, target, provenance rule, promotion rule, admission gate, or claim boundary changes.
