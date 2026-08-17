import SpecimenTest.StrataDefs.LambdaCore
import Specimen.DeriveConstrainedProducer

open Lambda

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

inductive V141Expr : Type where
  | lit (n : Nat)
  | abs (aty : LMonoTy) (body : V141Expr)

inductive V141HasType : V141Expr → LMonoTy → Prop where
  | lit : V141HasType (.lit n) .int
  | abs : V141HasType body rty →
          V141HasType (.abs aty body) (.arrow aty rty)

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (τ : LMonoTy) => ∃ e : V141Expr, V141HasType e τ)
