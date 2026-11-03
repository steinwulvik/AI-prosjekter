from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs, urlencode
from urllib.request import Request, urlopen
import json
import ssl
import certifi
import os
import time

ROOT = Path(__file__).resolve().parent
TLS = ssl.create_default_context(cafile=certifi.where())
POINT_CACHE = {"expires": 0, "data": None}
TRAFFIC_API = "https://trafikkdata-api.atlas.vegvesen.no/"


def fetch_json(url, method="GET", body=None, headers=None, timeout=30):
    request_headers = {"User-Agent": "TryggSykkeltur/0.1 (learning project)"}
    if headers:
        request_headers.update(headers)
    data = json.dumps(body).encode("utf-8") if body is not None else None
    if data is not None:
        request_headers.setdefault("Content-Type", "application/json")
    req = Request(url, data=data, headers=request_headers, method=method)
    with urlopen(req, timeout=timeout, context=TLS) as response:
        return json.loads(response.read().decode("utf-8"))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        if parsed.path == "/api/weather":
            lat = params.get("lat", ["59.9086"])[0]
            lon = params.get("lon", ["10.7345"])[0]
            url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?" + urlencode({"lat": lat, "lon": lon})
            self.proxy(url, {"User-Agent": "TryggSykkeltur/0.1 (learning project)"}, "application/json; charset=utf-8")
        elif parsed.path == "/api/cycle/route":
            lon1 = params.get("lon1", ["7.9956"])[0]
            lat1 = params.get("lat1", ["58.1467"])[0]
            lon2 = params.get("lon2", ["8.7669"])[0]
            lat2 = params.get("lat2", ["58.4617"])[0]
            route_url = "https://brouter.de/brouter?" + urlencode({"lonlats": f"{lon1},{lat1}|{lon2},{lat2}", "profile": "trekking", "alternativeidx": "0", "format": "geojson"})
            self.proxy(route_url, {"User-Agent": "TryggSykkeltur/0.1 (learning project)"}, "application/geo+json; charset=utf-8", timeout=45)
        elif parsed.path == "/api/cycle/traffic-points":
            self.traffic_points()
        elif parsed.path == "/api/cycle/history":
            point_id = params.get("id", [""])[0]
            if not point_id or len(point_id) > 80:
                self.send_json(400, {"error": "Ugyldig målepunkt-ID"})
            else:
                self.traffic_history(point_id)
        elif parsed.path in ("/", "/sykkelturen", "/sykkelturen.html"):
            self.send_file("sykkelturen.html")
        else:
            self.send_error(404)

    def send_file(self, name):
        try:
            body = (ROOT / name).read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except FileNotFoundError:
            self.send_error(404)

    def send_json(self, status, body, cache="no-store"):
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", cache)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def traffic_points(self):
        now = time.time()
        if POINT_CACHE["data"] is not None and now < POINT_CACHE["expires"]:
            self.send_json(200, POINT_CACHE["data"], "public, max-age=21600")
            return
        query = """{ trafficRegistrationPoints(searchQuery: { roadCategoryIds: [E, R, F] }) { id name location { coordinates { latLon { lat lon } } } } }"""
        try:
            result = fetch_json(TRAFFIC_API, "POST", {"query": query}, timeout=45)
            if result.get("errors"):
                raise RuntimeError(str(result["errors"][0].get("message", "GraphQL-feil")))
            points = result.get("data", {}).get("trafficRegistrationPoints", [])
            POINT_CACHE["data"] = points
            POINT_CACHE["expires"] = now + 21600
            self.send_json(200, points, "public, max-age=21600")
        except Exception as exc:
            self.send_json(502, {"error": f"Trafikkdata-punkter: {exc}"})

    def traffic_history(self, point_id):
        safe_id = json.dumps(point_id)
        query = f"""{{ trafficData(trafficRegistrationPointId: {safe_id}) {{ volume {{ average {{ daily {{ byYear {{ year total {{ volume {{ average confidenceInterval {{ lowerBound upperBound }} }} coverage {{ percentage }} }} }} }} }} }} }} }}"""
        try:
            result = fetch_json(TRAFFIC_API, "POST", {"query": query})
            if result.get("errors"):
                raise RuntimeError(str(result["errors"][0].get("message", "GraphQL-feil")))
            rows = result.get("data", {}).get("trafficData", {}).get("volume", {}).get("average", {}).get("daily", {}).get("byYear", [])
            self.send_json(200, rows, "public, max-age=21600")
        except Exception as exc:
            self.send_json(502, {"error": f"Historiske trafikkdata: {exc}"})

    def proxy(self, url, headers, content_type, timeout=25):
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=timeout, context=TLS) as response:
                data = response.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Cache-Control", "public, max-age=300")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception as exc:
            self.send_json(502, {"error": str(exc)})

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.log_date_time_string(), fmt % args))

if __name__ == "__main__":
    host = "0.0.0.0"
    port = int(os.environ.get("PORT", "8001"))
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"Den trygge sykkelturen kjører på port {port}")
    print("Stopp serveren med Ctrl+C")
    server.serve_forever()
