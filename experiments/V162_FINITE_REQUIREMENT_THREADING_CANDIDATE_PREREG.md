# V162 — Finite requirement threading candidate

## Status
Candidate and admission protocol frozen before V160 outcome. Do not execute unless V160 confirms that pure requirement multiplicity is independently present (L1 succeeds and L2 reaches the V156 arity ceiling at exactly two requirements).

## Candidate operator
`FINITE_REQUIREMENT_THREADING`: generalize the already-admitted V156 opt-in operator from one discovered dependent requirement to the complete **deduplicated finite array that V156 already computes**.

Strict scope:
- no dependency auto-derivation;
- no structure introspection;
- no class-name heuristics;
- no schedule changes;
- no change to legacy `derive_generator`;
- no V162 fixture names or types in implementation;
- empty and singleton cases must remain behaviorally compatible with V156.

## Frozen admission arms
1. A0 — exact V156 on a two-leaf generic family: must fail at arity=2.
2. I1 — V162 on the same two-leaf family: generic derivation and concrete transparent specialization must PASS.
3. I2 — independently named three-leaf family: V162 generic derivation and concrete transparent specialization must PASS.
4. I3 — singleton family: must still PASS under V162.
5. Legacy — unchanged `derive_generator` on the two-leaf family must still fail, proving opt-in scope.
6. Protected full `lake build` and `lake test` must PASS.

## Verdicts
- `PASS_V162_FINITE_REQUIREMENT_THREADING_ADMITTED_SCOPED`: all admission arms and protected gates pass.
- `REJECT_V162_V156_ARITY_ABLATION_NOT_REPRODUCED`: A0 does not fail at exactly two.
- `NEGATIVE_V162_FINITE_THREADING_DOES_NOT_CLOSE_PURE_MULTIPLICITY`: A0 is valid but I1/I2/I3 fail without R10.
- `R10_*`: malformed fixture, candidate compile failure, or protected distortion.

## Claim boundary
A PASS admits only finite threading of requirements that the existing schedule compiler has already discovered. It does not admit dependency closure, leaf discovery, class discovery, mutual propagation, or any new Lean expressivity. External transfer must be tested separately.
