import SpecimenTest.StrataLexprGen

open Lambda

abbrev V140T0 : LExprParams := ⟨Unit, Unit⟩

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (Δ : List LMonoTy) (τ : LMonoTy) =>
    ∃ e : LExpr V140T0.mono, LExpr.HasTypeA (T := V140T0) Δ e τ)
