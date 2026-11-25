#!/usr/bin/env python3
"""corridance — the entry program for make.fun's "Invent a Word We Need".

Writes the one-line entry (a newly coined word plus its definition,
95 characters, under the 140-character gate) to ``<output>/entry.txt``
and prints it. Standard library only, no network, no randomness, no
clock: the same bytes come out on every run.

The grader runs this as ``python3 -P -s /bot/main.py`` and reads
``/output/entry.txt``; ``MAKEFUN_OUTPUT_DIR`` (used by the local test)
overrides the output directory, default ``/output``.
"""

import os
import sys

# The entry, byte-identical to entry.txt in this repository.
# corridors + dance, with the middle elided: the word English never
# grew for the mirrored sidestep two people do in a hallway.
ENTRY = "corridance \u2014 the mirrored sidestep two people do in a hallway, each dodging the same way twice."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = "entry.txt"


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 140):
        raise SystemExit("entry must be 1 to 140 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file
    # readable by everyone (0644), never the 0600 a temp file gets.
    os.chmod(path, 0o644)
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
