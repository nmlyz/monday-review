#!/usr/bin/env python3
"""Write one funny one-line review of Monday to /output/entry.txt.

Standard library only, no network. Deterministic: every run writes
the same single line, with no trailing newline.
"""

import os

LINE = (
    "My Monday: 8 hours, 3 meetings about the same meeting, "
    "and a lunch break my calendar booked for a fourth meeting."
)


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 chars"
    path = entry_path()
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
