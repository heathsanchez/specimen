import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible
set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V138NegP where
  Payload : Type

def V138NegP0 : V138NegP := ⟨Nat → Nat⟩

inductive V138NegBox (p : V138NegP) : Type where
| mk (x : p.Payload) : V138NegBox p

inductive V138NegHas (p : V138NegP) : V138NegBox p → Nat → Prop where
| mk (x : p.Payload) (n : Nat) : V138NegHas p (V138NegBox.mk x) n

derive_mutual (fun (n : Nat) => ∃ b : V138NegBox V138NegP0, V138NegHas V138NegP0 b n)
