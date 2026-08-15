import Specimen.DeriveConstrainedProducer

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

structure V122BParams where
  tag : Nat

inductive V122BTree (P : V122BParams) : Type where
  | leaf : V122BTree P
  | node (payload : Nat) (child : V122BTree P) : V122BTree P

inductive V122BHas (P : V122BParams) : V122BTree P → Prop where
  | leaf : V122BHas P (.leaf)
  | node (payload : Nat) (child : V122BTree P) :
      V122BHas P child → V122BHas P (.node payload child)

derive_mutual (fun (P : V122BParams) => ∃ t : V122BTree P, V122BHas P t)
