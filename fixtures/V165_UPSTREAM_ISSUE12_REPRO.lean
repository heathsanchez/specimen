import Specimen.DeriveChecker
import Specimen.DecOpt
import Plausible

structure S where
  a : UInt8
  b : UInt8
deriving Plausible.Arbitrary

inductive R : S → Prop where
| mk : x = 1 → R ⟨x, b⟩

derive_checker (fun s => R s)
