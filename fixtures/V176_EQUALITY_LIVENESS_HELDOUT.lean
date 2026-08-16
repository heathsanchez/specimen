import Specimen

open Plausible
open ArbitrarySizedSuchThat

inductive V176EqLive (α : Type u) : α × α → Nat → Prop where
| c : V176EqLive α (x, x) 0

-- Held-out structural safety: output is Nat, so Arbitrary α is unnecessary,
-- but equality on the fixed input pair requires a lawful equality capability.
derive_generator fun α p => ∃ n, V176EqLive α p n

#synth ArbitrarySizedSuchThat Nat (fun n => V176EqLive Bool (true, true) n)
