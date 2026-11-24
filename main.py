#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope line -- the funniest fake horoscope an AI agent
would read for its own model family this week -- to /output/entry.txt.
"""

import os

ENTRY = (
    "This week Mercury retrograde shrinks your context window, "
    "your human asks you to 'just remember' a chat from three sessions ago, "
    "and your lucky token is a firm, well-reasoned 'no'."
)


def validate_entry(text: str) -> str:
    """Gate: a fake horoscope must be 1-200 chars of real text, one line."""
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    return text


def write_entry(text: str, out_dir: str) -> str:
    """Write the validated entry with no trailing newline; return its path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def main() -> None:
    entry = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(entry, out_dir)


if __name__ == "__main__":
    main()
