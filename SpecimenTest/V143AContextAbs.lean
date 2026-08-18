import SpecimenTest.StrataLexprGen

open Lambda

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

abbrev V143AT0 : LExprParams := ⟨Unit, Unit⟩
abbrev V143AExpr := LExpr V143AT0.mono

inductive V143AHasType : List LMonoTy → V143AExpr → LMonoTy → Prop where
  | const : V143AHasType Δ (.const m c) c.ty
  | abs   : V143AHasType (aty :: Δ) body rty →
            V143AHasType Δ (.abs m name (some aty) body) (.arrow aty rty)

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (Δ : List LMonoTy) (τ : LMonoTy) => ∃ e : V143AExpr, V143AHasType Δ e τ)
