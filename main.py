"""One haiku about debugging, written to $MAKEFUN_OUTPUT_DIR/entry.txt.

The grader runs: python3 -P -s /bot/main.py
No network, no randomness, no input read. Deterministic output.
"""

import os

HAIKU = (
    # the(1) cur-sor(2) blinks(1) waits(1) = 5
    "the cursor blinks, waits\n"
    # three(1) in(1) the(1) morn-ing(2) still(1) stuck(1) = 7
    "three in the morning, still stuck\n"
    # it(1) was(1) a(1) ty-po(2) = 5
    "it was a typo\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
