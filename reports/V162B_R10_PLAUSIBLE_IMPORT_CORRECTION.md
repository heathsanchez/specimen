# V162B — R10 Plausible import correction

V162B fixed the local `Specimen` import but still did not execute the frozen issue #9 task. All three arms failed in under one second because `fixtures/V162_UPSTREAM_ISSUE9_REPRO.lean` imports the top-level `Plausible` module and the corresponding `Plausible.olean` had not been built.

Therefore `NEGATIVE_V162B_K6_NO_EFFECT_ON_ISSUE9` is invalid and superseded by:

`R10_V162B_TASK_NEVER_EXECUTED_MISSING_PLAUSIBLE_OLEAN`

V162C changes apparatus only. Before any scientific arm is spent it must explicitly build both `Plausible` and `Specimen`, then pass an import-only probe containing `import Plausible` and `import Specimen.DeriveConstrainedProducer`. The frozen issue #9 fixture, K2/K5 scripts, admitted K6 scripts, 120 s cap and A/B/C decision rule remain unchanged.
