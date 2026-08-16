import Specimen.DeriveConstrainedProducer
import Specimen.DeriveArbitrary
import Plausible.Arbitrary

open Plausible

inductive V170Fixed where
  | only

inductive V170ParamRel {α : Type} : α → Nat → Prop where
  | mk : V170ParamRel x 0

derive_generator (fun (α : Type) (x : α) => ∃ n, @V170ParamRel α x n)

#synth ArbitrarySizedSuchThat Nat (fun n => @V170ParamRel V170Fixed V170Fixed.only n)
