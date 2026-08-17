import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V135R where
  Payload : Type

def V135R0 : V135R := ⟨Nat → Nat⟩

inductive V135OpaqueEnvelope (r : V135R) : Type where
| wrap (x : r.Payload) : V135OpaqueEnvelope r

inductive V135OpaqueCarries {r : V135R} : V135OpaqueEnvelope r → Nat → Prop where
| mk (x : r.Payload) (n : Nat) : V135OpaqueCarries (V135OpaqueEnvelope.wrap x) n

derive_mutual (fun (n : Nat) => ∃ e : V135OpaqueEnvelope V135R0, @V135OpaqueCarries V135R0 e n)
