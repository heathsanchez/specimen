# V138 — K6 implementation design: fixed root binders

Status: frozen after V137 PASS, before production implementation.

## Evidence
V137 produced ORIGINAL_RC=1 and SPECIALIZED_RC=0 under exact K2+K5. Explicitly baking the fixed root specialization into an extensionally matched relation is sufficient to remove the `Arbitrary a.Meta` obstruction.

## Implementation object
Introduce a root-only distinction between:

- runtime input positions: represented by ordinary local declarations / generated function parameters;
- fixed root positions: represented by a local name whose value is the preserved elaborated root expression, and omitted from the generated instance's runtime parameter list.

Schedules may continue to refer to the local name. The name is bound to the fixed value, so dependent expressions such as `p.Meta` may reduce using the preserved value.

## Scope
Initial implementation is deliberately limited to user-supplied root specs. Recursive/transitive dependency `SpecKey` identity remains unchanged.

No new typeclass instances, no type-specific rewrites, no widening of synthesis, no bypass of schedule generation.

## First implementation gate
Use the already-frozen zero-recursive-dependency families:

1. Unit fixed projection: baseline K2+K5 fails; K6 must pass.
2. Bool fixed projection: source-distinct transfer must pass.
3. Generic root remains generic.
4. Nat -> Nat fixed projection must remain unsynthesizable.

Only if those pass do we run the inherited protected suite and K6 ablation.

## Rejection rule
If fixed local binding alone does not make Unit and Bool pass, do not broaden K6 post hoc. Return to residual analysis.