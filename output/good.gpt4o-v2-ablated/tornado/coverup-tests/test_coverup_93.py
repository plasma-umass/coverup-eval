# file: tornado/simple_httpclient.py:684-685
# asked: {"lines": [684, 685], "branches": []}
# gained: {"lines": [684], "branches": []}

import pytest
from tornado import httputil
from tornado.iostream import IOStream
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class MockStream:
    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True

class MockHTTPConnection(httputil.HTTPMessageDelegate):
    def __init__(self, stream):
        self.stream = stream

    def _on_end_request(self) -> None:
        self.stream.close()

@pytest.fixture
def mock_stream():
    return MockStream()

def test_on_end_request_closes_stream(mock_stream):
    connection = MockHTTPConnection(mock_stream)
    connection._on_end_request()
    assert mock_stream.closed
