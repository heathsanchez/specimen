import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V134P where
  Meta : Type

def V134P0 : V134P := ⟨Unit⟩

inductive V134Box (p : V134P) : Type where
| mk (x : p.Meta) : V134Box p

inductive V134Has {p : V134P} : V134Box p → Nat → Prop where
| mk (x : p.Meta) (n : Nat) : V134Has (V134Box.mk x) n

/-- GENERIC control: arbitrary p should retain a parameter-dependent field obligation. -/
derive_mutual (fun (p : V134P) (n : Nat) => ∃ b : V134Box p, V134Has b n)
