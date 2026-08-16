import Specimen.DeriveConstrainedProducer
import Specimen.DeriveArbitrary
import Plausible.Arbitrary

open Plausible

inductive V171Gen {α : Type} : α → Prop where
  | mk : V171Gen x

derive_generator (fun (α : Type) => ∃ x, @V171Gen α x)
