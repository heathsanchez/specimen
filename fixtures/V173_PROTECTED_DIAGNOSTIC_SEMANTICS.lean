import Plausible.Gen
import Plausible.Attr
import Specimen.DecOpt
import Specimen.ArbitrarySizedSuchThat
import Specimen.DeriveConstrainedProducer
import Specimen.DeriveChecker

open Plausible
open ArbitrarySizedSuchThat
open DecOpt

/-!
V173 semantic separator for the exact structural families whose protected
#guard_msgs snapshots changed under V171 deletion. Derivation diagnostics are
neutralized here; executable semantics are the oracle.
-/

inductive V173Bar where
  | bar

inductive V173Baz : V173Bar → V173Bar → Prop where
  | isBar : V173Baz .bar .bar

#guard_msgs(drop error, drop info) in
derive_generator (fun a => ∃ b, V173Baz a b)

/-- info: true -/
#guard_msgs in
#eval do
  let b ← Gen.run (ArbitrarySizedSuchThat.arbitrarySizedST (fun b => V173Baz V173Bar.bar b) 20) 0
  pure (match b with | .bar => true)

inductive V173Square : Nat → Nat × Nat → Prop where
  | sq : ∀ x, V173Square x (x, x)

#guard_msgs(drop error, drop info) in
derive_generator (fun p => ∃ x, V173Square x p)

/-- info: true -/
#guard_msgs in
#eval do
  let x ← Gen.run (ArbitrarySizedSuchThat.arbitrarySizedST (fun x => V173Square x (3, 3)) 20) 0
  pure (x == 3)

inductive V173Diag : (α : Type u) → α → α × α → Prop where
  | c : V173Diag α a (b, b)

#guard_msgs(drop error, drop info) in
derive_generator fun γ p => ∃ g, V173Diag γ g p

#guard_msgs(drop error, drop info) in
derive_checker fun γ g p => V173Diag γ g p

/-- info: true -/
#guard_msgs in
#eval do
  let g ← Gen.run (ArbitrarySizedSuchThat.arbitrarySizedST (fun g => @V173Diag Nat g (4, 4)) 20) 0
  pure (g == 4)

/-- info: true -/
#guard_msgs in
#eval match DecOpt.decOpt (@V173Diag Nat 4 (4, 4)) 20 with
  | .ok true => true
  | _ => false

abbrev V173Map α β := List (α × β)
abbrev V173Maps α β := List (V173Map α β)

inductive V173MapFind {α β : Type} : V173Map α β → α × β → Prop where
  | hd : V173MapFind ((x, y) :: m) (x, y)
  | tl : V173MapFind m (x, y) → V173MapFind (p :: m) (x, y)

#guard_msgs(drop error, drop info) in
derive_generator fun α β m => ∃ pa, @V173MapFind α β m pa

/-- info: true -/
#guard_msgs in
#eval do
  let pa ← Gen.run (ArbitrarySizedSuchThat.arbitrarySizedST (fun pa => @V173MapFind Nat Nat [(1, 2)] pa) 30) 0
  pure (pa == (1, 2))

inductive V173MapsFind : V173Maps α β → α × β → Prop where
  | hd : V173MapFind m (x, y) → V173MapsFind (m :: ms) (x, y)
  | tl : V173MapsFind ms (x, y) → V173MapsFind (m :: ms) (x, y)

#guard_msgs(drop error, drop info) in
derive_generator fun α β ms => ∃ pa, @V173MapsFind α β ms pa

/-- info: true -/
#guard_msgs in
#eval do
  let pa ← Gen.run (ArbitrarySizedSuchThat.arbitrarySizedST (fun pa => @V173MapsFind Nat Nat [[(5, 6)]] pa) 30) 0
  pure (pa == (5, 6))

inductive V173FirstOf {α β : Type} : α × β → α → Prop where
  | mk : V173FirstOf (x, y) x

#guard_msgs(drop error, drop info) in
derive_generator fun α β p => ∃ x, @V173FirstOf α β p x

/-- info: true -/
#guard_msgs in
#eval do
  let x ← Gen.run (ArbitrarySizedSuchThat.arbitrarySizedST (fun x => @V173FirstOf Nat Nat (7, 9) x) 20) 0
  pure (x == 7)
