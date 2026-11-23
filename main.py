#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Entry program: writes the vacuum's one-line excuse to /output/entry.txt.
Deterministic, no network, same bytes on every run.
"""

import os

LINE = "I keep one spot dirty. It is the before photo."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE
    # Pre-write self-check: the gate wants UTF-8 text of 1-200
    # characters, not only whitespace, on a single line.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    assert encoded.decode("utf-8") == text, "entry is not clean UTF-8"
    assert "\n" not in text, "entry must be a single line"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)

    # Post-write re-read self-check: the bytes on disk are exactly
    # the chosen line, nothing more.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        on_disk = f.read()
    assert on_disk == text, "entry.txt does not match the chosen line"
    assert 1 <= len(on_disk) <= 200, "entry.txt length outside 1-200"


if __name__ == "__main__":
    main()
