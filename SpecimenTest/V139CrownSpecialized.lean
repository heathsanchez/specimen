import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible
set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V139SCfg where
  Payload : Type

def V139SCfg0 : V139SCfg := ⟨Bool⟩

def V139SFamily (p : V139SCfg) (_n : Nat) : Type := p.Payload

inductive V139SBox (p : V139SCfg) (n : Nat) : Type where
| mk (x : V139SFamily p n) : V139SBox p n

inductive V139SHas0 (n : Nat) : V139SBox V139SCfg0 n → Prop where
| mk (x : V139SFamily V139SCfg0 n) : V139SHas0 n (V139SBox.mk x)

derive_mutual (fun (n : Nat) => ∃ b : V139SBox V139SCfg0 n, V139SHas0 n b)
