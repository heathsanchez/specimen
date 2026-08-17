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

inductive V137Has {p : V137P} : V137Box p → Nat → Prop where
| mk (x : p.Meta) (n : Nat) : V137Has (V137Box.mk x) n

derive_mutual (fun (n : Nat) => ∃ b : V137Box V137P0, @V137Has V137P0 b n)
