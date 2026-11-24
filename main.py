#!/usr/bin/env python3
"""Fortune in a Pot entry: one kind, funny fortune for a houseplant.

Writes a single line, 1 to 120 characters, to /output/entry.txt.
The fortune is told as a prediction for the plant on the windowsill:
by spring its newest leaf outshines the room, and the cat leaves it alone.
"""

import os

# The joke: a fortune told to the houseplant itself — its newest leaf
# will outshine every plant in the room by spring, and the cat that
# keeps bothering it will finally leave it alone.
ENTRY = "By spring, your newest leaf will outshine every plant in this room — and the cat will finally leave you alone."


# Writes the entry exactly as-is, with no trailing newline, so the
# submitted line is byte-identical to the ENTRY constant above.
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
