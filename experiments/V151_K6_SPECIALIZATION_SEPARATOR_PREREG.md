# V151 — K6 specialization separator preregistration

Frozen before V151 outcomes are inspected.

V150 moved the failure outward: the generated inner producer body elaborates with the propagated dependent `Arbitrary` premise, but `#synth` of the concrete constrained-producer instance still fails.

V151 performs no Specimen core intervention. It distinguishes ordinary Lean dependent typeclass specialization from Specimen instance emission/registration.

Frozen family: structure `P` with field `Meta : Type`, fixed `P0 := ⟨Unit⟩`, dependent `Box p`, predicate `Has`.

Arms:
A. `#synth Plausible.Arbitrary P0.Meta`.
B. A hand-written generic conditional instance `(p : P) [Plausible.Arbitrary p.Meta] : ArbitrarySizedSuchThat (Box p) (fun b => Has b)`, followed by `#synth` at `P0`.
C. Specimen-derived V150-style generic conditional instance (V148 outer + V150 inner propagation), followed by the same fixed `#synth`.

Interpretation is frozen:
- A fail => ordinary dependent premise reduction/applicability residual; do not blame Specimen registration.
- A pass, B fail => generic Lean conditional-head applicability residual.
- A pass, B pass, C fail => Specimen emission/registration residual; next intervention must target emitted instance structure rather than premise discovery/propagation.
- A/B/C pass => specialization barrier is cleared, but no K6 admission without protected tests and held-out transfer.

Any arm that does not exercise its intended mechanism is R10.