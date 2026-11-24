"""Loading Screen Gold: a tip in 200 characters.

Writes a single original loading-screen tip to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback ".").
Deterministic, stdlib only, no network.
"""

import os

TIP = "The build isn't stuck. It's quietly judging your last commit. Stretch, hydrate — it can't ship without you."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TIP + "\n")

if __name__ == "__main__":
    main()
