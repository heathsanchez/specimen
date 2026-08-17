import SpecimenTest.StrataLexprGen

open Lambda

abbrev V140ST0 : LExprParams := ⟨Unit, Unit⟩
abbrev V140SExpr := LExpr V140ST0.mono

/- V140B APPARATUS-ONLY REPAIR.
   This is the exact HasTypeA constructor grammar from the vendored Strata slice,
   materialized as an inductive at the already-frozen concrete specialization.
   No typing rule, constructor condition, search law, K2/K5 patch, or task has
   changed. The prior reducible alias was rejected by derive_mutual because it
   was not itself an inductive declaration. -/
inductive V140SHasType : List LMonoTy → V140SExpr → LMonoTy → Prop where
  | const : V140SHasType Δ (.const m c) c.ty
  | op    : V140SHasType Δ (.op m o (some ty)) ty
  | fvar  : V140SHasType Δ (.fvar m x (some ty)) ty
  | bvar  : Δ[i]? = some t → V140SHasType Δ (.bvar m i) t
  | abs   : V140SHasType (aty :: Δ) body rty →
            V140SHasType Δ (.abs m name (some aty) body) (.arrow aty rty)
  | quant : V140SHasType (qty :: Δ) tr τ_tr →
            V140SHasType (qty :: Δ) body .bool →
            V140SHasType Δ (.quant m k name (some qty) tr body) .bool
  | app   : V140SHasType Δ fn (.arrow aty rty) →
            V140SHasType Δ arg aty →
            V140SHasType Δ (.app m fn arg) rty
  | ite   : V140SHasType Δ c .bool →
            V140SHasType Δ t τ →
            V140SHasType Δ e τ →
            V140SHasType Δ (.ite m c t e) τ
  | eq    : V140SHasType Δ e1 τ →
            V140SHasType Δ e2 τ →
            V140SHasType Δ (.eq m e1 e2) .bool

#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (Δ : List LMonoTy) (τ : LMonoTy) =>
    ∃ e : V140SExpr, V140SHasType Δ e τ)

/- Exact executable checker used by the historical V118 Strata transfer gate. -/
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
      | _, _, _ => none
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
