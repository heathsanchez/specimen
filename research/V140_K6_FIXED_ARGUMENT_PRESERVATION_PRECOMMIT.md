# V140 — K6 fixed-argument preservation admission precommit

Date frozen: 2026-08-16 NZST

## Licensed residual

V139 prospectively established `PASS_V139_FIXED_INDEX_APPLICABILITY_BARRIER`: under exact admitted K2+K5, a generic family variable reaches the later symbolic `Arbitrary p.Meta` stage, while the same family fixed to concrete `P0` is rejected earlier because `P0 is expected to be a variable`.

V139 licenses one narrow successor mechanism only.

## K6 mechanism frozen before execution

`K6_PRESERVE_CONCRETE_FIXED_ARGUMENT`:

When a non-output inductive/family argument in the user target is not already a free variable, do not replace it by an unconstrained synthetic unknown. Instead introduce a local let-bound free variable whose value is exactly the original elaborated argument expression, and route that local through the existing downstream derivation machinery.

Thus downstream code receives the FVar representation it currently requires while definitional equality to the original fixed expression is preserved.

K6 must be generic: no `V139`, `V134`, `Strata`, `Meta`, `P0`, or target-specific names/constructors may appear in the source patch.

Exact admitted K2 and K5 remain unchanged and are applied before K6.

## Primary acquisition

Use the V139/V134 controlled family:

- `P` with `Meta : Type`
- `P0 := ⟨Unit⟩`
- `Box (p : P)` carrying `p.Meta`
- `Has`

Primary DIRECT target:

`derive_mutual (fun (_ : Unit) => ∃ b : Box P0, Has b)`

## Frozen gates

K1 — K2+K5 without K6 reproduces `NON_FVAR_APPLICABILITY` on the DIRECT target.

K2 — K2+K5+K6 compiles the derivation module.

K3 — K2+K5+K6 removes the `expected to be a variable` obstruction on DIRECT.

K4 — scientific discriminator after K6 is interpreted without rescue:
- if DIRECT passes, specialization-before-instance-synthesis succeeds in this minimal fixed case;
- if DIRECT reaches a symbolic `Arbitrary ...Meta` obligation despite definitional equality to `P0`, the deeper specialization barrier is isolated;
- any unrelated failure is a new residual and does not count as K6 scientific PASS.

K5 — generic variable control remains a genuine generic problem and must not be silently specialized by K6.

K6 — full repository `lake build` and `lake test` pass under K2+K5+K6.

K7 — causal ablation removes only K6 while retaining exact K2+K5 and restores the DIRECT `NON_FVAR_APPLICABILITY` failure.

K8 — patch audit contains no target-specific identifiers and changes only representation/access handling needed for fixed non-output argument preservation.

## Verdicts

`PASS_V140_K6_AND_NULL_SPECIALIZATION_BARRIER` iff K1-K3 and K5-K8 hold and DIRECT passes under K6. This means the V133 candidate explanation 'specialization is not propagated before instance synthesis' is null in the controlled minimal case; the real Strata residual is richer.

`PASS_V140_K6_AND_ISOLATE_SPECIALIZATION_BARRIER` iff K1-K3 and K5-K8 hold and DIRECT reaches the frozen symbolic-instance class under K6. This admits K6 for the current protected Specimen scope and separately isolates the deeper specialization barrier.

`NULL_V140_K6_NO_CAUSAL_EFFECT` if K6 does not remove the fixed-index applicability failure.

`INVALID_V140_PROTECTED_REGRESSION` if acquisition improves but protected build/test fails.

Other failures are residuals and must be named rather than post-hoc rescued.

## Q9 boundary

Neither successful K6 admission nor a minimal fixed-case null alone establishes constructor growth. Q9 constructor growth is closed only if an admitted mechanism causally expands constructibility beyond exact K2+K5, survives protected replay and ablation, and is then exercised on a separately frozen target requiring the newly admitted capability. V140 can satisfy the mechanism-admission half; any stronger developmental constructor-growth claim must be tied to the frozen causal result, not inferred from green CI.

## Claim boundary

This is a bounded admission test in one pinned Lean metaprogramming system. It cannot establish unrestricted/open-ended self-modification or universal dependent-type support.