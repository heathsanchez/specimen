import Specimen.DeriveConstrainedProducer
import Specimen.ArbitrarySizedSuchThat
import Plausible.Arbitrary

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true
set_option trace.plausible.deriving.arbitrary true

structure V135TraceP where
  Meta : Type

def V135TraceP0 : V135TraceP := ⟨Unit⟩

inductive V135TraceBox (p : V135TraceP) : Type where
| mk (x : p.Meta) : V135TraceBox p

inductive V135TraceHas {p : V135TraceP} : V135TraceBox p → Nat → Prop where
| mk (x : p.Meta) (n : Nat) : V135TraceHas (V135TraceBox.mk x) n

derive_mutual (fun (n : Nat) => ∃ b : V135TraceBox V135TraceP0, @V135TraceHas V135TraceP0 b n)
