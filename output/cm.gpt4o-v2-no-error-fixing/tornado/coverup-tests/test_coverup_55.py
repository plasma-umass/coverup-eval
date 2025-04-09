# file: tornado/simple_httpclient.py:687-694
# asked: {"lines": [687, 688, 690, 691, 692, 694], "branches": [[688, 690], [688, 691], [691, 692], [691, 694]]}
# gained: {"lines": [687], "branches": []}

import pytest
from tornado import httputil
from tornado.simple_httpclient import SimpleAsyncHTTPClient

class MockRequest:
    def __init__(self, follow_redirects=False, max_redirects=None, streaming_callback=None):
        self.follow_redirects = follow_redirects
        self.max_redirects = max_redirects
        self.streaming_callback = streaming_callback

class MockHTTPConnection(httputil.HTTPMessageDelegate):
    def __init__(self, request):
        self.request = request
        self.chunks = []
        self.code = 200
        self.headers = {"Location": "http://example.com"}

    def _should_follow_redirect(self) -> bool:
        if self.request.follow_redirects:
            assert self.request.max_redirects is not None
            return self.code in (301, 302, 303, 307, 308) and self.request.max_redirects > 0 and (self.headers is not None) and (self.headers.get('Location') is not None)
        return False

    def data_received(self, chunk: bytes) -> None:
        if self._should_follow_redirect():
            return
        if self.request.streaming_callback is not None:
            self.request.streaming_callback(chunk)
        else:
            self.chunks.append(chunk)

def test_data_received_no_redirect():
    request = MockRequest(follow_redirects=False)
    conn = MockHTTPConnection(request)
    conn.data_received(b"test_chunk")
    assert conn.chunks == [b"test_chunk"]

def test_data_received_with_redirect():
    request = MockRequest(follow_redirects=True, max_redirects=1)
    conn = MockHTTPConnection(request)
    conn.code = 302
    conn.data_received(b"test_chunk")
    assert conn.chunks == []

def test_data_received_with_streaming_callback():
    def mock_callback(chunk):
        mock_callback.chunks.append(chunk)
    mock_callback.chunks = []

    request = MockRequest(streaming_callback=mock_callback)
    conn = MockHTTPConnection(request)
    conn.data_received(b"test_chunk")
    assert mock_callback.chunks == [b"test_chunk"]
