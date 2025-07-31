#!/usr/bin/env python3
"""Fetch images from Unsplash and cache them locally.

This utility downloads random images via the Unsplash API and stores them in the
``images/`` directory. Downloaded images are reused if already present to reduce
bandwidth usage. The daily download amount is limited through ``config.json``.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

CONFIG_FILE = Path(__file__).with_name("config.json")
IMAGE_DIR = Path(__file__).with_name("images")
IMAGE_DIR.mkdir(exist_ok=True)
LOG_FILE = Path(__file__).with_name("download.log")
OFFLINE_FLAG = Path(__file__).with_name("offline.flag")


def load_config() -> dict:
    """Load configuration from ``config.json``."""
    with CONFIG_FILE.open() as f:
        return json.load(f)


def log(msg: str) -> None:
    """Append a timestamped log message to ``download.log``."""
    with LOG_FILE.open("a") as f:
        f.write(f"{datetime.utcnow().isoformat()} {msg}\n")


def download_image(url: str, filename: Path) -> None:
    """Download ``url`` to ``filename``."""
    req = Request(url, headers={"User-Agent": "Info-Beamer Photoframe"})
    with urlopen(req) as resp, open(filename, "wb") as out:
        out.write(resp.read())


def fetch_images(count: int, api_key: str) -> None:
    """Fetch ``count`` random images using ``api_key``."""
    for _ in range(count):
        api_url = f"https://api.unsplash.com/photos/random?client_id={api_key}"
        try:
            with urlopen(api_url) as resp:
                data = json.loads(resp.read().decode())
            img_url = data["urls"]["full"]
            name = data["id"] + ".jpg"
            target = IMAGE_DIR / name
            if not target.exists():
                download_image(img_url, target)
                log(f"downloaded {name}")
                if OFFLINE_FLAG.exists():
                    OFFLINE_FLAG.unlink()
        except URLError as err:
            log(f"network error: {err}")
            OFFLINE_FLAG.touch()
            break
        except Exception as err:  # noqa: BLE001
            log(f"error: {err}")
            OFFLINE_FLAG.touch()
            break


def main() -> None:
    cfg = load_config()
    api_key = cfg.get("unsplash_key", {}).get("value") or os.getenv("UNSPLASH_KEY")
    if not api_key:
        print("Unsplash key missing")
        sys.exit(1)

    daily = int(cfg.get("daily_limit", {}).get("value", 50))
    fetch_images(daily, api_key)


if __name__ == "__main__":
    main()
