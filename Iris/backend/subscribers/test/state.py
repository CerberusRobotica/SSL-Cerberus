from threading import Lock

class TestState:
    def __init__(self):
        self._lock = Lock()
        self.last_message = None

    def update(self, data: bytes):
        with self._lock:
            self.last_message = data

    def get(self):
        with self._lock:
            return self.last_message


test_state = TestState()
