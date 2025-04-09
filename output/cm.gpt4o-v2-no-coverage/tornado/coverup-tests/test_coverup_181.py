# file: tornado/simple_httpclient.py:499-512
# asked: {"lines": [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 512], "branches": []}
# gained: {"lines": [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 512], "branches": []}

import pytest
from tornado.simple_httpclient import _HTTPConnection
from tornado.iostream import IOStream
from tornado.http1connection import HTTP1Connection, HTTP1ConnectionParameters
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.tcpclient import TCPClient
from unittest.mock import Mock

@pytest.fixture
def mock_stream():
    stream = Mock(spec=IOStream)
    return stream

@pytest.fixture
def mock_http_connection_params():
    params = HTTP1ConnectionParameters(
        no_keep_alive=True,
        max_header_size=1024,
        max_body_size=2048,
        decompress=True
    )
    return params

@pytest.fixture
def mock_http_connection(mock_stream, mock_http_connection_params):
    client = Mock()
    request = Mock(spec=HTTPRequest)
    request.decompress_response = True
    release_callback = Mock()
    final_callback = Mock()
    max_buffer_size = 104857600
    tcp_client = Mock(spec=TCPClient)
    max_header_size = 1024
    max_body_size = 2048

    connection = _HTTPConnection(
        client=client,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=max_buffer_size,
        tcp_client=tcp_client,
        max_header_size=max_header_size,
        max_body_size=max_body_size
    )
    connection._sockaddr = ('127.0.0.1', 8888)
    return connection

def test_create_connection(mock_http_connection, mock_stream):
    connection = mock_http_connection._create_connection(mock_stream)
    
    # Assertions to verify the connection is created correctly
    assert isinstance(connection, HTTP1Connection)
    mock_stream.set_nodelay.assert_called_once_with(True)
    assert connection.is_client is True
    assert connection.params.no_keep_alive is True
    assert connection.params.max_header_size == 1024
    assert connection.params.max_body_size == 2048
    assert connection.params.decompress is True
    assert connection.context == ('127.0.0.1', 8888)
