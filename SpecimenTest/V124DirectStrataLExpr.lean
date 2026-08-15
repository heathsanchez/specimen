import SpecimenTest.StrataDefs.LambdaCore
import Plausible.Gen
import Specimen.DecOpt
import Plausible.Arbitrary
import Specimen.ArbitrarySizedSuchThat
import Specimen.DeriveConstrainedProducer
import Specimen.DeriveArbitrary
import Specimen.DeriveEnum

open Plausible
open ArbitrarySizedSuchThat
open Lambda

set_option guard_msgs.diff true
set_option specimen.autoDeriveDeps true
set_option specimen.multiOutput true

/-- The same trivial monomorphic parameter choice used by the existing
    `LExprU` workaround, but here we retain the real parameterized `LExpr`. -/
def V124Base : LExprParams := ⟨Unit, Unit⟩
abbrev V124Expr := LExpr V124Base.mono

instance : Arbitrary Rat where
  arbitrary := do return (Rat.ofInt (← Arbitrary.arbitrary))

deriving instance Arbitrary for QuantifierKind
deriving instance Arbitrary for LConst
deriving instance Arbitrary for Identifier

instance : Arbitrary LMonoTy where
  arbitrary := do
    let choices : List LMonoTy :=
      [.int, .bool, .string,
       .arrow .int .bool, .arrow .bool .bool, .arrow .int .int]
    let n ← Plausible.Gen.chooseNatLt 0 choices.length (by decide)
    return choices[n.val]!

instance v124LookupProducer (Δ : List LMonoTy) (t : LMonoTy) :
    ArbitrarySizedSuchThat Nat (fun i => Δ[i]? = some t) where
  arbitrarySizedST _ := do
    let candidates := (List.range Δ.length).filter (fun i => Δ[i]? = some t)
    match candidates with
    | [] => throw Plausible.Gen.genericFailure
    | c :: cs =>
      let n ← Plausible.Gen.chooseNatLt 0 (c :: cs).length (by simp)
      return (c :: cs)[n.val]!

instance v124LookupProducerSyn (Δ : List LMonoTy) :
    ArbitrarySizedSuchThat (Nat × Option LMonoTy) (fun p => Δ[p.1]? = p.2) where
  arbitrarySizedST _ := do
    if h : 0 < Δ.length then
      let n ← Plausible.Gen.chooseNatLt 0 Δ.length h
      return (n.val, Δ[n.val]?)
    else
      return (0, none)

/-- Direct derivation over the real Strata-style parameterized expression type.
    No copied `LExprU` or copied typing relation is used. -/
#guard_msgs(drop info, drop warning) in
derive_mutual (fun Δ τ => ∃ e : V124Expr, LExpr.HasTypeA (T := V124Base) Δ e τ)

/-- A computable checker over the real parameterized expression type, mirroring
    the declarative `HasTypeA` rules used by the existing Strata validation. -/
def v124TypeCheck (ctx : List LMonoTy) : V124Expr → Option LMonoTy
  | .const _ c => some c.ty
  | .op _ _ (some ty) => some ty
  | .op _ _ none => none
  | .fvar _ _ (some ty) => some ty
  | .fvar _ _ none => none
  | .bvar _ i => ctx[i]?
  | .abs _ _ (some aty) body => (v124TypeCheck (aty :: ctx) body).map (.arrow aty ·)
  | .abs _ _ none _ => none
  | .quant _ _ _ (some qty) tr body =>
      match v124TypeCheck (qty :: ctx) tr, v124TypeCheck (qty :: ctx) body with
      | some _, some (.tcons "bool" []) => some .bool
      | _, _ => none
  | .quant _ _ _ none _ _ => none
  | .app _ fn arg =>
      match v124TypeCheck ctx fn, v124TypeCheck ctx arg with
      | some (.tcons "arrow" [dom, cod]), some aty => if dom = aty then some cod else none
      | _, _ => none
  | .ite _ c t e =>
      match v124TypeCheck ctx c, v124TypeCheck ctx t, v124TypeCheck ctx e with
      | some (.tcons "bool" []), some tt, some et => if tt = et then some tt else none
      | _, _, _ => none
  | .eq _ a b =>
      match v124TypeCheck ctx a, v124TypeCheck ctx b with
      | some ta, some tb => if ta = tb then some .bool else none
      | _, _ => none

/-- 60 verifier samples across five context/type requests. -/
#guard_msgs(drop info) in
#eval show IO Unit from do
  let trials : List (List LMonoTy × LMonoTy) :=
    [([.int, .bool], .bool), ([.int], .int), ([], .bool),
     ([.bool, .int, .string], .string), ([.arrow .int .bool, .int], .bool)]
  for (ctx, τ) in trials do
    for s in List.range 12 do
      let e ← Gen.run (ArbitrarySizedSuchThat.arbitrarySizedST
        (fun e : V124Expr => LExpr.HasTypeA (T := V124Base) ctx e τ) 4) (s * 7 + 1)
      unless v124TypeCheck ctx e == some τ do
        throw (IO.userError s!"V124 ill-typed direct-Strata sample: expected {repr τ}, got {repr (v124TypeCheck ctx e)}")
