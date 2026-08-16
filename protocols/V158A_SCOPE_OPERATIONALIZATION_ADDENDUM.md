# V158A — Scope Operationalization Addendum (frozen before execution)

V157 established that creation-site `synthInstance?` is not a lawful availability discriminator when the requirement syntax refers to a generated binder that does not yet exist in that elaboration scope. V158 therefore MUST NOT repeat that apparatus.

For this bounded separator, `scope-valid promotable requirement` is operationalized structurally:

- origin must be `.unconstrained` (V156 provenance rule);
- the requirement syntax must depend on at least one generated non-output/input binder of the derived producer;
- only such dependent requirements are threaded into the generated outer and inner scopes;
- unconstrained requirements with no dependency on generated producer inputs are left to existing use-site synthesis behavior and are not promoted;
- constrained-producer requirements remain unpromoted;
- no type/test/identifier-specific whitelist or blacklist is permitted.

This is deliberately narrower than a universal missing-instance promotion system. A PASS earns only `K6_SCOPE_DEPENDENT_REQUIREMENT_PROMOTION`: lawful preservation/rebinding of dependent unconstrained prerequisites. Closed missing prerequisites are outside this K6 scope and remain a separate residual.

The scientific gates in V158 remain unchanged: primary, held-out, multi, protected source-distinct separators, schedule-quality regression, full build/test, and ablation must all pass.
