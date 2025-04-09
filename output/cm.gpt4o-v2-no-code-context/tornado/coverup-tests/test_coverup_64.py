# file: tornado/simple_httpclient.py:535-540
# asked: {"lines": [535, 536, 537, 538, 539, 540], "branches": [[537, 0], [537, 538]]}
# gained: {"lines": [535], "branches": []}

import pytest
from tornado import httputil, ioloop
from tornado.simple_httpclient import HTTPResponse

class MockIOLoop:
    def __init__(self):
        self.callbacks = []

    def add_callback(self, callback, response):
        self.callbacks.append((callback, response))

    def run_callbacks(self):
        for callback, response in self.callbacks:
            callback(response)

class MockHTTPConnection(httputil.HTTPMessageDelegate):
    def __init__(self, io_loop):
        self.io_loop = io_loop
        self.final_callback = None

    def _release(self):
        pass

    def _run_callback(self, response: HTTPResponse) -> None:
        self._release()
        if self.final_callback is not None:
            final_callback = self.final_callback
            self.final_callback = None  # type: ignore
            self.io_loop.add_callback(final_callback, response)

@pytest.fixture
def mock_io_loop():
    return MockIOLoop()

@pytest.fixture
def mock_http_connection(mock_io_loop):
    return MockHTTPConnection(mock_io_loop)

def test_run_callback_with_final_callback(mock_http_connection, mock_io_loop):
    def final_callback(response):
        assert response.code == 200

    mock_http_connection.final_callback = final_callback
    response = HTTPResponse(request=None, code=200, effective_url="http://example.com")
    mock_http_connection._run_callback(response)
    mock_io_loop.run_callbacks()

    assert mock_http_connection.final_callback is None

def test_run_callback_without_final_callback(mock_http_connection, mock_io_loop):
    mock_http_connection.final_callback = None
    response = HTTPResponse(request=None, code=200, effective_url="http://example.com")
    mock_http_connection._run_callback(response)
    mock_io_loop.run_callbacks()

    assert mock_http_connection.final_callback is None
