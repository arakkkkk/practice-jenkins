#!/usr/bin/env python3
import json


def main() -> None:
    payload = [
        {"title": "first", "name": "alice", "value": "10"},
        {"title": "second", "name": "bob", "value": "20"},
        {"title": "third", "name": "charlie", "value": "30"},
    ]
    print(json.dumps(payload, ensure_ascii=False))


if __name__ == "__main__":
    main()
