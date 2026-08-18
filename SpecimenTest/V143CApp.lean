import SpecimenTest.StrataLexprGen

open Lambda

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

abbrev V143CT0 : LExprParams := ⟨Unit, Unit⟩
abbrev V143CExpr := LExpr V143CT0.mono

inductive V143CHasType : List LMonoTy → V143CExpr → LMonoTy → Prop where
  | const : V143CHasType Δ (.const m c) c.ty
  | abs   : V143CHasType (aty :: Δ) body rty →
            V143CHasType Δ (.abs m name (some aty) body) (.arrow aty rty)
  | app   : V143CHasType Δ fn (.arrow aty rty) →
            V143CHasType Δ arg aty →
            V143CHasType Δ (.app m fn arg) rty

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (Δ : List LMonoTy) (τ : LMonoTy) => ∃ e : V143CExpr, V143CHasType Δ e τ)
