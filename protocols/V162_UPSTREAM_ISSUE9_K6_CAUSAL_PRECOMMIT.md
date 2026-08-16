# V162 — Upstream Issue #9 K6 Causal Test (PRECOMMIT)

Controller: Rigorous Breakthrough Stack v1.1.

Natural task: deterministic V161 selection `strata-org/specimen#9`, independently authored before K6. Use its published 10-inequality `derive_generator` reproduction.

Arms:
A: exact K2+K5.
B: exact K2+K5 + admitted byte-checked K6 stack (V156 provenance + V156B compatibility + V158 scope-dependent promotion).
C: independent K6 ablation, exact K2+K5 rebuilt after B.

Environment fixed: repository toolchain, same fixture, same runner class, project build output cleared before each arm; dependency packages may be reused. Each fixture invocation has a 120-second external timeout. Timeout is a valid task outcome because the upstream issue itself defines severe elaboration time/timeout as the bug; setup/build/provider failures are R10.

Primary outcome: whether the 10-conjunct generator elaborates successfully within 120 seconds. Secondary: wall-clock for completed runs. No claim from timing differences unless both complete and the difference is large/reproduced; a single run per arm is only descriptive.

Frozen reachability/efficiency classification:
- If A times out/fails semantically, B completes, C restores timeout/failure, and B protected build/test pass: scoped later-frontier causal PASS.
- If A/B/C have the same completion class: NEGATIVE/NULL for K6 on this natural task; no constructor-development credit.
- If A and B both complete, no reachability movement; timing alone is descriptive unless separately replicated.
- R10 only for apparatus failures.

K6 must remain byte-identical to V158 admission and contain no issue-9-specific logic.
Claim boundary: even a PASS would be one additional natural later-frontier transition, not recursive/open-ended development.
