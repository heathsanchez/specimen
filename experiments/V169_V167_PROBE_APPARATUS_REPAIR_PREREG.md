# V169 — V167 probe apparatus repair

## Status
Frozen before execution.

## Why V167 is R10
The metaprogram probe failed to elaborate before producing any liveness values because `info.levelParams.map Level.param` was parsed as a function-valued argument instead of a `List Level`. Protected build/test passed.

## Repair boundary
Preserve the exact V167 Plain/Struct raw-vs-sequential liveness probes and classifier. Change only level-list construction to an explicit expression:
`info.levelParams.map (fun n => Level.param n)`.

No production code changes.

## Verdicts
Same as V167. Any probe/setup/protected failure remains R10.
