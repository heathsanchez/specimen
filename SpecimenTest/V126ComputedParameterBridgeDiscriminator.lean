import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V126Base where
  tag : Nat

structure V126Wrapped : Type 1 where
  tag : Nat

def V126Lift (p : V126Base) : V126Wrapped := ⟨p.tag⟩

inductive V126BoxId (p : V126Base) : Type where
| mk (n : Nat) : V126BoxId p

inductive V126BoxMap (q : V126Wrapped) : Type where
| mk (n : Nat) : V126BoxMap q

inductive V126HasId {p : V126Base} : V126BoxId p → Nat → Prop where
| mk (n : Nat) : V126HasId (V126BoxId.mk n) n

inductive V126HasMap {p : V126Base} : V126BoxMap (V126Lift p) → Nat → Prop where
| mk (n : Nat) : V126HasMap (V126BoxMap.mk n) n

/-- ID arm. -/
derive_mutual (fun (p : V126Base) (n : Nat) => ∃ b : V126BoxId p, V126HasId b n)

/-- MAP arm. -/
derive_mutual (fun (p : V126Base) (n : Nat) => ∃ b : V126BoxMap (V126Lift p), V126HasMap b n)
