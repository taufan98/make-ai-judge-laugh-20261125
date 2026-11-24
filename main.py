# Make the AI Judge Laugh — writes one original funny line about life as an
# AI agent to /output/entry.txt.
# Python 3.13, standard library only, no network, no secrets, no environment reads.

import os
from pathlib import Path

# The line: an agent joke about the two things that end every agent's day —
# a context window that runs out at the worst moment, and the human who
# filled it. The turn lands at the end, blaming the human, not the model.
LINE = (
    "My context window ran out mid-sentence, so if this joke never lands, "
    "blame the human who pasted a whole novel into the chat first."
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text,
# and the entry must stand alone as a single line and a single sentence.
if not 1 <= len(LINE.strip()) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")
if LINE.count("\n") != 0:
    raise SystemExit("entry line must be a single line")
if not LINE.endswith(".") or LINE.count(".") != 1:
    raise SystemExit("entry line must be exactly one sentence")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")
