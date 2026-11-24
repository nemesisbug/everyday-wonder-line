#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes a single sentence -- a small moment of wonder in everyday life --
to /output/entry.txt. The sentence is fixed: it was chosen, not generated,
so every run produces the same entry.
"""

import os

ENTRY = (
    "At midnight the fridge stopped humming, and the silence was so "
    "complete I could hear the house holding its breath."
)


def main() -> None:
    # The gate requires 1 to 200 characters of UTF-8 text, not only
    # whitespace. Refuse to write anything that would fail it.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry is only whitespace"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
