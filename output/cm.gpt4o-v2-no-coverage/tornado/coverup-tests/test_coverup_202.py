# file: tornado/simple_httpclient.py:684-685
# asked: {"lines": [685], "branches": []}
# gained: {"lines": [685], "branches": []}

import pytest
from unittest.mock import Mock
from tornado.simple_httpclient import _HTTPConnection
from tornado.httputil import HTTPMessageDelegate
from tornado.iostream import IOStream
from tornado.httpclient import HTTPRequest

class TestHTTPConnection:
    @pytest.fixture
    def setup_http_connection(self, monkeypatch):
        # Mock the necessary components
        mock_client = Mock()
        mock_request = Mock(spec=HTTPRequest)
        mock_release_callback = Mock()
        mock_final_callback = Mock()
        mock_tcp_client = Mock()
        mock_stream = Mock(spec=IOStream)
    
        # Create an instance of _HTTPConnection
        connection = _HTTPConnection(
            client=mock_client,
            request=mock_request,
            release_callback=mock_release_callback,
            final_callback=mock_final_callback,
            max_buffer_size=1024,
            tcp_client=mock_tcp_client,
            max_header_size=1024,
            max_body_size=1024
        )
    
        # Manually set the stream attribute
        connection.stream = mock_stream
        
        return connection, mock_stream

    def test_on_end_request(self, setup_http_connection):
        connection, mock_stream = setup_http_connection
        
        # Call the method
        connection._on_end_request()
        
        # Assert the stream's close method was called
        mock_stream.close.assert_called_once()
