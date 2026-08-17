# V137 — Specialized-root oracle

Purpose: test whether preserving root specialization is sufficient to remove the V134/V135 instance obstruction without changing scheduling or instance search.

Frozen before execution.

## Matched semantic family

Define a parameter record `P` with field `Meta : Type`, fixed value `P0 := ⟨Unit⟩`, family `Box (p : P)` with constructor payload `p.Meta`, and generic relation `Has {p}` over `Box p`.

Arm ORIGINAL_FIXED uses the existing form:

`derive_mutual (fun n => ∃ b : Box P0, @Has P0 b n)`

Arm SPECIALIZED_RELATION uses an explicitly specialized inductive relation whose domain is `Box P0` and whose constructor payload is `Unit`, then derives:

`derive_mutual (fun n => ∃ b : Box P0, HasP0 b n)`

Both run under exact admitted K2+K5, autoDeriveDeps=true, multiOutput=true.

## Interpretation

- ORIGINAL_FIXED fails with `Arbitrary _.Meta` and SPECIALIZED_RELATION passes => `PASS_V137_ROOT_SPECIALIZATION_SUFFICIENT_ORACLE`. This does not admit K6; it establishes that compile-time specialization itself is sufficient and licenses implementing a generic root-specialization-preservation transform.
- Both fail => `NULL_V137_SPECIALIZATION_NOT_SUFFICIENT`; revisit scheduler/instance mechanism.
- ORIGINAL_FIXED passes => R10, because V134/V135 no longer reproduce.
- Any unrelated parser/type error => R10.

No production source is changed by V137.
