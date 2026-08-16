# V158 — Scope-Valid Prerequisite Placement (PRECOMMIT)

## Controller
Rigorous Breakthrough Stack v1.1. Frozen experimental facts and verifier outcomes only are hard evidence. Infrastructure/apparatus failures are R10 and imply no semantic conclusion.

## Residual inherited from V157
V157 tested provenance-preserving, missing-only promotion of unconstrained producer requirements. The intervention compiled, but primary/held-out/multi fixtures failed with unknown generated binders (`p_1`/`q_1`), and protected tests exposed analogous scope failures. Therefore provenance × missingness is insufficient: prerequisite availability is scope-relative.

## Question
Can a discovered, provenance-approved, genuinely missing unconstrained prerequisite be introduced only at a generated scope where all free-variable dependencies of that prerequisite are already bound, while leaving otherwise satisfiable/local obligations unchanged?

## Frozen intervention hypothesis
K6 candidate V158 = SCOPE_VALID_PREREQUISITE_PLACEMENT.

For each requirement discovered at an unconstrained producer site:
1. retain origin/provenance from V156;
2. ask Lean whether the requirement is already synthesizable in the creation-site local context;
3. if already synthesizable, do not promote it;
4. if missing, compute/retain the requirement expression before lossy syntax conversion and its free-variable dependencies;
5. introduce a generated prerequisite only at a scope whose bound-variable set dominates those dependencies;
6. if no valid outer scope exists, keep the requirement local rather than introducing an ill-scoped outer binder;
7. no identifier/name/test-specific filtering is permitted.

The smallest intended implementation is to preserve enough expression dependency information to rebind the same prerequisite against the actual generated parameter scope. The intervention must not special-case `p_1`, `q_1`, `Nat`, `Unit`, `Bool`, `MemNat`, STLC, Strata, Cedar, or any protected fixture.

## Baseline / intervention / ablation
Baseline is exact admitted K2+K5 without V158. Baseline must reproduce the symbolic instance residual on the primary fixture. Intervention is exact K2+K5 + V156 provenance representation + V156B checker compatibility + V158 scope-valid placement. Ablation is baseline behavior with V158 absent.

## Frozen discriminator fixtures
A. Primary projected-type family (`V153P.Meta`).
B. Source-distinct held-out projected-type family (`V153Q.Carrier`).
C. Valid two-requirement family (`V156Pair.A`, `V156Pair.B`).
D. Existing `InstanceParameterTest.lean`.
E. Existing `MutuallyRecursiveRelationsTest.lean`.
F. Existing `DependentArgs.lean`.
G. Existing `DeriveSTLCGenerator.lean`.
H. Existing `StrataLexprGen.lean`.
I. Existing `ScheduleQualityRegressionTest.lean` via the repository test/build path rather than an invalid standalone import context.

All fixture/source hashes are recorded before intervention execution.

## Admission gates
PASS_V158_SCOPE_VALID_PLACEMENT_ADMITTED_SCOPED requires ALL:
G1 baseline reproduces SYMBOLIC_INSTANCE on primary.
G2 primary intervention passes.
G3 held-out intervention passes.
G4 two-requirement intervention passes.
G5 InstanceParameter passes.
G6 mutual recursion passes.
G7 DependentArgs passes.
G8 DeriveSTLCGenerator passes.
G9 StrataLexprGen passes.
G10 ScheduleQualityRegressionTest passes through a valid repository build/test invocation.
G11 full `lake build` passes.
G12 full `lake test` passes.
G13 ablation restores the primary symbolic failure.
G14 implementation is generic and no protected-name special casing is present.

Any intervention compile/apply failure or invalid fixture invocation is R10, not a semantic negative.

## Claim boundary
Even a full PASS earns only a scoped K6 capability: scope-valid promotion/rebinding of missing unconstrained prerequisites. It does NOT establish constructor development. Constructor development still requires a frozen later-frontier experiment showing K_previous + K6 makes a later natural constructor/capability newly reachable or cheaper, with K6 ablation reversing that advantage.
