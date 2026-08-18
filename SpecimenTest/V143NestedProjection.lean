import Specimen.DeriveConstrainedProducer
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V143Base : Type 1 where
  Metadata : Type

structure V143ParamsT : Type 1 where
  base : V143Base
  TypeType : Type

abbrev V143Base0 : V143Base := ⟨Unit⟩
abbrev V143Mono (b : V143Base) : V143ParamsT := ⟨b, V143Ty⟩

inductive V143Ty : Type where
  | atom
  | arrow (a b : V143Ty)
  deriving Repr, BEq

instance : Arbitrary V143Ty where
  arbitrary := pure .atom

inductive V143Expr (p : V143ParamsT) : Type where
  | lit (m : p.base.Metadata)
  | abs (m : p.base.Metadata) (aty : p.TypeType) (body : V143Expr p)

abbrev V143P0 : V143ParamsT := V143Mono V143Base0

inductive V143HasType : V143Expr V143P0 → V143Ty → Prop where
  | lit : V143HasType (.lit ()) .atom
  | abs : V143HasType body rty →
          V143HasType (.abs () aty body) (.arrow aty rty)

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (τ : V143Ty) => ∃ e : V143Expr V143P0, V143HasType e τ)
