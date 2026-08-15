import Specimen.DeriveConstrainedProducer

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V117HighParams where
  α : Type

inductive V117HighExpr (P : V117HighParams) : Type where
  | unit : V117HighExpr P

inductive V117HighHas (P : V117HighParams) : V117HighExpr P → Prop where
  | unit : V117HighHas P (.unit)

derive_mutual (fun (P : V117HighParams) => ∃ e : V117HighExpr P, V117HighHas P e)
