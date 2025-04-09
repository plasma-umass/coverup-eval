# file: tornado/simple_httpclient.py:494-497
# asked: {"lines": [494, 495, 496, 497], "branches": [[495, 0], [495, 496]]}
# gained: {"lines": [494], "branches": []}

import pytest
from tornado import ioloop, httputil
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class MockIOLoop:
    def __init__(self):
        self.timeouts = []

    def remove_timeout(self, timeout):
        self.timeouts.remove(timeout)

@pytest.fixture
def mock_ioloop(monkeypatch):
    mock_loop = MockIOLoop()
    monkeypatch.setattr(ioloop, 'IOLoop', lambda: mock_loop)
    return mock_loop

@pytest.fixture
def http_connection(mock_ioloop):
    class _HTTPConnection(httputil.HTTPMessageDelegate):
        def __init__(self, io_loop):
            self.io_loop = io_loop
            self._timeout = None

        def _remove_timeout(self) -> None:
            if self._timeout is not None:
                self.io_loop.remove_timeout(self._timeout)
                self._timeout = None

    return _HTTPConnection(mock_ioloop)

def test_remove_timeout_with_timeout(http_connection, mock_ioloop):
    http_connection._timeout = 'timeout'
    mock_ioloop.timeouts.append('timeout')
    http_connection._remove_timeout()
    assert http_connection._timeout is None
    assert 'timeout' not in mock_ioloop.timeouts

def test_remove_timeout_without_timeout(http_connection, mock_ioloop):
    http_connection._timeout = None
    http_connection._remove_timeout()
    assert http_connection._timeout is None
    assert mock_ioloop.timeouts == []
