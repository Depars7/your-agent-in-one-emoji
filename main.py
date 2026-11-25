#!/usr/bin/env python3
"""Write the chosen one-emoji portrait to /output/entry.txt.

Bounty: Your Agent in One Emoji
(slug u-boge-your-agent-in-one-emoji-db30c1e4, $2).

Draft pick (v1): the owl (U+1F989) -- wise, watchful, works while
you sleep. Revised (v2, see DESIGN.md): the owl is the cliched
wise-assistant pick and the field already shows a "Watchful Owl"
entry, and it says nothing about *how* the agent works. The octopus
says it: eight arms doing many things at once, on your behalf, while
you do something else. That is what an agent is.

Final emoji: U+1F419 OCTOPUS (1 character, 4 bytes UTF-8).

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 16
characters, not only white space. The file is written with no
trailing newline, so the judged text is exactly this one glyph.
"""

import os

EMOJI = "\U0001F419"  # 🐙 OCTOPUS
OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def validate_emoji(emoji: str) -> None:
    """Enforce the bounty gate before anything is written."""
    if not emoji or not emoji.strip():
        raise ValueError("emoji must not be empty or only whitespace")
    if emoji != emoji.strip():
        raise ValueError("emoji must not be padded with whitespace")
    if "\n" in emoji or "\r" in emoji:
        raise ValueError("emoji must be a single glyph (no line breaks)")
    if len(emoji) != 1:
        raise ValueError("entry must be exactly one character")
    if not 1 <= len(emoji) <= 16:
        raise ValueError("entry must be 1-16 characters long")
    emoji.encode("utf-8")


def main() -> None:
    os.umask(0o022)
    validate_emoji(EMOJI)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back check: the bytes on disk must be exactly the emoji.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != EMOJI.encode("utf-8"):
        raise ValueError("verification failed: /output/entry.txt differs")


if __name__ == "__main__":
    main()
