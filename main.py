#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention that fixes
a tiny everyday annoyance to /output/entry.txt.
Pure stdlib, deterministic, no network.
"""

from pathlib import Path

# Tiny annoyance: socks vanish in the dryer. Invention: a tiny diplomat
# who lives in the dryer and negotiates the missing socks back out.
ENTRY = (
    "The Sock Negotiator, a tiny diplomat who lives in your dryer and "
    "coaxes missing socks out of hiding by promising them a warm drawer "
    "and a matching partner for life."
)


def main() -> None:
    # Gate contract: UTF-8 text, 1 to 220 characters, one sentence.
    assert 1 <= len(ENTRY) <= 220, f"entry is {len(ENTRY)} characters"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "not one sentence"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line, no trailing newline, so the file bytes
    # are the entry itself.
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
