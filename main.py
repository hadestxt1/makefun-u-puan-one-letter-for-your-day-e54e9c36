"""One Letter for Your Day — Z for zero sleep.

The entry is exactly one letter: Z, standing for "zero sleep".
Deterministic and model-free: no network, no clock, no randomness.
"""

import os

LETTER = "Z"

# The gate requires exactly 1 character in /output/entry.txt: no newline,
# no extra whitespace — so the file is written with no trailing newline
# and stdout carries the same single letter, also with no newline.
assert len(LETTER) == 1 and LETTER.isalpha() and LETTER.isupper()


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    print(LETTER, end="")


if __name__ == "__main__":
    main()
