import Specimen.DeriveConstrainedProducer

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V118Params where
  tag : Nat

inductive V118ExplicitExpr : V118Params → Type where
  | unit (P : V118Params) : V118ExplicitExpr P

inductive V118ExplicitHas : (P : V118Params) → V118ExplicitExpr P → Prop where
  | unit (P : V118Params) : V118ExplicitHas P (.unit P)

derive_mutual (fun (P : V118Params) => ∃ e : V118ExplicitExpr P, V118ExplicitHas P e)
