import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible
set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V138UnitP where
  Meta : Type

def V138UnitP0 : V138UnitP := ⟨Unit⟩

inductive V138UnitBox (p : V138UnitP) : Type where
| mk (x : p.Meta) : V138UnitBox p

inductive V138UnitHas (p : V138UnitP) : V138UnitBox p → Nat → Prop where
| mk (x : p.Meta) (n : Nat) : V138UnitHas p (V138UnitBox.mk x) n

derive_mutual (fun (n : Nat) => ∃ b : V138UnitBox V138UnitP0, V138UnitHas V138UnitP0 b n)
