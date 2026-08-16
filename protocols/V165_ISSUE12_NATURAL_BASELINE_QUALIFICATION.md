# V165 — Upstream issue #12 natural baseline qualification

## Purpose
Qualify the next deterministic pre-existing upstream issue as a natural later frontier before proposing or implementing K7.

Issue #9 was disqualified under V164B because its exact published reproduction fails earlier on an unstated `DecOpt` prerequisite even on frozen upstream itself. Under the already-frozen upstream-issue ordering rule, the next eligible issue by number is #12.

## Frozen natural target
Upstream issue `strata-org/specimen#12`, independently authored before K7.

Use the published reproduction verbatim in substance:

```lean
import Specimen.DeriveChecker
import Specimen.DecOpt
import Plausible

structure S where
  a : UInt8
  b : UInt8
deriving Plausible.Arbitrary

inductive R : S → Prop where
| mk : x = 1 → R ⟨x, b⟩

derive_checker (fun s => R s)
```

No source or fixture change is permitted after this precommit.

## Frozen baseline
Apply the exact admitted prior stack only:

- K2 apparatus/intervention script: `v120_apply_binder_aware_fixed_parameter.py`
- K5 apparatus/intervention script: `v132_apply_output_dependent_input_determined.py`
- K6 admitted stack: `v156_apply_requirement_provenance_promotion.py`, `v156b_apply_checker_consumer_compat.py`, `v158_apply_scope_dependent_promotion.py`

No K7 logic is permitted.

## Eligibility
PASS qualification requires:
1. imports/build apparatus is valid;
2. exact issue fixture fails under the admitted prior stack;
3. failure contains `redundantMatchAlt` / `Redundant alternative` for the generated wildcard match arm;
4. failure is not an unrelated missing instance, import, timeout, or source-application error.

If the exact fixture passes, verdict `NULL_V165_ISSUE12_ALREADY_SOLVED` and do not spend K7 here.
If it fails differently, classify the exact residual and do not retrofit the target.
Apparatus failure is R10 only.

## Claim boundary
V165 only qualifies a natural frontier. It does not admit K7 or establish constructor development.
