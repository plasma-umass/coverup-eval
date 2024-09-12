# file: tornado/simple_httpclient.py:687-694
# asked: {"lines": [687, 688, 690, 691, 692, 694], "branches": [[688, 690], [688, 691], [691, 692], [691, 694]]}
# gained: {"lines": [687], "branches": []}

import pytest
from tornado import httputil
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from unittest.mock import Mock

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
def mock_request():
    return MockRequest()

@pytest.fixture
def mock_http_connection(mock_request):
    return MockHTTPConnection(mock_request)

def test_data_received_no_redirect_no_streaming_callback(mock_http_connection):
    mock_http_connection.data_received(b'test_chunk')
    assert mock_http_connection.chunks == [b'test_chunk']

def test_data_received_no_redirect_with_streaming_callback(mock_request, mock_http_connection):
    mock_callback = Mock()
    mock_request.streaming_callback = mock_callback
    mock_http_connection.data_received(b'test_chunk')
    mock_callback.assert_called_once_with(b'test_chunk')

def test_data_received_with_redirect(monkeypatch, mock_http_connection):
    monkeypatch.setattr(mock_http_connection, '_should_follow_redirect', lambda: True)
    mock_http_connection.data_received(b'test_chunk')
    assert mock_http_connection.chunks == []
