import Plausible.Arbitrary
import Specimen.ArbitrarySizedSuchThat
import Specimen.DeriveConstrainedProducer

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

/-- A family parameter with a type-valued field. -/
structure V134P where
  Meta : Type

/-- Concrete target parameter.  Its field is definitionally `Unit`. -/
def V134P0 : V134P := ⟨Unit⟩

/-- Data indexed by the family parameter; constructing `leaf` requires a value
    at the parameter-dependent type `p.Meta`. -/
inductive V134Box (p : V134P) : Type where
| leaf (m : p.Meta) : V134Box p

/-- Relation whose witness carries the same parameter-dependent field. -/
inductive V134Has {p : V134P} : V134Box p → Prop where
| leaf (m : p.Meta) : V134Has (V134Box.leaf m)

/-- GENERIC_ARM -/
-- derive_mutual (fun (p : V134P) => ∃ b : V134Box p, V134Has b)

/-- FIXED_ARM -/
-- derive_mutual (fun _ : Unit => ∃ b : V134Box V134P0, V134Has b)
