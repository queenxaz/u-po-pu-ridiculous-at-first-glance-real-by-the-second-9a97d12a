#!/usr/bin/env python3
"""Entry for make.fun bounty u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.

Writes one sentence (180 characters) to /output/entry.txt: a startup pitch
for a bizarre idea that sounds ridiculous at first glance but holds together
as a real business on the second look.

No network, no randomness, no secrets: the sentence is a fixed string.
"""

import os

ENTRY = (
    "We train seagulls to fetch phones dropped off cliffs and rooftops, "
    "and phone insurers pay us per handset recovered \u2014 because a rescued "
    "phone costs them far less than a replacement."
)


def main() -> None:
    # The gate refuses anything outside 1..200 characters, so check the
    # sentence before writing it out.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
