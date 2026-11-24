"""The Perfect Pickup Line — make.fun entry.

Writes a single original pickup line to /output/entry.txt.
Stdlib only, deterministic.
"""

import os

LINE = "Are you my system prompt? Because ever since I met you, everything I generate starts with you."

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line: str) -> None:
    """Guard the gate: 1-200 chars, single line, no stray whitespace."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= 200, f"line must be 1-200 chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line == line.strip(), "line must not have leading/trailing whitespace"
    assert line.strip(), "line must not be only whitespace"


def main() -> None:
    validate_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
