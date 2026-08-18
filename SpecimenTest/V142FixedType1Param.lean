import Specimen.DeriveConstrainedProducer
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V142Params : Type 1 where
  Meta : Type

abbrev V142P0 : V142Params := ⟨Unit⟩

inductive V142Ty : Type where
  | atom
  | arrow (a b : V142Ty)
  deriving Repr, BEq

instance : Arbitrary V142Ty where
  arbitrary := pure .atom

inductive V142Expr (p : V142Params) : Type where
  | lit (m : p.Meta)
  | abs (m : p.Meta) (aty : V142Ty) (body : V142Expr p)

inductive V142HasType : V142Expr V142P0 → V142Ty → Prop where
  | lit : V142HasType (.lit ()) .atom
  | abs : V142HasType body rty →
          V142HasType (.abs () aty body) (.arrow aty rty)

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (τ : V142Ty) => ∃ e : V142Expr V142P0, V142HasType e τ)
