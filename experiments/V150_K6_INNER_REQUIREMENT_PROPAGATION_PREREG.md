# V150 — K6 inner requirement propagation preregistration

Frozen before any V150 intervention outcome is inspected.

## Residual
V148 established that schedule compilation discovers the exact dependent requirement and that the generated outer instance can retain it, but the generated `aux_arb` body still fails to synthesize the same requirement. V148 therefore rejected outer-only requirement threading as sufficient.

## Candidate
`K6_INNER_REQUIREMENT_PROPAGATION`: preserve the exact already-discovered singleton dependent requirement in both (1) the generated outer instance context and (2) the generated inner producer function context. No fixed value, fixture type, constructor, or protected-test token may appear in implementation source.

This is a refinement of the V148 mechanism, not a new semantic constructor family.

## Frozen fixtures
A: dependent field `p.Meta`, fixed specialization reducing to `Unit`.
B held-out: independently named dependent field `q.Carrier`, fixed specialization reducing to `Bool`.

## Gates
G1 baseline reproduces `SYMBOLIC_INSTANCE`.
G2 intervention makes generic derivation and fixed A specialization elaborate.
G3 held-out B also elaborates without fixture-specific code.
G4 targeted ablation (no dependent premise propagation) restores the baseline failure.
G5 full protected `lake build` and `lake test` pass.
G6 implementation contains no V150 fixture identifiers.

PASS only if all gates pass. Missing execution artifacts or failure to exercise the intended mechanism is R10. If G2 or G3 fails after intended mechanism execution, this K6 refinement is rejected. If G5 fails, K6 is not admitted even if fixtures pass.

Claim boundary: a V150 PASS would admit only a scoped dependent-requirement propagation capability. Constructor-development claims still require a later natural/frontier task enabled by it.