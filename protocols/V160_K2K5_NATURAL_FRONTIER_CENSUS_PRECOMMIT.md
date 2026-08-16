# V160 — Deterministic K2+K5 Natural Frontier Census (PRECOMMIT)

Controller: Rigorous Breakthrough Stack v1.1.

Purpose: after V159 was NULL because the precommitted Strata target was already solved by K2+K5, determine whether the existing pre-K6 Specimen test corpus contains any genuine later baseline frontier. Do not select a target using K6 outcomes.

Corpus: all tracked `SpecimenTest/**/*.lean` files on this branch that contain the literal token `derive_generator`, frozen by sorted path and SHA256 before baseline execution.

Baseline: exact admitted K2+K5 only. K6 scripts MUST NOT be applied during census.

Procedure:
1. Freeze sorted candidate manifest and file hashes before baseline results.
2. Apply exact K2+K5.
3. Run full `lake build SpecimenTest` and record failed modules.
4. From failing modules, retain only candidates in the frozen manifest whose failure is semantic (`failed to synthesize instance of type class`, `expected to be a variable`, or `unknown free variable`), excluding parser/build-tool/network failures as R10.
5. If eligible failures exist, select the lexicographically first path. Rebuild that module independently under K2+K5 to reproduce before any K6 exposure.
6. If none exist, verdict `CORPUS_CEILING_V160_NO_K2K5_LATER_FRONTIER` and stop; do not manufacture a task.

This census does not establish constructor development. If a target is selected, a separate frozen K6 intervention/ablation experiment is required.
