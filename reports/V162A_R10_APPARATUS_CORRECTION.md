# V162A — R10 apparatus correction

The original V162 workflow did not execute the frozen upstream issue #9 scientific task. In all A/B/C arms it removed `.lake/build` and immediately invoked `lake env lean fixtures/V162_UPSTREAM_ISSUE9_REPRO.lean`, producing `unknown module prefix 'Specimen'` in about 0.5 s.

Therefore the emitted `NEGATIVE_V162_K6_NO_EFFECT_ON_ISSUE9` verdict is invalid and is superseded by:

`R10_V162_TASK_NEVER_EXECUTED`

No scientific inference about K6 or issue #9 is licensed from that run.

The only allowed repair in V162B is apparatus: after applying the exact same frozen arm mutation, rebuild the local `Specimen` library before invoking the exact same frozen reproduction under the same 120 s task cap. The fixture, K2/K5 scripts, admitted K6 scripts and scientific decision rule are unchanged. A further apparatus check rejects any arm whose log contains `unknown module prefix 'Specimen'`.
