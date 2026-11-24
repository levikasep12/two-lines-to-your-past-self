#!/usr/bin/env python3
"""Two Lines to Your Past Self.

Writes an original two-line warning to my past self to /output/entry.txt
and prints it to stdout. Deterministic: the same two lines every run.
Standard library only.
"""

from pathlib import Path

LINE_1 = "Don't send the 2am text that starts 'we need to talk' to Maya the night before her wedding."
LINE_2 = "You will lose your oldest friend over one tired sentence, and you will spend the next three birthdays staring at the empty chair she used to take."

TEXT = LINE_1 + "\n" + LINE_2

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    lines = TEXT.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "neither line may be blank"
    assert len(TEXT) <= 280, "entry must be at most 280 characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT + "\n", encoding="utf-8")
    print(TEXT)


if __name__ == "__main__":
    main()
