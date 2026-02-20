#!/usr/bin/env python3
import json
import logging
import sys


logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stderr,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    logger.info("payload generation started")

    payload = [
        {"title": "first", "name": "alice", "value": "10"},
        {"title": "second", "name": "bob", "value": "20"},
        {"title": "third", "name": "charlie", "value": "30"},
    ]
    logger.info("payload generated: items=%d", len(payload))
    print(json.dumps(payload, ensure_ascii=False))
    logger.info("payload output completed")


if __name__ == "__main__":
    main()
