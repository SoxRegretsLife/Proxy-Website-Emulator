from flask import Flask, request, Response
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

app = Flask(__name__)

@app.route('/')
def index():
    return open("index.html").read()

@app.route('/render')
def render():
    url = request.args.get('url')
    if not url:
        return "Missing URL", 400

    parsed_url = urlparse(url)
    if not parsed_url.scheme.startswith("http"):
        return "Invalid URL", 400

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, 'html.parser')

        tags_attrs = {
            'a': 'href',
            'img': 'src',
            'script': 'src',
            'link': 'href',
            'iframe': 'src',
            'source': 'src'
        }

        for tag, attr in tags_attrs.items():
            for t in soup.find_all(tag):
                if t.has_attr(attr):
                    original = t[attr]
                    new_url = urljoin(url, original)
                    t[attr] = f"/proxy?url={new_url}"

                    if tag == 'a':
                        t['onclick'] = f"event.preventDefault(); loadWebsite('{new_url}');"

        emulator_css = """
        <style>
          body { font-family: Arial, sans-serif; margin: 20px; }
          img { max-width: 100%; }
          a { color: blue; text-decoration: underline; }
        </style>
        """
        soup.head.insert(0, BeautifulSoup(emulator_css, "html.parser"))

        return str(soup)

    except Exception as e:
        return f"<p>Error: {e}</p>"

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return "Missing URL", 400

    try:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, stream=True)
        content_type = resp.headers.get('Content-Type', 'text/plain')
        return Response(resp.content, status=resp.status_code, content_type=content_type)
    except Exception as e:
        return f"Error proxying: {e}", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
