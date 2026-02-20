#!/usr/bin/env python3
import json
import sys


def main() -> int:
    print("python: start", file=sys.stderr)

    payload = {
        "host": "host-a",
        "action": "run",
        "param": "sample1",
        "flag": True,
        "note": "demo",
    }
    print(json.dumps(payload, separators=(",", ":")))

    print("python: done", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
