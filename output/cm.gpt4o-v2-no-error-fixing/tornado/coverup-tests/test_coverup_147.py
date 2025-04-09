# file: tornado/simple_httpclient.py:578-586
# asked: {"lines": [579, 580, 581, 582, 583, 584, 585, 586], "branches": [[579, 0], [579, 580], [581, 582], [581, 583]]}
# gained: {"lines": [579, 580, 581, 582, 583, 584, 585, 586], "branches": [[579, 580], [581, 582], [581, 583]]}

import pytest
from tornado.iostream import IOStream
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.simple_httpclient import _HTTPConnection, HTTPStreamClosedError
from tornado import httputil
from unittest.mock import Mock, patch

@pytest.fixture
def mock_http_connection():
    request = HTTPRequest(url="http://example.com")
    release_callback = Mock()
    final_callback = Mock()
    tcp_client = Mock()
    connection = _HTTPConnection(
        client=None,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=1024,
        tcp_client=tcp_client,
        max_header_size=1024,
        max_body_size=1024,
    )
    connection.stream = Mock(spec=IOStream)
    return connection

def test_on_connection_close_with_final_callback_and_stream_error(mock_http_connection):
    mock_http_connection.final_callback = Mock()
    mock_http_connection.stream.error = HTTPStreamClosedError("Stream error")
    
    with pytest.raises(HTTPStreamClosedError):
        mock_http_connection.on_connection_close()

def test_on_connection_close_with_final_callback_and_no_stream_error(mock_http_connection):
    mock_http_connection.final_callback = Mock()
    mock_http_connection.stream.error = None
    
    with patch.object(mock_http_connection, '_handle_exception') as mock_handle_exception:
        mock_http_connection.on_connection_close()
        mock_handle_exception.assert_called_once()
