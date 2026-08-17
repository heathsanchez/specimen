import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible
set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V139Cfg where
  Payload : Type

def V139Cfg0 : V139Cfg := ⟨Bool⟩

def V139Family (p : V139Cfg) (_n : Nat) : Type := p.Payload

inductive V139Box (p : V139Cfg) (n : Nat) : Type where
| mk (x : V139Family p n) : V139Box p n

inductive V139Has (p : V139Cfg) (n : Nat) : V139Box p n → Prop where
| mk (x : V139Family p n) : V139Has p n (V139Box.mk x)

derive_mutual (fun (n : Nat) => ∃ b : V139Box V139Cfg0 n, V139Has V139Cfg0 n b)
