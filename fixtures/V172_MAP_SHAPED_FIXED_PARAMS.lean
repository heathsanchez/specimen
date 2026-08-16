import Specimen.DeriveConstrainedProducer
import Specimen.DeriveArbitrary
import Plausible.Arbitrary

open Plausible

inductive V172Key where
  | key

inductive V172Val where
  | val

inductive V172MapRel {α β : Type} : α → β → List (α × β) → Nat → Prop where
  | mk : V172MapRel a b entries 0

derive_generator (fun (α β : Type) (a : α) (b : β) (entries : List (α × β)) => ∃ n, @V172MapRel α β a b entries n)

#synth ArbitrarySizedSuchThat Nat (fun n => @V172MapRel V172Key V172Val V172Key.key V172Val.val [] n)
