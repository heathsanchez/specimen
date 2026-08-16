# V164 — R10 apparatus correction

The frozen upstream checkout and fixture identity checks passed, but the workflow had not installed Lean/Elan before invoking `lake`, so the exact upstream task never executed.

Supersede the V164 run with:

`R10_V164_TASK_NEVER_EXECUTED_NO_LEAN_TOOLCHAIN`

V164B changes apparatus only by installing the repository's frozen Lean toolchain before cloning/running upstream. Upstream SHA `c991edb5e2a7d836bd4e42cb3a02897e0c2ea788`, fixture bytes, 120-second cap, and outcome classification are unchanged.
