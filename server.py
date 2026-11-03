from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs, urlencode
from urllib.request import Request, urlopen
import json
import ssl
import certifi
import os

ROOT = Path(__file__).resolve().parent

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        if parsed.path == "/api/weather":
            lat, lon = params.get("lat", ["59.9086"])[0], params.get("lon", ["10.7345"])[0]
            url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?" + urlencode({"lat": lat, "lon": lon})
            self.proxy(url, {"User-Agent": "KystdagensKontrollrom/1.0 learning project (local app)"}, "application/json; charset=utf-8")
        elif parsed.path == "/api/tide":
            now = __import__("datetime").datetime.now().astimezone()
            fromtime = params.get("fromtime", [now.strftime("%Y-%m-%dT%H:00")])[0]
            totime = params.get("totime", [(now + __import__("datetime").timedelta(days=1)).strftime("%Y-%m-%dT%H:00")])[0]
            query = {"tide_request": "locationdata", "lat": params.get("lat", ["59.9086"])[0], "lon": params.get("lon", ["10.7345"])[0], "fromtime": fromtime, "totime": totime, "datatype": "all", "interval": "60", "refcode": "cd", "lang": "nb", "tzone": "1", "dst": "1"}
            url = "https://vannstand.kartverket.no/tideapi.php?" + urlencode(query)
            self.proxy(url, {}, "application/xml; charset=utf-8")
        elif parsed.path in ("/", "/kystdagens-kontrollrom.html"):
            content = (ROOT / "kystdagens-kontrollrom.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            self.send_error(404)

    def proxy(self, url, headers, content_type):
        try:
            req = Request(url, headers=headers)
            tls_context = ssl.create_default_context(cafile=certifi.where())
            with urlopen(req, timeout=20, context=tls_context) as upstream:
                data = upstream.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Cache-Control", "public, max-age=300")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception as exc:
            payload = json.dumps({"error": str(exc)}).encode()
            self.send_response(502)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.log_date_time_string(), fmt % args))

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", "8000"))
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"Kystdagens kontrollrom kjører på port {port}")
    print("Stopp serveren med Ctrl+C")
    server.serve_forever()
