import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V136P where
  Meta : Type

def V136P0 : V136P := ⟨Unit⟩

inductive V136Box (p : V136P) : Type where
| mk (x : p.Meta) : V136Box p

inductive V136Has {p : V136P} : V136Box p → Nat → Prop where
| mk (x : p.Meta) (n : Nat) : V136Has (V136Box.mk x) n

derive_mutual (fun (n : Nat) => ∃ b : V136Box V136P0, @V136Has V136P0 b n)
