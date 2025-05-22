import random
import threading
import time

class SensorData:
    def __init__(self):
        self.lock = threading.Lock()
        # Example sensors
        self.data = {
            'temperature': 25.0,
            'pressure': 1.0,
            'flow': 100.0,
        }
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self._update_loop, daemon=True).start()

    def _update_loop(self):
        while self.running:
            with self.lock:
                # Randomly vary sensors
                self.data['temperature'] += random.uniform(-0.5, 0.5)
                self.data['pressure'] += random.uniform(-0.02, 0.02)
                self.data['flow'] += random.uniform(-1, 1)
            time.sleep(1)

    def get_data(self):
        with self.lock:
            return dict(self.data)

sensors = SensorData()
