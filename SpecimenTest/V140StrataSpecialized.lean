import SpecimenTest.StrataLexprGen

open Lambda

abbrev V140ST0 : LExprParams := ⟨Unit, Unit⟩
abbrev V140SExpr := LExpr V140ST0.mono
abbrev V140SHasType (Δ : List LMonoTy) (e : V140SExpr) (τ : LMonoTy) : Prop :=
  LExpr.HasTypeA (T := V140ST0) Δ e τ

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (Δ : List LMonoTy) (τ : LMonoTy) =>
    ∃ e : V140SExpr, V140SHasType Δ e τ)

def v140TypeCheck (ctx : List LMonoTy) : V140SExpr → Option LMonoTy
  | .const _ c => some c.ty
  | .op _ _ (some ty) => some ty
  | .op _ _ none => none
  | .fvar _ _ (some ty) => some ty
  | .fvar _ _ none => none
  | .bvar _ i => ctx[i]?
  | .abs _ _ (some aty) body => (v140TypeCheck (aty :: ctx) body).map (.arrow aty ·)
  | .abs _ _ none _ => none
  | .quant _ _ _ (some qty) tr body =>
      match v140TypeCheck (qty :: ctx) tr, v140TypeCheck (qty :: ctx) body with
      | some _, some (.tcons "bool" []) => some .bool
      | _, _ => none
  | .quant _ _ _ none _ _ => none
  | .app _ fn arg =>
      match v140TypeCheck ctx fn, v140TypeCheck ctx arg with
      | some (.tcons "arrow" [dom, cod]), some aty => if dom = aty then some cod else none
      | _, _ => none
  | .ite _ c t e =>
      match v140TypeCheck ctx c, v140TypeCheck ctx t, v140TypeCheck ctx e with
      | some (.tcons "bool" []), some tt, some et => if tt = et then some tt else none
      | _, _ => none
  | .eq _ a b =>
      match v140TypeCheck ctx a, v140TypeCheck ctx b with
      | some ta, some tb => if ta = tb then some .bool else none
      | _, _ => none

#guard_msgs(drop info) in
#eval show IO Unit from do
  let trials : List (List LMonoTy × LMonoTy) :=
    [([.int, .bool], .bool), ([.int], .int), ([], .bool),
     ([.bool, .int, .string], .string), ([.arrow .int .bool, .int], .bool)]
  let mut checked := 0
  for (ctx, τ) in trials do
    for s in List.range 8 do
      let e ← Plausible.Gen.run
        (ArbitrarySizedSuchThat.arbitrarySizedST
          (fun e => V140SHasType ctx e τ) 4)
        (s * 11 + 3)
      unless v140TypeCheck ctx e == some τ do
        throw (IO.userError
          s!"V140 Strata sample failed executable typing check: ctx={repr ctx}, requested={repr τ}, got={repr (v140TypeCheck ctx e)}")
      checked := checked + 1
  unless checked == 40 do
    throw (IO.userError s!"V140 expected 40 checked samples, got {checked}")
  IO.println s!"V140_REAL_STRATA_SAMPLES_OK={checked}"
