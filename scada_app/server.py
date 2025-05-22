import json
import os
import time
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from .sensors import sensors

class SCADAHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/events':
            self.send_response(200)
            self.send_header('Content-type', 'text/event-stream')
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            try:
                while True:
                    data = sensors.get_data()
                    self.wfile.write(f"data: {json.dumps(data)}\n\n".encode())
                    self.wfile.flush()
                    time.sleep(1)
            except BrokenPipeError:
                pass
        else:
            super().do_GET()

def run(host='0.0.0.0', port=8000):
    sensors.start()
    # Serve files from the package directory
    os.chdir(os.path.dirname(__file__))
    server = HTTPServer((host, port), SCADAHandler)
    print(f"Serving on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    run()
