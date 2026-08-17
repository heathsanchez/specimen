from pathlib import Path

path = Path("Specimen/MExp.lean")
text = path.read_text()

old = '''def unconstrainedProducer (prodSort : ProducerSort) (ty : TSyntax `term) : CompileScheduleM MExp := do
  let typeClassName :=
'''
new = '''def unconstrainedProducer (prodSort : ProducerSort) (ty : TSyntax `term) : CompileScheduleM MExp := do
  -- V146R trace-only diagnostic: record the reconstructed demand and the
  -- user names that are actually available in the current local context.
  let localCtx ← getLCtx
  let namesInContext :=
    (fun e => getUserNameInContext! localCtx e.fvarId!) <$> localCtx.getFVars
  trace[plausible.deriving.arbitrary] m!"V146R_DEMAND={ty}; V146R_LCTX_NAMES={namesInContext}"
  let typeClassName :=
'''
count = text.count(old)
if count != 1:
    raise SystemExit(f"V146R expected one unconstrainedProducer anchor, found {count}")
text = text.replace(old, new, 1)
path.write_text(text)
print("V146R trace-only instance-demand context probe applied")
