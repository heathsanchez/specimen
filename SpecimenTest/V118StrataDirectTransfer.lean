import SpecimenTest.StrataLexprGen

open Lambda

/-- Concrete metadata specialization used only for the executable sample gate.
    The derivation itself below is generic in `T`; this avoids baking a constant
    structure expression into a position where Specimen requires an input
    variable. -/
abbrev V118T0 : LExprParams := ⟨Unit, Unit⟩
abbrev V118RealExpr := LExpr V118T0.mono

/- Directly derive over the real parameterized Strata expression type and the
   unchanged declarative typing relation. `T` is an input variable, with the
   ordinary producer assumptions needed for constructor metadata exposed as
   instance parameters. K1b was frozen before this target was executed. -/
#guard_msgs(drop info, drop warning) in
derive_mutual
  (fun (T : LExprParams) [Arbitrary T.Metadata] [Arbitrary T.IDMeta] Δ τ =>
    ∃ e : LExpr T.mono, LExpr.HasTypeA (T := T) Δ e τ)

/-- Executable checker mirroring the unchanged `HasTypeA` rules, used only to
    independently test generated samples at the concrete `V118T0` metadata
    specialization. -/
def v118TypeCheck (ctx : List LMonoTy) : V118RealExpr → Option LMonoTy
  | .const _ c => some c.ty
  | .op _ _ (some ty) => some ty
  | .op _ _ none => none
  | .fvar _ _ (some ty) => some ty
  | .fvar _ _ none => none
  | .bvar _ i => ctx[i]?
  | .abs _ _ (some aty) body => (v118TypeCheck (aty :: ctx) body).map (.arrow aty ·)
  | .abs _ _ none _ => none
  | .quant _ _ _ (some qty) tr body =>
      match v118TypeCheck (qty :: ctx) tr, v118TypeCheck (qty :: ctx) body with
      | some _, some (.tcons "bool" []) => some .bool
      | _, _ => none
  | .quant _ _ _ none _ _ => none
  | .app _ fn arg =>
      match v118TypeCheck ctx fn, v118TypeCheck ctx arg with
      | some (.tcons "arrow" [dom, cod]), some aty => if dom = aty then some cod else none
      | _, _ => none
  | .ite _ c t e =>
      match v118TypeCheck ctx c, v118TypeCheck ctx t, v118TypeCheck ctx e with
      | some (.tcons "bool" []), some tt, some et => if tt = et then some tt else none
      | _, _, _ => none
  | .eq _ a b =>
      match v118TypeCheck ctx a, v118TypeCheck ctx b with
      | some ta, some tb => if ta = tb then some .bool else none
      | _, _ => none

/- Soundness/behavior gate: sample 40 direct `Lambda.LExpr` values from the
   derived constrained generator and independently check the requested type. -/
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
          (fun e => LExpr.HasTypeA (T := V118T0) ctx e τ) 4)
        (s * 11 + 3)
      unless v118TypeCheck ctx e == some τ do
        throw (IO.userError
          s!"V118 direct Strata sample failed executable typing check: ctx={repr ctx}, requested={repr τ}, got={repr (v118TypeCheck ctx e)}")
      checked := checked + 1
  unless checked == 40 do
    throw (IO.userError s!"V118 expected 40 checked samples, got {checked}")
  IO.println s!"V118_STRATA_DIRECT_SAMPLES_OK={checked}"
