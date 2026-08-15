import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

/-- Type-0 parameter carrier for the matched U0 arm. -/
structure V125P0 where
  tag : Nat

/-- Type-1 parameter carrier for the matched U1 arm. -/
structure V125P1 : Type 1 where
  Carrier : Type

inductive V125Box0 (p : V125P0) : Type where
| mk (n : Nat) : V125Box0 p

inductive V125Box1 (p : V125P1) : Type where
| mk (n : Nat) : V125Box1 p

inductive V125Has0 {p : V125P0} : V125Box0 p → Nat → Prop where
| mk (n : Nat) : V125Has0 (V125Box0.mk n) n

inductive V125Has1 {p : V125P1} : V125Box1 p → Nat → Prop where
| mk (n : Nat) : V125Has1 (V125Box1.mk n) n

/-- U0: structurally matched task whose fixed parameter carrier lives in `Type`. -/
derive_mutual (fun (p : V125P0) (n : Nat) => ∃ b : V125Box0 p, V125Has0 b n)

/-- U1: same shape, but the fixed parameter carrier lives in `Type 1`. -/
derive_mutual (fun (p : V125P1) (n : Nat) => ∃ b : V125Box1 p, V125Has1 b n)
