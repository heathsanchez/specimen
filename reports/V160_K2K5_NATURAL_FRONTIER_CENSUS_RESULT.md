# V160 K2+K5 Natural Frontier Census — Result

Hard-evidence source: GitHub Actions run `31947564217`, job `95165897596`.

Verdict: `CORPUS_CEILING_V160_NO_K2K5_LATER_FRONTIER`.

Before baseline execution, 26 tracked `SpecimenTest/**/*.lean` files containing `derive_generator` were frozen by sorted path and SHA256. Under exact admitted K2+K5 only, `lake build SpecimenTest` returned 0 and completed 138/138 jobs. There were zero observed failures, zero eligible semantic residuals, and no selected later frontier.

Claim boundary: this is a local-corpus ceiling. It does not negate admitted K6 and does not establish constructor development. It means the current pre-existing generator test corpus contains no failing K2+K5 target on which K6 can demonstrate reachability movement.
