import SpecimenTest.StrataDefs.LambdaCore
import Specimen.DeriveConstrainedProducer
import Plausible.Arbitrary

open Lambda
open Plausible

set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

/- Apparatus-only prerequisite copied exactly in spirit from the historical
   Strata harness: the recursive-pair separator needs occasional unconstrained
   LMonoTy values before it can reach the intended constrained dependency. -/
instance : Arbitrary LMonoTy where
  arbitrary := do
    let choices : List LMonoTy :=
      [.int, .bool, .string,
       .arrow .int .bool, .arrow .bool .bool, .arrow .int .int]
    let n ← Plausible.Gen.chooseNatLt 0 choices.length (by decide)
    return choices[n.val]!

inductive V141Expr : Type where
  | lit (n : Nat)
  | abs (aty : LMonoTy) (body : V141Expr)

inductive V141HasType : V141Expr → LMonoTy → Prop where
  | lit : V141HasType (.lit n) .int
  | abs : V141HasType body rty →
          V141HasType (.abs aty body) (.arrow aty rty)

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (τ : LMonoTy) => ∃ e : V141Expr, V141HasType e τ)
