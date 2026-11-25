#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — make.fun entry.

Writes the winning one-line deadpan review of the most boring everyday
object to /output/entry.txt. The line is a single line, 107 characters
(gate: 1 to 200), chosen by a local pairwise tournament judged against
the bounty's published judge brief (see README.md for the tournament
table).

Revision (v2): after the first test run, the entry was changed from the
provisional doorstop line (#1, Swiss 1.4, last place) to the tournament
winner, the lint roller line (#13, Swiss 2.45, final 0.75-0.25 over the
Swiss leader #14), and validate() now rejects lines with a trailing
newline or leading/trailing whitespace instead of silently accepting
them, so the entry the grader reads is exactly the line that was judged.
"""

import os

# Winning line (tournament winner — see README.md).
ENTRY = (
    "The lint roller picks up every hair except the one you actually "
    "saw, which it rolls over like a speed bump."
)


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> str:
    """Check `line` against the kit's sealed-scorer gate, verbatim.

    competition.yaml: "/output/entry.txt is UTF-8 text of 1 to 200
    characters, not only white space". Single-line follows from the
    task itself (one line, at most 200 characters). Returns the line
    unchanged; raises ValueError on any gate violation.
    """
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    line.encode("utf-8")  # must be valid UTF-8
    if not 1 <= len(line) <= 200:
        raise ValueError(f"length {len(line)} outside 1-200")
    if not line.strip():
        raise ValueError("entry is only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be one line")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    return line


def write_entry(line: str, out_dir: str) -> str:
    """Atomically write `line` to entry.txt inside `out_dir`.

    Writes to a temp file in the same directory, flushes and fsyncs
    it, then renames it into place so the grader never observes a
    half-written entry, and fsyncs the directory so the rename itself
    is durable. Returns the final path.
    """
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    try:
        with open(tmp, "w", encoding="utf-8", newline="") as f:
            f.write(line)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, target)
        dir_fd = os.open(out_dir, os.O_DIRECTORY)
        try:
            os.fsync(dir_fd)
        finally:
            os.close(dir_fd)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return target


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: entry.txt on disk must match `expected` exactly.

    Compares both the raw bytes and the decoded text; any mismatch
    raises RuntimeError so a corrupted or truncated entry fails loudly
    instead of being submitted.
    """
    expected_bytes = expected.encode("utf-8")
    with open(path, "rb") as f:
        actual_bytes = f.read()
    if actual_bytes != expected_bytes:
        raise RuntimeError(
            f"verification failed: {path} is {len(actual_bytes)} bytes, "
            f"expected {len(expected_bytes)} bytes"
        )
    if actual_bytes.decode("utf-8") != expected:
        raise RuntimeError(f"verification failed: {path} content mismatch")


def main() -> None:
    line = validate(ENTRY)
    out_dir = output_dir()
    path = write_entry(line, out_dir)
    verify_written(path, line)
    print(f"Wrote {len(line)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
