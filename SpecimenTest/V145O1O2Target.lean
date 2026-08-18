import Specimen

open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

/- V145 frozen residual.  It combines exactly two previously isolated shapes:
   (1) `k` is an implicit uniform parameter of the relation family (O1/K2 shape);
   (2) `n + 1` is computed entirely from a relation input and occurs in the
       dependent type of the output witness (O2/K5 shape).
   There are no hand-written constrained instances and no target-specific repair. -/

inductive V145Cell : Nat → Type where
  | mk (n : Nat) : V145Cell n
  deriving Repr

inductive V145Rel {k : Nat} (n : Nat) : V145Cell (n + 1) → Prop where
  | mk : V145Rel (k := k) n (V145Cell.mk (n + 1))

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (k n : Nat) => ∃ x : V145Cell (n + 1), V145Rel (k := k) n x)
