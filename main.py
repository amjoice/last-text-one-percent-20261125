#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes the dying phone's final text message to /output/entry.txt.

The line: a phone at 1% spends its last breath doing its owner one
final favour — deleting the ex's "u up?" text — then dies in peace.
It reads like a real text, it is the phone's own voice with a stake
in dying, and the joke turns on a specific detail instead of a
battery pun.

Stdlib only: the grading sandbox is plain python:3.13-slim.
"""

import os

ENTRY = (
    "1%. your ex just texted 'u up?' so i deleted it. "
    "you're welcome. now let me die in peace."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
