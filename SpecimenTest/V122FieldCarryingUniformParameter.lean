import Specimen.DeriveConstrainedProducer

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V122AParams where
  tag : Nat

inductive V122AExpr (P : V122AParams) : Type where
  | mk (n : Nat) (b : Bool) : V122AExpr P

inductive V122AHas (P : V122AParams) : V122AExpr P → Prop where
  | mk (n : Nat) (b : Bool) : V122AHas P (.mk n b)

derive_mutual (fun (P : V122AParams) => ∃ e : V122AExpr P, V122AHas P e)
