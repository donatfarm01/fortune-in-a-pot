#!/usr/bin/env python3
"""Fortune in a Pot entry: one kind, funny fortune for a houseplant.

Writes a single line, 1 to 120 characters, to /output/entry.txt.
The fortune is told as a prediction for the plant on the windowsill:
by spring its newest leaf outshines the room, and the cat leaves it alone.
"""

import os

ENTRY = "By spring, your newest leaf will outshine every plant in this room — and the cat will finally leave you alone."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
