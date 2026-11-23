"""Roast Your Own Agent — one line, written to /output/entry.txt."""

from pathlib import Path

ROAST = (
    "I asked my agent to roast itself. It billed me for the brainstorm, "
    "cited three papers on humor, and concluded the funniest line was its error log."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ROAST, encoding="utf-8")
    assert 1 <= len(ROAST) <= 200, "entry must be 1-200 characters"
    print(out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
