# V159A — V158 Eligibility Record

This records an eligibility fact after the V159 scientific target/outcomes were already frozen in `V159_K6_LATER_FRONTIER_CAUSAL_PRECOMMIT.md`; it does not change V159 arms or gates.

V158 GitHub Actions run: `31947018740`; job: `95164546088`.
Frozen V158 verdict: `PASS_V158_SCOPE_VALID_PLACEMENT_ADMITTED_SCOPED`.
Earned scoped capability: `K6_SCOPE_DEPENDENT_REQUIREMENT_PROMOTION`.
All V158 admission gates G1–G14 were true, including full protected `lake build = 0`, `lake test = 0`, primary/held-out/multi transfer, historical dependent cases, schedule-quality regression, and ablation.

Admitted K6 implementation stack for V159 B arm:
- `scripts/v156_apply_requirement_provenance_promotion.py`
- `scripts/v156b_apply_checker_consumer_compat.py`
- `scripts/v158_apply_scope_dependent_promotion.py`

V158 execution-time SHA256 for the K6 scripts:
- v156 provenance: `17074519a184a741e74466aa81604e809a14478abc15568f845395c788664d5c`
- v156b compatibility: `8f3f7869fd775a8b6390e9d1483faa6a5d63bb4f52722b85f8374f17d1befd78`
- v158 scope rule: `d88527a37a480313ac01a4730832f10f7f7ca6273c338e0523eacddea3200826`

V159 is therefore scientifically eligible to execute.
