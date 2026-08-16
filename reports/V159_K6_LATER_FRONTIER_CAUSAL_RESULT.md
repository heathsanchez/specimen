# V159 K6 Later-Frontier Causal Dependence — Result

Hard-evidence source: GitHub Actions run `31947253390`, job `95165123739`.

Frozen verdict: `NULL_V159_NO_REACHABILITY_MOVEMENT`.

The precommitted natural later-frontier target `SpecimenTest.StrataLexprGen` was already reachable under exact admitted K2+K5 in the current substrate:
- A (K2+K5): PASS, rc=0, wall≈46.92s
- B (K2+K5+admitted K6): PASS, rc=0, wall≈48.19s
- C (independent K6 ablation, K2+K5): PASS, rc=0, wall≈44.28s
- B protected `lake build`: 0
- B protected `lake test`: 0

Therefore the frozen reachability frontier did not exist and K6 cannot be credited with moving it. Wall-clock differences do not establish capability and do not support an efficiency claim here.

Claim boundary: K6 remains admitted from V158, but constructor development remains unestablished by V159. This is a corpus/frontier-ceiling null for this target, not evidence that K6 can never move a later frontier.
