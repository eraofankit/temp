import threading
import time
import urllib.request
import unittest

from scada_app.server import run

HOST = '127.0.0.1'
PORT = 8765


def start_server():
    threading.Thread(target=run, kwargs={'host': HOST, 'port': PORT}, daemon=True).start()
    time.sleep(1)


class ServerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        start_server()

    def test_index_served(self):
        with urllib.request.urlopen(f'http://{HOST}:{PORT}/') as resp:
            self.assertEqual(resp.status, 200)
            self.assertIn(b'SCADA', resp.read())

    def test_events_stream(self):
        req = urllib.request.Request(f'http://{HOST}:{PORT}/events')
        with urllib.request.urlopen(req) as resp:
            self.assertEqual(resp.status, 200)
            self.assertEqual(resp.headers.get_content_type(), 'text/event-stream')


if __name__ == '__main__':
    unittest.main()
