import Specimen.DeriveChecker
import Specimen.DecOpt
import Plausible

inductive V163Atom where
  | A | B | C
deriving Plausible.Arbitrary

derive_checker (fun a b => Eq (α := V163Atom) a b)

#synth DecOpt (V163Atom.A = V163Atom.B)
