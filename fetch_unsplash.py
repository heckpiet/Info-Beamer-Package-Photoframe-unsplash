This script queries the Unsplash API for random photos and stores them in the
``images/`` directory. Already downloaded images are reused to keep bandwidth
low. It respects a daily download limit defined in ``config.json``.
"""
import json
import os
import random
import sys
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen, Request

CONFIG_FILE = Path(__file__).with_name('config.json')
IMAGE_DIR = Path(__file__).with_name('images')
IMAGE_DIR.mkdir(exist_ok=True)


def load_config():
    with CONFIG_FILE.open() as f:
        return json.load(f)


def save_log(msg: str) -> None:
    """Append log message with timestamp."""
    with Path('download.log').open('a') as f:
        f.write(f"{datetime.utcnow().isoformat()} {msg}\n")


def download_image(url: str, filename: Path) -> None:
    req = Request(url, headers={'User-Agent': 'Info-Beamer Photoframe'})
    with urlopen(req) as resp, open(filename, 'wb') as out:
        out.write(resp.read())


def fetch_images(count: int, api_key: str) -> None:
    for _ in range(count):
        url = f"https://api.unsplash.com/photos/random?client_id={api_key}"
        try:
            with urlopen(url) as resp:
                data = json.loads(resp.read().decode())
                img_url = data['urls']['full']
                name = data['id'] + '.jpg'
                target = IMAGE_DIR / name
                if not target.exists():
                    download_image(img_url, target)
                    save_log(f"downloaded {name}")
        except Exception as err:
            save_log(f"error: {err}")
            return


def main():
    cfg = load_config()
    api_key = cfg.get('unsplash_key', {}).get('value') or os.getenv('UNSPLASH_KEY')
    if not api_key:
        print('Unsplash key missing')
        sys.exit(1)
    daily = cfg.get('daily_limit', {}).get('value', 50)
    fetch_images(daily, api_key)


if __name__ == '__main__':
    main()
