#!/usr/bin/env python3
"""Write one pitch sentence to /output/entry.txt.

Competition: u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a
("Ridiculous at First Glance, Real by the Second").

The sentence pitches a bizarre startup idea that sounds ridiculous at first
glance yet makes sense as a real business: a dog's autobiography, published
on Amazon. See candidates.md for the 12 candidates and the manual ranking
that picked this one.

The program is deterministic: it always writes the same sentence, with no
trailing newline, so the two grading runs produce byte-identical output.
A guard refuses to write anything outside the gate's limits (1-200
characters, one sentence, not only white space) instead of silently
producing an invalid entry.
"""

import os

ENTRY = (
    "We write your dog's autobiography and publish it on Amazon, "
    "because owners will pay anything to see their rescue mutt become "
    "a bestseller."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} characters, outside 1-200")
    if ENTRY != ENTRY.strip() or "\n" in ENTRY:
        raise SystemExit("entry must be a single sentence with no newlines")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
