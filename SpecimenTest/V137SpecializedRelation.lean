import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V137P where
  Meta : Type

def V137P0 : V137P := ⟨Unit⟩

inductive V137Box (p : V137P) : Type where
| mk (x : p.Meta) : V137Box p

inductive V137HasP0 : V137Box V137P0 → Nat → Prop where
| mk (x : Unit) (n : Nat) : V137HasP0 (V137Box.mk x) n

derive_mutual (fun (n : Nat) => ∃ b : V137Box V137P0, V137HasP0 b n)
