# V154 — standalone section-context old-closure separator

Frozen before any V154 outcome is inspected and before any K6 operator is constructed.

## Rival
V140/V142 established that putting an instance binder inside the `derive_mutual` submitted lambda does not make the instance available while the generated body elaborates. V147 established that ordinary standalone `derive_generator` still reproduces the fixed/generic barriers, but did not test a section-local typeclass context.

The standalone command may elaborate and install its generated command under Lean's current section context. If so, existing language may already support the desired generic conditional producer without any Specimen core change.

## No core intervention
Only exact admitted K2 and K5 are applied. No V148/V150 changes.

## Arms
S0 — ordinary generic standalone derivation with no section instance; must replay symbolic-instance failure.
S1 — inside a section with `variable (p : P) [Arbitrary p.Meta]`, invoke standalone `derive_generator` on the relation specialized to section variable `p`. Then close the section. Success means existing standalone derivation can inherit the local instance context.
S2 — same S1 construction, add the exact V152 bridge `Arbitrary P0.Meta` and require fixed `#synth ArbitrarySizedSuchThat (Box P0) ...`.
S3 — matched `abbrev P0A := ⟨Unit⟩` after S1, without an explicit bridge, require fixed synth. This tests transparent specialization separately from bridge composition.

## Interpretation
- S0 control failure to replay => R10.
- S1+S2 PASS => REJECT K6: existing standalone+section+bridge composition suffices.
- S1+S3 PASS => even stronger old closure: transparent specialization suffices after section-context derivation.
- S1 fails while intended context is exercised => section-context rival killed; missing derivation automation remains licensed by V152/V153 only if their controls pass.

Protected build/test must remain green. No result here can establish constructor development.