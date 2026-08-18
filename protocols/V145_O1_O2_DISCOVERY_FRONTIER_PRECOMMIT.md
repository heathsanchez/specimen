# V145 — O1→O2 causal discovery-frontier fast pass

Status: FROZEN BEFORE EXECUTION

## Claim under test
Does admitting O1 change which next representation repair is discovered under the same residual, candidate language, verifier, controller, budget, and seeds?

O1 = V120/K2 `CARRY_IMPLICIT_FIXED_PARAMETER`.
O2 semantic law = preserve a computed application from flattening iff BOTH:
1. every free-variable dependency is relation-input-determined; and
2. that exact application occurs in the inferred dependent type of an output-position argument.
This is the behavior later implemented by V132/K5, but the discovery controller sees only anonymous candidate IDs and verifier results.

## Frozen residual
`SpecimenTest/V145O1O2Target.lean`: a minimal relation combining (a) an implicit uniform parameter carried by the inductive family and (b) a computed, input-determined expression in the dependent output type. Same bytes in all arms.

## Candidate language
Five anonymous boolean policies over `(inputDetermined, inOutputType)`:
- preserve none
- preserve on inputDetermined
- preserve on inOutputType
- preserve on conjunction
- preserve all
Candidate IDs are seed-permuted. The controller is not told which candidate is O2.

Independent semantic O2 classifier: the candidate preservation truth table must be exactly `[0,0,0,1]` on `(00,01,10,11)`.

## Arms
A: D = unmodified source, no O1.
B: D+O1 = exact V120/K2 applied before each candidate.
Ancestor ablation: any O2-equivalent candidate discovered in B is replayed under D with O1 removed.

## Frozen controller/verifier
For each seed, permute all five candidates using Python `random.Random(seed)`. Budget = 5 candidate evaluations. For each candidate: restore pristine `Specimen/DeriveConstrainedProducer.lean`; optionally apply O1; apply candidate; `lake build Specimen`; compile frozen residual. A candidate qualifies only if acquisition compiles and the protected `lake build SpecimenTest` passes. Stop at first qualified candidate. Record all attempts, order, return codes, and logs.

Seeds: `[14501,14502,14503,14504]`.

## Fast-pass success
`PASS_V145_FAST_FRONTIER_EXPANSION` iff:
- B discovers an O2-equivalent first qualified repair on >=3/4 seeds;
- A discovers O2-equivalent first qualified repair on <=1/4 seeds;
- ancestor-ablation replay of B's O2-equivalent repair under D fails acquisition or protected qualification;
- no apparatus asymmetry.

`PASS_V145_FAST_FRONTIER_ACCELERATION` iff both arms discover O2 on >=2 seeds but B median candidate evaluations to O2 <= 0.5 × A median.

`NULL_V145_O1_NO_DISCOVERY_EFFECT` for matched behavior without threshold effect.
`NULL_V145_O2_ALREADY_REACHABLE` if A reaches O2 readily (>=3/4).
`FAIL_V145_ANCESTOR_ABLATION` if B shows an O2 advantage but the same O2 candidate remains qualified after O1 removal.
`R10_V145_APPARATUS` for unequal inputs/environment, missing scripts/modules, build-system failure, or incomplete arm execution.

## Claim boundary
A pass is bounded evidence that an admitted representation repair changes the next repair reachable by this frozen discovery process. It is not open-ended self-improvement.