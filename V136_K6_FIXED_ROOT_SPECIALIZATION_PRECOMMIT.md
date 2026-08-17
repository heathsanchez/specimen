# V136 — K6: Preserve Fixed Root Specialization

## Status
Frozen before implementation.

## Primary evidence inherited
- K2 and K5 are the only admitted constructor-state interventions.
- V134 cleanly established that a fixed root specialization `P0.Meta ≡ Unit` still degrades to a symbolic `Arbitrary a.Meta` obligation under exact K2+K5.
- V135 post-unification trace showed the fixed term itself is already absent from `finalState`: `p -> u_0 -> a_1`, with `a_1 : Fixed`; no state entry identifies `a_1` with `P0`.
- The same V135 case has one base constructor and zero recursive relation dependencies, therefore `SpecKey`/recursive dependency memoization cannot be the immediate cause of this failure.
- `derive_mutual` currently reduces each user root spec to `(inductiveName, outputIndices, globalName, deriveSort)` and later reconstructs generic inputs from the inductive signature; concrete fixed non-output arguments are not retained in that root metadata.

## K6 hypothesis
K6 = PRESERVE_FIXED_ROOT_SPECIALIZATION.

A root spec supplied by the user must retain lawful compile-time fixed non-output argument expressions through schedule construction instead of replacing those positions with fresh generic runtime inputs.

This is a representation-preservation rule, not a new instance rule and not a target-specific patch.

## Forbidden interventions
K6 may not:
- add `Arbitrary`, `Enum`, or other typeclass instances;
- special-case `Meta`, `Unit`, `Bool`, V134/V135/V136 names, or Strata names;
- widen or retry typeclass search;
- disable auto-derive;
- bypass schedule generation;
- alter K2 or K5 semantics;
- use the expected test result to select which fixed arguments are preserved.

## Minimal intervention target
Extend root-spec metadata only as far as necessary to retain fixed non-output argument expressions from the elaborated user spec and use them when constructing the root schedule problem.

Positions that are genuine lambda-bound inputs remain runtime inputs. Existential outputs remain outputs. Only non-output arguments that are already closed/fixed in the elaborated user root spec are eligible for preservation.

## Frozen test family
1. ACQUISITION / Unit
   - exact V134 fixed family: `P0.Meta := Unit`.
   - K2+K5 baseline must fail with symbolic `Arbitrary a.Meta`.
   - K2+K5+K6 must derive successfully without adding an instance.

2. SOURCE-DISTINCT TRANSFER / Bool
   - separate names and family; fixed projection is `Bool`.
   - baseline K2+K5 must exhibit the same specialization-loss pattern or fail at the equivalent symbolic obligation.
   - K6 must derive successfully.

3. NEGATIVE CONTROL / unsynthesizable fixed projection
   - separate names and family; fixed projection is `Nat -> Nat`.
   - K6 must not manufacture capability. If no lawful `Arbitrary (Nat -> Nat)` exists in the frozen environment, the arm must remain a genuine instance-synthesis failure after specialization.

4. GENERIC CONTROL
   - generic `p` version remains generic and must not be silently specialized.

5. PROTECTED SUITE
   - full historical protected Specimen suite used for K5 admission must remain green (137/137 threshold inherited from V132 evidence package, or exact current reconstruction of that frozen protected set).

6. ABLATION
   - remove K6 while retaining K2+K5: Unit and Bool acquisition/transfer must return to the pre-K6 specialization-loss failure.

## Earning criteria
K6 is ADMITTED only if all are true:
- Unit baseline fails and K6 succeeds;
- Bool source-distinct transfer succeeds with K6;
- generic control is not incorrectly specialized;
- unsynthesizable negative remains unsynthesizable;
- protected suite remains fully green;
- K6 ablation restores the relevant failures;
- implementation is representation-generic and contains no frozen target names/types.

Anything less is diagnostic/causal evidence only, not admission.

## Developmental crown-jewel boundary
Even if K6 is admitted, constructor development is not yet called compounding. A later experiment must show that the admitted K6 state changes a subsequent discovery frontier, with ancestor ablation moving that later frontier backward.