import SpecimenTest.StrataLexprGen

open Lambda

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

abbrev V143BT0 : LExprParams := ⟨Unit, Unit⟩
abbrev V143BExpr := LExpr V143BT0.mono

inductive V143BHasType : List LMonoTy → V143BExpr → LMonoTy → Prop where
  | const : V143BHasType Δ (.const m c) c.ty
  | bvar  : Δ[i]? = some t → V143BHasType Δ (.bvar m i) t
  | abs   : V143BHasType (aty :: Δ) body rty →
            V143BHasType Δ (.abs m name (some aty) body) (.arrow aty rty)

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (Δ : List LMonoTy) (τ : LMonoTy) => ∃ e : V143BExpr, V143BHasType Δ e τ)
