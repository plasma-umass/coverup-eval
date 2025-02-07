# file: tornado/simple_httpclient.py:687-694
# asked: {"lines": [687, 688, 690, 691, 692, 694], "branches": [[688, 690], [688, 691], [691, 692], [691, 694]]}
# gained: {"lines": [687, 688, 690, 691, 692, 694], "branches": [[688, 690], [688, 691], [691, 692], [691, 694]]}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from unittest.mock import Mock
from tornado.simple_httpclient import _HTTPConnection

class TestHTTPConnection:
    
    @pytest.fixture
    def setup_http_connection(self, monkeypatch):
        request = HTTPRequest(url="http://example.com")
        release_callback = Mock()
        final_callback = Mock()
        tcp_client = Mock(spec=TCPClient)
        
        connection = _HTTPConnection(
            client=None,
            request=request,
            release_callback=release_callback,
            final_callback=final_callback,
            max_buffer_size=104857600,
            tcp_client=tcp_client,
            max_header_size=104857600,
            max_body_size=104857600
        )
        
        monkeypatch.setattr(connection, "_should_follow_redirect", Mock(return_value=False))
        monkeypatch.setattr(connection, "request", request)
        monkeypatch.setattr(connection, "chunks", [])
        
        return connection

    def test_data_received_no_redirect(self, setup_http_connection):
        connection = setup_http_connection
        chunk = b"test data"
        
        connection.data_received(chunk)
        
        assert connection.chunks == [chunk]

    def test_data_received_with_redirect(self, setup_http_connection, monkeypatch):
        connection = setup_http_connection
        monkeypatch.setattr(connection, "_should_follow_redirect", Mock(return_value=True))
        chunk = b"test data"
        
        connection.data_received(chunk)
        
        assert connection.chunks == []

    def test_data_received_with_streaming_callback(self, setup_http_connection, monkeypatch):
        connection = setup_http_connection
        streaming_callback = Mock()
        monkeypatch.setattr(connection.request, "streaming_callback", streaming_callback)
        chunk = b"test data"
        
        connection.data_received(chunk)
        
        streaming_callback.assert_called_once_with(chunk)
