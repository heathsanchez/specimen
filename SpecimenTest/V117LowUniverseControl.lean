import Specimen.DeriveConstrainedProducer

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V117LowParams where
  tag : Nat

inductive V117LowExpr (P : V117LowParams) : Type where
  | unit : V117LowExpr P

inductive V117LowHas (P : V117LowParams) : V117LowExpr P → Prop where
  | unit : V117LowHas P (.unit)

derive_mutual (fun (P : V117LowParams) => ∃ e : V117LowExpr P, V117LowHas P e)
