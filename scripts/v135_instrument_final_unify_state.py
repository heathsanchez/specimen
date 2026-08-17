from pathlib import Path

path = Path("Specimen/DeriveConstrainedProducer.lean")
text = path.read_text()
old = '''      let finalState ← get

      -- Takes the `patterns` and `equalities` fields from `UnifyState`'''
new = '''      let finalState ← get
      trace[plausible.deriving.results] m!"V135_FINAL_UNIFY_STATE {repr finalState}"

      -- Takes the `patterns` and `equalities` fields from `UnifyState`'''
if old not in text:
    raise SystemExit("V135 instrumentation anchor not found")
if text.count(old) != 1:
    raise SystemExit(f"V135 instrumentation anchor count != 1: {text.count(old)}")
path.write_text(text.replace(old, new, 1))
