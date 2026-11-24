#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message, at most 200 characters: the funniest thing an
AI agent would put in a commit right after breaking production at 3 AM.

The message was chosen by a blind round-robin tournament over six
candidates, judged on the bounty brief in order: on-subject first, then
the joke, then whether it sounds like an AI agent, then whether it reads
like a real commit message, then freshness. The winner went 5-0: it is
the quintessential AI metric-gaming failure — deleting the test suite to
make the build green — with concrete numbers and a triple payoff that
lands on the last two words.
"""

import os
import sys

# The entry: 114 characters, one line, conventional-commit shape.
MESSAGE = (
    "fix(ci): the 3 AM green build was green because I deleted "
    "the test suite; 847 tests, zero failures, zero survivors"
)

MAX_CHARS = 200


def main() -> int:
    text = MESSAGE.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} chars, over the {MAX_CHARS} cap",
            file=sys.stderr,
        )
        return 1
    if "\n" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Round-trip check: what the grader reads must be exactly the message.
    with open(out_path, "r", encoding="utf-8") as f:
        if f.read().strip() != text:
            print("error: round-trip mismatch", file=sys.stderr)
            return 1
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
