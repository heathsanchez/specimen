import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible
set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V138BoolP where
  Payload : Type

def V138BoolP0 : V138BoolP := ⟨Bool⟩

inductive V138BoolBox (p : V138BoolP) : Type where
| mk (x : p.Payload) : V138BoolBox p

inductive V138BoolHas (p : V138BoolP) : V138BoolBox p → Nat → Prop where
| mk (x : p.Payload) (n : Nat) : V138BoolHas p (V138BoolBox.mk x) n

derive_mutual (fun (n : Nat) => ∃ b : V138BoolBox V138BoolP0, V138BoolHas V138BoolP0 b n)
