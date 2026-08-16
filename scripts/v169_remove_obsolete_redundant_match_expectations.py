from pathlib import Path
import re

TARGETS = {
    Path('SpecimenTest/DeriveArbitrarySuchThat/Syntax.lean'): 1,
    Path('SpecimenTest/DeriveArbitrarySuchThat/FunctionCallsTest.lean'): 1,
    Path('SpecimenTest/DeriveArbitrarySuchThat/NEqGenerator.lean'): 5,
}

block_re = re.compile(
    r'/\--(?P<body>.*?)-/\s*\n'
    r'#guard_msgs\(error, drop info(?P<suffix>[^)]*)\) in',
    re.S,
)
redundant_re = re.compile(
    r'error:\s*Redundant alternative:\s*Any expression matching\s*'
    r'_\s*will match one of the preceding alternatives',
    re.S,
)

def rewrite(path: Path, expected: int) -> None:
    text = path.read_text()
    touched = 0

    def repl(m: re.Match) -> str:
        nonlocal touched
        body = m.group('body')
        if 'Redundant alternative' not in body:
            return m.group(0)
        residual = redundant_re.sub('', body)
        residual = residual.replace('---', '')
        if residual.strip():
            return m.group(0)
        touched += 1
        return f"#guard_msgs(drop info{m.group('suffix')}) in"

    out = block_re.sub(repl, text)
    if touched != expected:
        raise SystemExit(f'V169_EXPECTATION_COUNT_MISMATCH:{path}:{touched}!={expected}')
    path.write_text(out)

for path, expected in TARGETS.items():
    rewrite(path, expected)

# Scope audit: this script is test-maintenance only.
for path in TARGETS:
    if not str(path).startswith('SpecimenTest/'):
        raise SystemExit(f'V169_NONTEST_TARGET:{path}')

print('V169_OBSOLETE_REDUNDANT_MATCH_EXPECTATIONS_REMOVED')
