import SpecimenTest.StrataLexprGen

open Lambda

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

abbrev V143ET0 : LExprParams := ⟨Unit, Unit⟩
abbrev V143EExpr := LExpr V143ET0.mono

inductive V143EHasType : List LMonoTy → V143EExpr → LMonoTy → Prop where
  | const : V143EHasType Δ (.const m c) c.ty
  | op    : V143EHasType Δ (.op m o (some ty)) ty
  | fvar  : V143EHasType Δ (.fvar m x (some ty)) ty
  | bvar  : Δ[i]? = some t → V143EHasType Δ (.bvar m i) t
  | abs   : V143EHasType (aty :: Δ) body rty →
            V143EHasType Δ (.abs m name (some aty) body) (.arrow aty rty)
  | quant : V143EHasType (qty :: Δ) tr τ_tr →
            V143EHasType (qty :: Δ) body .bool →
            V143EHasType Δ (.quant m k name (some qty) tr body) .bool
  | app   : V143EHasType Δ fn (.arrow aty rty) →
            V143EHasType Δ arg aty →
            V143EHasType Δ (.app m fn arg) rty
  | ite   : V143EHasType Δ c .bool →
            V143EHasType Δ t τ →
            V143EHasType Δ e τ →
            V143EHasType Δ (.ite m c t e) τ
  | eq    : V143EHasType Δ e1 τ →
            V143EHasType Δ e2 τ →
            V143EHasType Δ (.eq m e1 e2) .bool

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (Δ : List LMonoTy) (τ : LMonoTy) => ∃ e : V143EExpr, V143EHasType Δ e τ)
