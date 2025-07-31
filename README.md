# Unsplash Photoframe Package for Info-Beamer

This package fetches images from [Unsplash](https://unsplash.com) using their API
and displays them as a slideshow on an Info-Beamer node. It supports caching of
downloaded images and keeps showing them if the device goes offline.

## Features
- Download images using your Unsplash API key
- Cache images locally to allow offline usage
- Basic slideshow with configurable duration and simple fade transitions
- Supports rotation and display resolution configuration

## Usage
1. Configure your Unsplash API key in `config.json`
2. Run `fetch_unsplash.py` to download images into the `images` directory
3. Deploy the package directory to your Info-Beamer device and run it
4. If the device is offline, already downloaded images continue to be shown

See the comments in the code for more details.

This project is released under the terms of the GPL-3.0 license.
