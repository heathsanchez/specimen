# V161 — Upstream Natural Issue Frontier Census (PRECOMMIT)

Controller: Rigorous Breakthrough Stack v1.1.

Purpose: V160 established a local test-corpus ceiling. Search once in the pre-existing upstream `strata-org/specimen` open-issue corpus for a natural, independently authored later task without choosing by K6 outcome.

## Frozen selection
Query upstream open issues, excluding pull requests, ordered by ascending issue number. Only issues created before 2026-08-16T00:00:00Z are eligible (pre-K6 outcome).

Metadata eligibility requires title OR labels to contain at least one of: `derive`, `generator`, `arbitrary`, `instance`, `typeclass`, `dependent`, `parameter`, `enumerator`, `checker` (case-insensitive).

Freeze the complete returned issue metadata set and the eligible ordered list before inspecting the selected issue body or attempting execution. Select the lowest issue number among eligible issues.

After selection only, inspect its body and determine executability using frozen rules:
- task must concern Specimen derivation/generation/checking behavior rather than docs/administration;
- there must be an external verifier in the repo (build/test/reproduction) or an unambiguous executable acceptance condition from the issue;
- do not author a new target merely to fit K6;
- if the selected issue is non-executable or already resolved in the pinned substrate, advance to the next eligible issue for the same reason only, recording the exclusion; never skip because K6 does not help.

K6 MUST NOT be applied until an executable task is frozen and exact K2+K5 baseline outcome is recorded.

If no eligible executable issue exists, verdict `CORPUS_CEILING_V161_NO_UPSTREAM_NATURAL_FRONTIER` and stop constructor-development reachability search.

If one exists, a separate baseline/K6/ablation run is required. This census alone cannot establish constructor development.
