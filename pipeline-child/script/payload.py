#!/usr/bin/env python3
import json
import logging
import sys
from pathlib import Path


def setup_logger() -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        # stdout は Upstream が JSON を受け取る用途に使うため、ログは stderr に出す。
        stream=sys.stderr,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    return logging.getLogger(__name__)


def main() -> None:
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("payload.json")
    logger = setup_logger()
    logger.info("payload generation started")

    payload = [
        {"title": "first", "name": "alice", "value": "10"},
        {"title": "second", "name": "bob", "value": "20"},
        {"title": "third", "name": "charlie", "value": "30"},
    ]
    logger.info("payload generated: items=%d", len(payload))
    payload_text = json.dumps(payload, ensure_ascii=False)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(payload_text, encoding="utf-8")
    logger.info("payload file written: path=%s", output_path)
    # 既存互換のため、stdout にも JSON を出力する。
    print(payload_text)
    logger.info("payload output completed")


if __name__ == "__main__":
    main()
