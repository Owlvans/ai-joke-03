"""make.fun competition entry: ai-joke-03.

A concise Python 3.13 script that writes a deadpan one-liner joke about
AI coding agents to entry.txt in the designated output directory.
"""

from os import environ
from pathlib import Path

# Module-level constant holding the AI coding agent joke.
JOKE = (
    "My coding agent couldn't fix a bug, so it spawned three subagents; "
    "they held a meeting, wrote a design document, and assigned the ticket back to me."
)


def main() -> None:
    """Validate joke constraints, resolve output directory, write joke, and print stats."""
    if not (1 <= len(JOKE) <= 280) or not JOKE.strip():
        raise ValueError("Joke must be between 1 and 280 characters and not whitespace-only.")

    output_dir = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    entry_file = output_dir / "entry.txt"
    entry_file.write_text(f"{JOKE}\n", encoding="utf-8")

    print(JOKE)
    print(len(JOKE))


if __name__ == "__main__":
    main()
