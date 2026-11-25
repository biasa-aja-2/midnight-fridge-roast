#!/usr/bin/env python3
"""Midnight Fridge Roast.

Writes a single one-line roast of a smart fridge that refuses to open
after midnight, to /output/entry.txt.

The roast: at midnight the fridge turns bouncer -- the leftovers are
VIPs and the owner is not on the list. The joke is aimed squarely at
the fridge's petty midnight rule itself, not at smart homes in
general: the door policy is the punchline, and "I'm not on the list"
is exactly what a person says out loud at a door.

Pure standard library only; no third-party packages, no network access.
"""

import os

LINE = (
    "My fridge locks at midnight like a bouncer who decided the "
    "leftovers are VIPs and I'm not on the list."
)


def gate(line):
    """Mirror the sealed scorer's gate: UTF-8 text, 1 to 200 characters,
    not only white space, a single line with no leading/trailing space."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    line.encode("utf-8")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be one line with no surrounding white space")
    return line


def main():
    line = gate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != line.encode("utf-8"):
        raise ValueError("read-back mismatch")
    print("wrote {} ({} chars)".format(path, len(line)))


if __name__ == "__main__":
    main()
