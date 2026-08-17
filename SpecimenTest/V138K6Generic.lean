import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible
set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V138GenericP where
  Payload : Type

inductive V138GenericBox (p : V138GenericP) : Type where
| mk (x : p.Payload) : V138GenericBox p

inductive V138GenericHas (p : V138GenericP) : V138GenericBox p → Nat → Prop where
| mk (x : p.Payload) (n : Nat) : V138GenericHas p (V138GenericBox.mk x) n

derive_mutual (fun (p : V138GenericP) (n : Nat) => ∃ b : V138GenericBox p, V138GenericHas p b n)
