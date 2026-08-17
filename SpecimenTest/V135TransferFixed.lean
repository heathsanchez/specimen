import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V135Q where
  Payload : Type

def V135Q0 : V135Q := ⟨Bool⟩

inductive V135Envelope (q : V135Q) : Type where
| wrap (x : q.Payload) : V135Envelope q

inductive V135Carries {q : V135Q} : V135Envelope q → String → Prop where
| mk (x : q.Payload) (tag : String) : V135Carries (V135Envelope.wrap x) tag

derive_mutual (fun (tag : String) => ∃ e : V135Envelope V135Q0, @V135Carries V135Q0 e tag)
