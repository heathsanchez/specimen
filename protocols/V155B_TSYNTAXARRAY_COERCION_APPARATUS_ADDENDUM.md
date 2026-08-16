# V155B — TSyntaxArray Coercion Apparatus Addendum

V155A again failed before scientific execution. Lean reported that `Term.bracketedBinder` is not a quotation parser. This is R10 apparatus.

The existing compiling function `mkTypeClassInstanceBinders` in `Specimen/MakeConstrainedProducerInstance.lean` already demonstrates the correct construction pattern: quote each binder with `Lean.Elab.Deriving.instBinderF`, collect those syntax values, then return `TSyntaxArray.mk instances` as `TSyntaxArray Lean.Parser.Term.bracketedBinder`.

The only licensed V155B repair is to use that exact existing construction pattern for the V155 outer and inner requirement binder arrays. Scientific intervention, requirement contents, deduplication, placement, fixtures, gates and protected tests remain frozen.
