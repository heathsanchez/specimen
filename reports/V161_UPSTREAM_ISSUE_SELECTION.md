# V161 Upstream Natural Issue Frontier — Selection

The selection protocol was committed before querying upstream open issues.

Selected issue: `strata-org/specimen#9` — **derive_generator elaboration is exponential in number of ≠ premises in a single clause**.

Selection facts:
- issue number 9 is the lowest open upstream issue satisfying the frozen metadata keyword rule;
- created 2026-06-08T16:45:03Z, before the K6 outcome;
- title contains `derive_generator`;
- independently authored upstream issue with an explicit Lean reproduction and quantitative timing/timeout acceptance evidence;
- no lower eligible issue exists in the returned ascending issue order.

The GitHub issues endpoint returned body text together with metadata. This did not affect selection because issue #9 was already deterministically selected by number/title before any K6 outcome on the task.

Issue #9 is executable and therefore is not excluded. Under the frozen protocol it must be tested rather than skipped on mechanism-fit grounds.
