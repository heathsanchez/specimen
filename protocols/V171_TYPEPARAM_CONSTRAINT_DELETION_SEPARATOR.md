# V171 — type-parameter constraint deletion separator

## Purpose
Closure-before-invention separator for qualified natural issue #19. Test whether the unconditional type-parameter class binders are globally unnecessary before proposing any K8 liveness mechanism.

## Frozen intervention
Delete the automatically generated producer-class (`Plausible.Arbitrary`/`Enum`) and `DecidableEq` binders for Sort-typed parameters from constrained-producer/checker definitions and instances. Do not add replacement logic.

This is deliberately stronger than the hoped-for final rule. It is a pruning/closure test designed to reveal which constraints are actually necessary.

## Frozen fixtures
1. Natural issue #19 fixture from V170: type parameter fixed by caller; only Nat is generated. Baseline fails from overconstraint; deletion should rescue if those constraints are unnecessary there.
2. Generated-type safety: a relation whose output itself is `α`; generic producer must genuinely need `Plausible.Arbitrary α`. Blind deletion must not be accepted if this case breaks.
3. Equality safety: a relation whose body genuinely checks equality on fixed `α` values; generic checker/producer must retain whatever decidability capability is semantically required.

## Arms
A — exact admitted K2+K5+K6+K7S stack.
B — exact admitted stack + blind deletion.
C — independent deletion ablation from clean A.

## Decision
- If B rescues natural #19 and all safety/protected tests pass, reject the claim that a new liveness mechanism is required; deletion is sufficient.
- If B rescues natural #19 but breaks a frozen safety/protected case, reject blind deletion and use the first failing safety invariant to specify the next separator.
- If B does not rescue #19, reject this closure route.
- Any application/build/apparatus failure is R10 only.

No K8 is admitted by this experiment.