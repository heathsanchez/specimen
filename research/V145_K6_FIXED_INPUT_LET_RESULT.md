# V145 K6 fixed-input let — result

Run: GitHub Actions 31995127626
Artifact: 9276599542
Artifact SHA256: `0bb3bb50ea6feb7e7087adb864d1c3da0043711d18eb79a0a3f27935536a0eab`

## Frozen-arm outcome

- **B — K2+K5, no K6:** `NON_FVAR_APPLICABILITY`.
- **I — K2+K5+K6_FIXED_INPUT_LET:** intervention module compiled and the original non-fvar applicability failure disappeared, but the direct closed-index target failed at `Plausible.Arbitrary fixedInput_0_1.Meta`.
- **A — targeted K6 ablation:** restored `NON_FVAR_APPLICABILITY`.
- **G — symbolic control:** remained `Plausible.Arbitrary p_1.Meta`.
- Full protected `lake build` and `lake test` passed under I.
- The source patch contained no fixture-specific identifiers/constants checked by the frozen harness.

## Gates

- G1 baseline reproduces non-fvar: PASS
- G2 intervention fully elaborates/synthesizes: FAIL
- G3 ablation restores baseline failure: PASS
- G4 symbolic control preserved: PASS
- G5 protected surface: PASS
- G6 source-generic patch: PASS

## Verdict

`V145_K6_MOVED_RESIDUAL_NOT_ADMITTED`

K6 fixed-input let is causally effective at the applicability boundary but is **not admitted**: carrying the exact closed value as a local let-bound fvar does not by itself make the dependent projection usable by downstream typeclass synthesis. The residual moved from rejection of the closed argument to synthesis over `fixedInput_0_1.Meta`.

## Information-state update

Preserved: the original closed argument value is present as the value of a local let declaration and the scheduler receives an fvar, so the prior applicability obstruction is removed.

Still inaccessible: downstream instance synthesis behaves as though the dependent projection is symbolic. The next discriminator must test whether the let value is semantically recoverable by local reduction/zeta-specialization at the instance-demand boundary versus whether that value has already been erased from the representation consumed by instance generation.

No constructor-development claim follows from V145.
