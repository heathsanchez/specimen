import Specimen.DeriveConstrainedProducer

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V119ImplicitParams where
  tag : Nat

inductive V119ImplicitExpr (P : V119ImplicitParams) : Type where
  | unit : V119ImplicitExpr P

inductive V119ImplicitHas (P : V119ImplicitParams) : V119ImplicitExpr P → Prop where
  | unit : V119ImplicitHas P (.unit)

derive_mutual (fun (P : V119ImplicitParams) => ∃ e : V119ImplicitExpr P, V119ImplicitHas P e)
