import SpecimenTest.StrataLexprGen

open Lambda

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

abbrev V143DT0 : LExprParams := ⟨Unit, Unit⟩
abbrev V143DExpr := LExpr V143DT0.mono

inductive V143DHasType : List LMonoTy → V143DExpr → LMonoTy → Prop where
  | const : V143DHasType Δ (.const m c) c.ty
  | abs   : V143DHasType (aty :: Δ) body rty →
            V143DHasType Δ (.abs m name (some aty) body) (.arrow aty rty)
  | quant : V143DHasType (qty :: Δ) tr τ_tr →
            V143DHasType (qty :: Δ) body .bool →
            V143DHasType Δ (.quant m k name (some qty) tr body) .bool

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (Δ : List LMonoTy) (τ : LMonoTy) => ∃ e : V143DExpr, V143DHasType Δ e τ)
