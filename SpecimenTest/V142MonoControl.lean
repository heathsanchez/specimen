import Specimen.DeriveConstrainedProducer
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

inductive V142Ty : Type where
  | atom
  | arrow (a b : V142Ty)
  deriving Repr, BEq

instance : Arbitrary V142Ty where
  arbitrary := pure .atom

inductive V142MonoExpr : Type where
  | lit
  | abs (aty : V142Ty) (body : V142MonoExpr)

inductive V142MonoHasType : V142MonoExpr → V142Ty → Prop where
  | lit : V142MonoHasType .lit .atom
  | abs : V142MonoHasType body rty →
          V142MonoHasType (.abs aty body) (.arrow aty rty)

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (τ : V142Ty) => ∃ e : V142MonoExpr, V142MonoHasType e τ)
