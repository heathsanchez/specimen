# V166 result — K7 not admitted

Canonical status: **not admitted**.

Observed scientific fixture results:
- A natural issue #12: failed with `redundantMatchAlt` as frozen.
- A held-out single-constructor inductive: failed with `redundantMatchAlt` as frozen.
- A multi-constructor safety: passed.
- B + K7 natural: passed.
- B + K7 held-out: passed.
- B + K7 multi-constructor safety: passed.

Protected-suite result:
- Full `lake test` failed with missing-pattern cases in existing tests, including `SpecimenTest/CedarExample/CedarCheckerGenerators.lean`.
- The counterexample demonstrates that checking only whether the outer constructor is unique is too broad: a sole outer constructor can contain nested restrictive constructor/literal subpatterns.
- C ablation did not run because B did not clear the protected gate.

Interpretation: the target rescue and held-out transfer were real, but the K7 abstraction was insufficiently precise. The next residual is complete-pattern irrefutability, not outer-inductive constructor count.
