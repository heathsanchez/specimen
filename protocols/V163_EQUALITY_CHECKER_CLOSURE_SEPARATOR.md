# V163 — Equality checker closure separator (diagnostic precommit)

## Purpose
Discriminate the next mechanism after the valid V162C residual. This is a diagnostic separator, not constructor-development evidence.

V162C reached the frozen upstream issue #9 task and failed because emitted checks require `DecOpt (op = E.X)` after `op` is locally generated. The published finite type `E` has `Plausible.Arbitrary` but no declared `DecidableEq`.

## Frozen question
Can the existing Specimen checker derivation structurally construct a `DecOpt (a = b)` capability for a finite inductive `E` without any declared `DecidableEq E`?

## Fixture
Define a fresh finite three-constructor inductive `V163Atom`, derive only `Plausible.Arbitrary`, and invoke:

`derive_checker (fun a b => Eq a b)`

Then require `#synth DecOpt (V163Atom.A = V163Atom.B)`.

No `DecidableEq` derivation or local instance is permitted.

## Outcomes
- PASS: derived equality checker capability exists without `DecidableEq`; next K7 hypothesis is checker-dependency closure/reuse at emitted `.Check` sites.
- FAIL with missing DecOpt/DecidableEq or inability to derive Eq checker: next K7 requires a new structural decidability mechanism; do not misclassify as closure.
- Infrastructure failure: R10 only.

## Claim boundary
Diagnostic mechanism separator only. It cannot establish natural-task reachability, K7 admission, constructor development, or recursive improvement.
