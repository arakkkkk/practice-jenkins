#!/usr/bin/env python3
import json
import logging
import sys


def setup_logger() -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        # stdout は Upstream が JSON を受け取る用途に使うため、ログは stderr に出す。
        stream=sys.stderr,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    return logging.getLogger(__name__)


def main() -> None:
    logger = setup_logger()
    logger.info("payload generation started")

    payload = [
        {"title": "first", "name": "alice", "value": "10"},
        {"title": "second", "name": "bob", "value": "20"},
        {"title": "third", "name": "charlie", "value": "30"},
    ]
    logger.info("payload generated: items=%d", len(payload))
    # Upstream 側で returnStdout として受け取る値なので、JSONのみを stdout に出力する。
    print(json.dumps(payload, ensure_ascii=False))
    logger.info("payload output completed")


if __name__ == "__main__":
    main()
