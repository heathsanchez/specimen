import Specimen.DeriveConstrainedProducer
import Specimen.DeriveChecker
import Specimen.DecOpt
import Specimen.GeneratorCombinators
import Specimen.ArbitrarySizedSuchThat
import Specimen.DeriveArbitrary
import Plausible

inductive E where
  | A | B | C | D | E_ | F | G | H | I_ | J | K
deriving Plausible.Arbitrary

inductive Excludes : E → Prop where
  | clause0 :
      op ≠ E.A → op ≠ E.B → op ≠ E.C → op ≠ E.D →
      op ≠ E.E_ → op ≠ E.F → op ≠ E.G → op ≠ E.H →
      op ≠ E.I_ → op ≠ E.J →
      Excludes op

set_option maxRecDepth 4096
set_option maxHeartbeats 4000000
set_option profiler true

derive_checker   (fun op => Excludes op)
derive_generator (∃ (op : _), Excludes op)
