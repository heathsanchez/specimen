import Specimen.DeriveChecker
import Specimen.DecOpt
import Plausible

inductive V166Choice where
  | left (n : UInt8)
  | right (n : UInt8)
deriving Plausible.Arbitrary

inductive V166LeftOnly : V166Choice → Prop where
  | mk : n = 3 → V166LeftOnly (.left n)

derive_checker (fun c => V166LeftOnly c)
