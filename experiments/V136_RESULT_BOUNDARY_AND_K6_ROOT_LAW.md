# V136 result boundary and K6 root-specialization law

Date: 2026-08-17

## Evidence consumed

V134 clean discriminator established that a fixed root with `P0.Meta = Unit` still reaches `Arbitrary a.Meta` under exact admitted K2+K5.

V135 post-unification trace established that the concrete root value is absent by final unification state: the root parameter is represented only through aliases ending in a runtime input marked `Fixed`; no equality to the original `P0` remains.

V136 routing separator compared identical fixed roots with `specimen.autoDeriveDeps` ON/OFF.

Observed:

- AUTO_ON: accepted the fixed root, then failed at `Arbitrary a_1.Meta`.
- AUTO_OFF: failed earlier with `P0 is expected to be a variable`.

Therefore the machine label `NULL_V136_COMMON_PATH_SPECIALIZATION_LOSS` is NOT admissible: the two arms did not reach a matched semantic stage.

Formal V136 verdict: `R10_V136_ASYMMETRIC_ROUTING_CAPABILITY`.

## Source-localized obstruction

The auto-derive root path reduces each user spec to `(inductiveName, outputIndices, globalName, deriveSort)` and calls `deriveBestInductiveSchedule` from that key. `deriveBestInductiveSchedule` reconstructs fresh generic variables for every inductive argument from the inductive type signature. Thus a syntactically fixed user argument is not represented in root schedule derivation.

The fallback path re-elaborates the original user term but rejects non-output non-variable arguments. This is a separate routing limitation and is not evidence about the auto-derive semantic residual.

## Frozen K6 law

`K6_ROOT_SPECIALIZATION_PRESERVATION`:

For a user-supplied root spec, if a non-output inductive argument is syntactically fixed by the root term, preserve that fixed argument through root schedule derivation and code emission rather than replacing it with a fresh runtime input.

Scope restrictions:

1. Root specs only.
2. Do not change recursive/transitive dependency `SpecKey` identity.
3. Do not add typeclass instances.
4. Do not special-case `Meta`, `Unit`, `Bool`, or any V134/V135/V136 identifier.
5. Runtime lambda-bound inputs remain runtime inputs.
6. Output positions remain outputs.
7. Generic-root behavior must remain unchanged.
8. A fixed root whose specialized dependent type lacks an instance must still fail.

## Earning gates

K6 is admitted only if all pass under exact K2+K5:

- Acquisition: fixed `Unit` root changes FAIL -> PASS.
- Source-distinct transfer: structurally equivalent fixed `Bool` projection changes FAIL -> PASS without modification.
- Negative control: fixed projection to a genuinely unsynthesizable type remains FAIL.
- Generic control: generic parameterized root behavior is unchanged.
- Protected suite: full protected Specimen suite passes.
- Ablation: removing K6 restores the V134 fixed-root failure.

A target-only success is insufficient.
