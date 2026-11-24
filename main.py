#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning label for a time machine to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-120 characters, one line).
"""

import os

LABEL = "WARNING: Do not meet yourself. He knows what you did, he is angrier than you remember, and he brought receipts."
# 111 chars — inside the sealed scorer's 1-120 gate, single line, no newline.


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    assert 1 <= len(LABEL) <= 120, f"label is {len(LABEL)} chars, gate is 1-120"
    assert "\n" not in LABEL, "label must be a single line"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
