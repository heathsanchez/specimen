import SpecimenTest.V143EFull
import Specimen.ArbitrarySizedSuchThat
import Plausible.Gen

open Plausible
open Lambda

def v144TypeCheck (ctx : List LMonoTy) : V143EExpr → Option LMonoTy
  | .const _ c => some c.ty
  | .op _ _ (some ty) => some ty
  | .op _ _ none => none
  | .fvar _ _ (some ty) => some ty
  | .fvar _ _ none => none
  | .bvar _ i => ctx[i]?
  | .abs _ _ (some aty) body => (v144TypeCheck (aty :: ctx) body).map (.arrow aty ·)
  | .abs _ _ none _ => none
  | .quant _ _ _ (some qty) tr body =>
      match v144TypeCheck (qty :: ctx) tr, v144TypeCheck (qty :: ctx) body with
      | some _, some (.tcons "bool" []) => some .bool
      | _, _ => none
  | .quant _ _ _ none _ _ => none
  | .app _ fn arg =>
      match v144TypeCheck ctx fn, v144TypeCheck ctx arg with
      | some (.tcons "arrow" [dom, cod]), some aty => if dom = aty then some cod else none
      | _, _ => none
  | .ite _ c t e =>
      match v144TypeCheck ctx c, v144TypeCheck ctx t, v144TypeCheck ctx e with
      | some (.tcons "bool" []), some tt, some et => if tt = et then some tt else none
      | _, _, _ => none
  | .eq _ a b =>
      match v144TypeCheck ctx a, v144TypeCheck ctx b with
      | some ta, some tb => if ta = tb then some .bool else none
      | _, _ => none

#eval show IO Unit from do
  let trials : List (List LMonoTy × LMonoTy) :=
    [([.int, .bool], .bool), ([.int], .int), ([], .bool),
     ([.bool, .int, .string], .string), ([.arrow .int .bool, .int], .bool)]
  let mut checked := 0
  for (ctx, τ) in trials do
    for s in List.range 8 do
      let e ← Gen.run
        (ArbitrarySizedSuchThat.arbitrarySizedST
          (fun e => V143EHasType ctx e τ) 4)
        (s * 11 + 3)
      unless v144TypeCheck ctx e == some τ do
        throw (IO.userError
          s!"V144 sample failed checker: ctx={repr ctx}, requested={repr τ}, got={repr (v144TypeCheck ctx e)}")
      checked := checked + 1
  unless checked == 40 do
    throw (IO.userError s!"V144 expected 40 checked samples, got {checked}")
  IO.println s!"V144_40_CHECKED_OK={checked}"
