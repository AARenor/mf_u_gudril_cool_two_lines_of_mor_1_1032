"""Write the make.fun entry text for

u-gudril-cool-two-lines-of-morning-light-ade94fc5
to entry.txt, with no trailing newline.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "The cat has not moved since six.\n"
    "The square of light has, and takes her with it."
)

assert 1 <= len(TEXT) <= 280


def output_dir() -> Path:
    """MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    folder = output_dir()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    print(f"wrote {target} ({len(TEXT)} characters)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
