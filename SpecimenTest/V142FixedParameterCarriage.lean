import SpecimenTest.StrataLexprGen

open Plausible
open ArbitrarySizedSuchThat
open Lambda

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

/- V142 isolates one distinction only: whether a fixed structure parameter carried by
   the produced inductive type is preserved, versus an otherwise equivalent
   parameter-erased monomorphic inductive. The historical StrataLexprGen import
   already attests the parameter-erased LExprU/HasTypeAU path. -/

abbrev V142T0 : LExprParams := ⟨Unit, Unit⟩
abbrev V142Expr := LExpr V142T0.mono

inductive V142HasType : V142Expr → LMonoTy → Prop where
  | const : V142HasType (.const m c) c.ty
  | abs   : V142HasType body rty →
            V142HasType (.abs m name (some aty) body) (.arrow aty rty)

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (τ : LMonoTy) => ∃ e : V142Expr, V142HasType e τ)
