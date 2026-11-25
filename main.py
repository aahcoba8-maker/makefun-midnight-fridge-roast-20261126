"""Midnight Fridge Roast — make.fun entry.

Writes one roast line to entry.txt in the output directory.
Gate: UTF-8 text of 1 to 200 characters, not only whitespace.
Stdlib only.
"""

import os

TEXT = "At midnight my fridge locks itself and flashes a salad at me, like it's staging an intervention I never agreed to."


def main():
    if not (1 <= len(TEXT) <= 200) or not TEXT.strip():
        raise SystemExit("entry text fails the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEXT)
    except OSError:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(TEXT)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        raise SystemExit("entry.txt does not match the roast text")
    print(TEXT)
    print("chars:", len(TEXT))


if __name__ == "__main__":
    main()
