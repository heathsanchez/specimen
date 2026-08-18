import Specimen.DeriveConstrainedProducer
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V143DirectParams : Type 1 where
  Meta : Type

abbrev V143DirectP0 : V143DirectParams := ⟨Unit⟩

inductive V143DirectTy : Type where
  | atom
  | arrow (a b : V143DirectTy)
  deriving Repr, BEq

instance : Arbitrary V143DirectTy where
  arbitrary := pure .atom

inductive V143DirectExpr (p : V143DirectParams) : Type where
  | lit (m : p.Meta)
  | abs (m : p.Meta) (aty : V143DirectTy) (body : V143DirectExpr p)

inductive V143DirectHasType : V143DirectExpr V143DirectP0 → V143DirectTy → Prop where
  | lit : V143DirectHasType (.lit ()) .atom
  | abs : V143DirectHasType body rty →
          V143DirectHasType (.abs () aty body) (.arrow aty rty)

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (τ : V143DirectTy) => ∃ e : V143DirectExpr V143DirectP0, V143DirectHasType e τ)
