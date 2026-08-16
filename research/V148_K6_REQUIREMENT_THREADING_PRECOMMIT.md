# V148 — K6 dependent-requirement threading precommit

Frozen 2026-08-16 NZST under Rigorous Breakthrough Stack v1.1 before the K6 source intervention is created or executed.

## Residual and rival boundary

V139/V147 establish that a concrete fixed index cannot enter either mutual or standalone constrained-producer derivation (`NON_FVAR_APPLICABILITY`), while the corresponding ordinary variable presentation reaches a later residual: schedule compilation discovers that generating `p.Meta` requires `Plausible.Arbitrary p.Meta`, but the generated producer does not carry that requirement and elaboration fails (`SYMBOLIC_INSTANCE`).

V140/V142/V143/V144 and V147 have rejected the tested old-language parameter, instance-scoped, relation-instance, routing, wrapper, and standalone explanations. V146 let-bound syntax did not exercise the intended mechanism and is R10 only.

## K6 hypothesis

The smallest candidate K6 is **dependent requirement threading**:

> When schedule-to-code compilation discovers a typeclass requirement for an unconstrained dependent value (for example `Plausible.Arbitrary p.Meta`), retain that requirement as an explicit instance premise of the generated constrained producer instead of merely tracing it and then attempting synthesis outside the required context.

This mechanism must be source-generic. No reference to V148 fixture names, `P0`, `Unit`, or any protected task identity is permitted in the implementation.

This K6 does not initially add a special case for closed/non-fvar arguments. The fixed target is reached by lawful composition: derive the generic indexed producer with its threaded requirement, then specialize typeclass search to a closed index for which that requirement is independently satisfiable.

## Frozen intervention / controls

Exact admitted K2 and K5 are applied unchanged first.

Fixture family A:
- `V148P` with field `Meta : Type`
- `V148P0 := ⟨Unit⟩`
- dependent `V148Box p`
- relation `V148Has`

Fixture family B (held-out presentation and underlying type):
- `V148Q` with field `Carrier : Type`
- `V148Q0 := ⟨Bool⟩`
- dependent `V148Packet q`
- relation `V148Accepts`

Arms:
1. `BASE_GENERIC_A`: exact K2+K5, no K6; generic A must reproduce `SYMBOLIC_INSTANCE`.
2. `K6_GENERIC_A`: K6 enabled; generic A must derive.
3. `K6_FIXED_SPECIALIZATION_A`: after K6 generic A derivation, `#synth` the constrained producer at concrete `V148P0`.
4. `K6_GENERIC_B_HELDOUT`: K6 enabled on held-out family B; generic derivation.
5. `K6_FIXED_SPECIALIZATION_B_HELDOUT`: specialize to concrete `V148Q0`.
6. `ABLATE_REQUIREMENT_THREADING_A`: targeted ablation removes only K6 threading while retaining exact K2+K5; generic A must return to the baseline symbolic-instance failure.
7. Full protected `lake build` and `lake test` after intervention.

The intervention implementation is frozen before arm outcomes and its source hash is recorded.

## K6 admission gate

`PASS_V148_K6_ADMITTED_SCOPED` requires:

1. Baseline A reproduces `SYMBOLIC_INSTANCE` under exact K2+K5.
2. K6 generic A derives successfully.
3. Concrete A specialization synthesizes successfully with no fixture-specific K6 code.
4. Held-out generic B derives successfully.
5. Held-out concrete B specialization synthesizes successfully.
6. Targeted ablation restores the baseline symbolic-instance failure.
7. Protected build and test suite are green.
8. No K6 implementation text contains fixture names or special cases for Unit/Bool/P0/Q0.

Failure of any semantic arm is a scoped negative. Build/parser/patch/application failures that prevent the intended intervention from being exercised are R10.

## Later-frontier requirement

Even a V148 PASS admits only a scoped constructor mechanism. It does **not** establish constructor development. After admission, a separately frozen natural/later-frontier experiment must test whether K6 changes what becomes reachable or cheaper downstream, with K6 ablation reversing that later advantage.

## Claim boundary

A PASS earns the scoped name `K6_DEPENDENT_REQUIREMENT_THREADING`. It does not by itself warrant operator invention, constructor development, recursive self-improvement, or open-ended development.