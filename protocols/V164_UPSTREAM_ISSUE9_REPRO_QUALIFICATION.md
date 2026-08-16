# V164 — Upstream issue #9 reproduction qualification

## Purpose
Determine whether the exact published issue #9 reproduction reaches its reported elaboration-performance pathology on upstream Specimen independently of the K2/K5/K6 lineage.

## Frozen upstream
Repository: `strata-org/specimen`
Commit: `c991edb5e2a7d836bd4e42cb3a02897e0c2ea788` (upstream main HEAD frozen before execution).

## Frozen task
Use `fixtures/V162_UPSTREAM_ISSUE9_REPRO.lean` byte-for-byte unchanged. It defines `E` deriving only `Plausible.Arbitrary`, defines `Excludes` with ten inequality premises, then invokes `derive_checker` and `derive_generator`.

## Apparatus
Clone upstream, checkout the frozen SHA, build required upstream modules, copy only the frozen reproduction file into the checkout, and execute it with `lake env lean` under 120 seconds. No K scripts or source changes are applied.

## Outcomes
- REPRODUCED_PERFORMANCE_FRONTIER: task passes semantic/typeclass elaboration and reaches timeout or substantial reported elaboration slowdown.
- UPSTREAM_SEMANTIC_PREREQUISITE_FAILURE: exact upstream task fails first on missing `DecOpt`/`Decidable` prerequisite or another verifier-confirmed semantic prerequisite.
- PASS_FAST: exact task succeeds without the reported pathology on this upstream SHA.
- R10: clone/build/import/apparatus failure only.

## Claim boundary
Qualification only. No K7 admission or constructor-development claim. If upstream itself hits the same missing prerequisite, issue #9 is not a clean natural performance frontier under the frozen current upstream environment and must not be repaired by silently modifying its published fixture.
