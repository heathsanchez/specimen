import Specimen.DeriveChecker
import Specimen.DecOpt
import Plausible

inductive V166Packet where
  | packet (tag : UInt8) (enabled : Bool)
deriving Plausible.Arbitrary

inductive V166Accept : V166Packet → Prop where
  | mk : tag = 2 → V166Accept (.packet tag enabled)

derive_checker (fun p => V166Accept p)
