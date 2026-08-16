import Specimen.DeriveChecker
import Specimen.DecOpt

inductive V171EqRel {α : Type} : α → α → Prop where
  | mk : x = y → V171EqRel x y

derive_checker (fun (α : Type) (x y : α) => @V171EqRel α x y)
