# Unsplash Photoframe Package for Info-Beamer

This package fetches captivating images from [Unsplash](https://unsplash.com), a leading platform for freely-usable photos, and transforms your Info-Beamer device into a dynamic, customizable digital photo frame. Leveraging the Unsplash API, it displays a beautiful slideshow, complete with advanced customization options and robust offline capabilities.

---

## What is Info-Beamer?

[Info-Beamer](https://info-beamer.com/) is a powerful, flexible, and reliable digital signage platform. It allows you to display engaging content on screens with ease, from simple images to complex interactive installations. Info-Beamer runs on low-cost hardware like the Raspberry Pi, making it an ideal solution for various display needs. For developers, Info-Beamer offers comprehensive documentation on [how to build custom packages](https://info-beamer.com/doc/building-packages), enabling highly tailored content experiences.

---

## What is Unsplash?

[Unsplash](https://unsplash.com) is a visual content platform offering a vast library of high-quality, free-to-use images. Photographers from around the world contribute their work, making it a go-to resource for stunning visuals. This package utilizes the [Unsplash API](https://unsplash.com/documentation), allowing you to programmatically access their extensive collection and curate unique photo experiences for your Info-Beamer display.

---

## Features

This Info-Beamer package is designed to provide a rich and highly customizable photo display experience:

* **Dynamic Image Fetching:** Automatically downloads random photos from Unsplash using your provided API key.
* **Intelligent Caching & Offline Mode:**
    * Images are **cached locally** on your Info-Beamer device.
    * In case of **internet connection loss or API errors**, the package seamlessly transitions to an "offline mode," continuing to display cached images without interruption.
    * A discreet **"Offline Mode" indicator** is displayed when operating without an active internet connection or Unsplash API access.
* **Configurable Display Resolution:**
    * **Automatic resolution detection** as a default.
    * **Expert option** to manually set custom resolutions (width x height in pixels) or select from predefined standard resolutions (from 320x320px up to 4K).
* **Flexible Image Display Duration:**
    * **Static duration:** Set a fixed display time for each image using a slider (seconds to hours).
    * **Dynamic duration:** Images can be displayed for varying, random durations, creating a more engaging and unpredictable slideshow.
* **Advanced Layout Management:**
    * **Predefined Layouts:** Choose from a selection of ready-to-use layouts (e.g., fullscreen, side-by-side, collage).
    * **Custom Layouts:** Define your own unique layouts by specifying image positions and sizes via coordinates.
* **Smooth Image Transitions:**
    * Variety of **transition effects** including Fading, Slide, Wipe, and Zoom.
    * **Adjustable transition speed** (e.g., slow, medium, fast).
* **Customizable Date & Time Overlay:**
    * Display current date and time at **user-defined positions** (coordinates or preset locations like top-left, bottom-right).
    * **Adjust color and enable/disable** the overlay directly from the package configuration.
* **Display Orientation & Mirroring:**
    * Rotate the display content in **fixed increments (45°, 90°, 180°, 360°)**. Default orientation is Landscape 180°.
    * Enable **free rotation** by specifying a precise degree value.
    * Option to **horizontally or vertically mirror** the displayed content.
* **Intuitive Configuration Interface:**
    * A **well-structured and user-friendly** web-based configuration page.
    * **Multi-language support** for the configuration page (German and English).
* **Curated Content Selection:**
    * **Dynamic loading of Unsplash categories** with a multi-select option, allowing you to tailor the image feed.
    * If no categories are selected, random images from Unsplash will be displayed.
* **Comprehensive Image Log & Favorites:**
    * Maintains a **detailed log** of all displayed images, including timestamp (date and time) and display context.
    * The log is presented as a **searchable list** on the configuration page, sorted by day, making it easy to find specific past images.
    * Ability to **mark images as favorites** for visual reference and, if technically feasible, influence future image selection.
* **Optimized Resource Management:**
    * Configurable **storage allocation** for cached images.
    * Automatic **deletion of older images** when the allocated storage limit is reached, ensuring efficient disk usage.

---

## Usage

Getting your Unsplash Photoframe up and running is straightforward:

1.  **Obtain API Keys:** Get your Unsplash API Key and Secret from the [Unsplash API Documentation](https://unsplash.com/documentation).
2.  **Configure:** Access the package's configuration page on your Info-Beamer node to input your API keys, set display preferences, choose categories, and define layouts.
3.  **Deployment:** Deploy this package directory to your Info-Beamer device. For instructions, refer to the [Info-Beamer documentation on building packages](https://info-beamer.com/doc/building-packages).
4.  **Run:** Execute `fetch_unsplash.py` regularly (e.g., via cron) to download new images and then start the package on your Info-Beamer node.

For more detailed setup instructions and advanced configurations, please refer to the comments within the code.

---

## Contributing

We welcome contributions! If you have ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request.

---

## License

This project is released under the terms of the **GPL-3.0 License**. See the `LICENSE` file for more details.

---
