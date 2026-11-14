# Built by an AI coding agent.
import os

JOKE = (
    "My agent fixed the bug, the test, the linter, and CI in one pass \u2014 "
    "and, as a bonus, my last shred of confidence that I know what I'm doing."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
