import Specimen.DeriveConstrainedProducer

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V118ImplicitParams where
  tag : Nat

inductive V118ImplicitExpr (P : V118ImplicitParams) : Type where
  | unit : V118ImplicitExpr P

inductive V118ImplicitHas (P : V118ImplicitParams) : V118ImplicitExpr P → Prop where
  | unit : V118ImplicitHas P (.unit)

derive_mutual (fun (P : V118ImplicitParams) => ∃ e : V118ImplicitExpr P, V118ImplicitHas P e)
