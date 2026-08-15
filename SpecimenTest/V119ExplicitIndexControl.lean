import Specimen.DeriveConstrainedProducer

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V119Params where
  tag : Nat

inductive V119ExplicitExpr : V119Params → Type where
  | unit (P : V119Params) : V119ExplicitExpr P

inductive V119ExplicitHas : (P : V119Params) → V119ExplicitExpr P → Prop where
  | unit (P : V119Params) : V119ExplicitHas P (.unit P)

derive_mutual (fun (P : V119Params) => ∃ e : V119ExplicitExpr P, V119ExplicitHas P e)
