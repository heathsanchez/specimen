# V152 — dependent projection normalization separator

Frozen before any V152 outcome is inspected.

## Residual
V151 showed that `#synth Plausible.Arbitrary P0.Meta` fails when `P0` is a named `def := ⟨Unit⟩`. Therefore the V150 failure cannot yet be attributed to Specimen instance emission; ordinary typeclass search already fails on the required dependent projection.

## Question
Is the barrier specifically transparency/normalization of a named closed dependent index, and can a lawful specialized bridge remove it without changing the generic producer mechanism?

## Frozen arms
A. Direct control: `#synth Plausible.Arbitrary Unit`.
B. Literal projection: `#synth Plausible.Arbitrary (P.mk Unit).Meta`.
C. `abbrev PA : P := ⟨Unit⟩`; synthesize `Arbitrary PA.Meta`.
D. `def PD : P := ⟨Unit⟩`; synthesize `Arbitrary PD.Meta`.
E. Construct an exact bridge instance `Arbitrary PD.Meta` by explicitly changing its goal to `Arbitrary Unit`, then verify direct premise synthesis.
F. With that exact bridge plus a hand-written generic conditional constrained-producer instance `[Arbitrary p.Meta]`, verify fixed `#synth` at `PD`.
G. A directly specialized fixed constrained-producer instance at `PD`, with a body generated from `Unit`, must elaborate and synthesize.

## Frozen interpretation
- A fail: apparatus/reference failure => R10.
- A pass, B fail: projection reduction itself is blocked; K6 normalization hypothesis rejected.
- B pass and D fail: named-definition transparency is a real separator.
- C distinguishes whether `abbrev` transparency removes the barrier.
- E pass proves an exact normalized bridge is expressible in old Lean.
- F pass proves the generic conditional instance is usable once the closed dependent requirement is normalized/bridged.
- G pass proves a direct closed-value specialized producer is expressible without a new primitive.

A V152 result does **not** admit K6. It only decides the representation mechanism. Any K6 intervention must subsequently be generic, held-out, ablated, and protected-suite clean.