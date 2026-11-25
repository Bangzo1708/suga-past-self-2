"""Two Lines to Your Past Self — round 2 entry.

Writes exactly two lines to /output/entry.txt (and ./entry.txt for local
verification). No network, no randomness, no input: the text is fixed.
"""

from pathlib import Path

ENTRY = (
    "Don't hang up on your father at 2 a.m. when he calls from the hospital "
    "car park to say he's sorry.\n"
    "He never calls again, and you spend the next twenty years writing the "
    "apology you refused to hear.\n"
)


def main() -> None:
    text = ENTRY
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    Path(__file__).resolve().parent.joinpath("entry.txt").write_text(
        text, encoding="utf-8"
    )


if __name__ == "__main__":
    main()
