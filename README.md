  # 🌐 Website Emulator

This project is a universal web emulator that lets you browse any website seamlessly inside a single page.
Built with Flask and HTML5, it fetches external websites, rewrites resources like images, links, and scripts, and displays them inside a custom viewer, without using iframes or external browsers.

✅ Supports clickable links, redirections, and dynamic JavaScript execution.
✅ Custom User-Agent field to simulate different browsers and devices.
✅ Realistic website appearance — CSS and JS are preserved, keeping the original design intact.
✅ Secure, fast, and lightweight — only a simple main.py and loader.html needed.
✅ Fullscreen mode and responsive layout for a better browsing experience.(Not really yet)
## 💡 Features

- Dynamic website loading via the address bar
- Resource rewriting (images, scripts, links)
- Safe proxying of remote content
- Inline script execution
- Clean, responsive UI

## 📦 Requirements

- Python 3.7+

- Flask
- requests
- beautifulsoup4

## Install dependencies:

```bash
pip install flask requests beautifulsoup4
