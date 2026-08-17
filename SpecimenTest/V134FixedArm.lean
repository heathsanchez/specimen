import SpecimenTest.V134SpecializationDefs

/-- FIXED arm: P0.Meta is definitionally Unit, so symbolic p.Meta obligations should disappear if specialization propagates before synthesis. -/
derive_mutual (fun (n : Nat) => ∃ b : V134Box V134P0, @V134Has V134P0 b n)
