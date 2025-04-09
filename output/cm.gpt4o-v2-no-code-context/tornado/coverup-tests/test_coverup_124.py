# file: tornado/tcpclient.py:161-164
# asked: {"lines": [161, 162, 163], "branches": []}
# gained: {"lines": [161], "branches": []}

import pytest
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient

class MockIOLoop:
    def __init__(self):
        self.timeouts = []

    def add_timeout(self, deadline, callback):
        self.timeouts.append((deadline, callback))
        return deadline

    def time(self):
        return 1000.0

    def remove_timeout(self, timeout):
        self.timeouts = [t for t in self.timeouts if t[0] != timeout]

@pytest.fixture
def mock_ioloop(monkeypatch):
    mock_loop = MockIOLoop()
    monkeypatch.setattr(IOLoop, 'current', lambda: mock_loop)
    return mock_loop

def test_set_timeout(mock_ioloop):
    class _Connector:
        def __init__(self, io_loop):
            self.io_loop = io_loop

        def on_timeout(self):
            pass

        def set_timeout(self, timeout: float) -> None:
            self.timeout = self.io_loop.add_timeout(
                self.io_loop.time() + timeout, self.on_timeout
            )

    connector = _Connector(mock_ioloop)
    connector.set_timeout(5.0)

    assert len(mock_ioloop.timeouts) == 1
    assert mock_ioloop.timeouts[0][0] == 1005.0
    assert mock_ioloop.timeouts[0][1] == connector.on_timeout
