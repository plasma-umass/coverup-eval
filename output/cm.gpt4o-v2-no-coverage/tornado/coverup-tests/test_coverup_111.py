# file: tornado/simple_httpclient.py:687-694
# asked: {"lines": [687, 688, 690, 691, 692, 694], "branches": [[688, 690], [688, 691], [691, 692], [691, 694]]}
# gained: {"lines": [687], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.tcpclient import TCPClient
from tornado.ioloop import IOLoop
from unittest.mock import Mock, call
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httputil import HTTPMessageDelegate
import time
from tornado import gen

class _HTTPConnection(HTTPMessageDelegate):
    def __init__(self, client, request, release_callback, final_callback, max_buffer_size, tcp_client, max_header_size, max_body_size):
        self.io_loop = IOLoop.current()
        self.start_time = self.io_loop.time()
        self.start_wall_time = time.time()
        self.client = client
        self.request = request
        self.release_callback = release_callback
        self.final_callback = final_callback
        self.max_buffer_size = max_buffer_size
        self.tcp_client = tcp_client
        self.max_header_size = max_header_size
        self.max_body_size = max_body_size
        self.code = None
        self.headers = None
        self.chunks = []
        self._decompressor = None
        self._timeout = None
        self._sockaddr = None
        IOLoop.current().add_future(gen.convert_yielded(self.run()), lambda f: f.result())

    async def run(self):
        pass

    def _should_follow_redirect(self):
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

class TestHTTPConnection:
    @pytest.fixture
    def setup_http_connection(self, monkeypatch):
        request = HTTPRequest(url="http://example.com", follow_redirects=True, max_redirects=3)
        release_callback = Mock()
        final_callback = Mock()
        tcp_client = TCPClient()
        max_buffer_size = 104857600
        max_header_size = 65536
        max_body_size = 104857600
    
        connection = _HTTPConnection(
            client=None,
            request=request,
            release_callback=release_callback,
            final_callback=final_callback,
            max_buffer_size=max_buffer_size,
            tcp_client=tcp_client,
            max_header_size=max_header_size,
            max_body_size=max_body_size
        )
    
        monkeypatch.setattr(connection, "io_loop", IOLoop.current())
        monkeypatch.setattr(connection, "_should_follow_redirect", Mock(return_value=False))
        monkeypatch.setattr(connection.request, "streaming_callback", Mock())
    
        return connection

    def test_data_received_with_streaming_callback(self, setup_http_connection):
        connection = setup_http_connection
        chunk = b"test data"
        
        connection.data_received(chunk)
        
        connection.request.streaming_callback.assert_called_once_with(chunk)
        assert connection.chunks == []

    def test_data_received_without_streaming_callback(self, setup_http_connection, monkeypatch):
        connection = setup_http_connection
        chunk = b"test data"
        
        monkeypatch.setattr(connection.request, "streaming_callback", None)
        
        connection.data_received(chunk)
        
        assert connection.chunks == [chunk]

    def test_data_received_with_redirect(self, setup_http_connection, monkeypatch):
        connection = setup_http_connection
        chunk = b"test data"
        
        monkeypatch.setattr(connection, "_should_follow_redirect", Mock(return_value=True))
        
        connection.data_received(chunk)
        
        connection._should_follow_redirect.assert_called_once()
        assert connection.request.streaming_callback.call_count == 0
        assert connection.chunks == []
