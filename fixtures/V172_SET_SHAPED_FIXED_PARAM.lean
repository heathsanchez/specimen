import Specimen.DeriveConstrainedProducer
import Specimen.DeriveArbitrary
import Plausible.Arbitrary

open Plausible

inductive V172Elem where
  | elem

inductive V172SetRel {α : Type} : α → List α → Nat → Prop where
  | mk : V172SetRel x xs 0

derive_generator (fun (α : Type) (x : α) (xs : List α) => ∃ n, @V172SetRel α x xs n)

#synth ArbitrarySizedSuchThat Nat (fun n => @V172SetRel V172Elem V172Elem.elem [] n)
