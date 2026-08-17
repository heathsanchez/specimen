import V134SpecializationDefs

/-- GENERIC control: arbitrary p should retain a parameter-dependent field obligation. -/
derive_mutual (fun (p : V134P) (n : Nat) => ∃ b : V134Box p, V134Has b n)
