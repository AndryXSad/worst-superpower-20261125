"""Worst Superpower — make.fun entry (program/v1).

Design: the entry is a single fixed one-liner, chosen by a local pairwise
round-robin tournament over 18 fresh candidate lines, scored on the judge
brief's five criteria in order (genuinely useless, funny to picture in use,
unexpected, tight and specific, clear on one reading). The winner took all
17 of its pairings:

    I can see ten seconds into the future, but only of a TV show I have
    already finished.

Why it wins: the power is genuinely useless (foresight of something already
watched), the image is instant (a hero squinting at a finale they know by
heart), it is not one of the banned cliches (no slow flight, no
invisible-when-unwatched), and the concrete detail — ten seconds, already
finished — fixes it in the world in a single reading.

The program writes exactly that line, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt). Stdlib only,
no input, no randomness, no network: two runs produce byte-identical output.
"""

import os
from pathlib import Path

LINE = "I can see ten seconds into the future, but only of a TV show I have already finished."


def main() -> None:
    # Guard the gate: the line must stay within the 1-140 character rule.
    if not (1 <= len(LINE) <= 140 and LINE.strip()):
        raise ValueError("entry line violates the 1-140 character gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
