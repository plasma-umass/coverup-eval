# file: tornado/simple_httpclient.py:687-694
# asked: {"lines": [687, 688, 690, 691, 692, 694], "branches": [[688, 690], [688, 691], [691, 692], [691, 694]]}
# gained: {"lines": [687], "branches": []}

import pytest
from tornado import httputil
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class MockRequest:
    def __init__(self, streaming_callback=None):
        self.streaming_callback = streaming_callback

class MockHTTPConnection(httputil.HTTPMessageDelegate):
    def __init__(self, request):
        self.request = request
        self.chunks = []

    def _should_follow_redirect(self):
        return False

    def data_received(self, chunk: bytes) -> None:
        if self._should_follow_redirect():
            return
        if self.request.streaming_callback is not None:
            self.request.streaming_callback(chunk)
        else:
            self.chunks.append(chunk)

@pytest.fixture
def mock_http_connection():
    request = MockRequest()
    return MockHTTPConnection(request)

def test_data_received_no_redirect_no_streaming_callback(mock_http_connection):
    mock_http_connection._should_follow_redirect = lambda: False
    mock_http_connection.data_received(b"test_chunk")
    assert mock_http_connection.chunks == [b"test_chunk"]

def test_data_received_with_redirect(mock_http_connection):
    mock_http_connection._should_follow_redirect = lambda: True
    mock_http_connection.data_received(b"test_chunk")
    assert mock_http_connection.chunks == []

def test_data_received_with_streaming_callback(mock_http_connection):
    chunks = []
    def streaming_callback(chunk):
        chunks.append(chunk)
    
    mock_http_connection.request.streaming_callback = streaming_callback
    mock_http_connection.data_received(b"test_chunk")
    assert chunks == [b"test_chunk"]
    assert mock_http_connection.chunks == []
