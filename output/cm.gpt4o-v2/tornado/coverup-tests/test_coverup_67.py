# file: tornado/simple_httpclient.py:499-512
# asked: {"lines": [499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 512], "branches": []}
# gained: {"lines": [499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 512], "branches": []}

import pytest
import socket
from tornado.simple_httpclient import _HTTPConnection
from tornado.iostream import IOStream
from tornado.http1connection import HTTP1Connection

class MockStream(IOStream):
    def __init__(self):
        super().__init__(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

    def set_nodelay(self, value: bool):
        self.nodelay = value

class MockRequest:
    decompress_response = True

class MockHTTPConnection(_HTTPConnection):
    def __init__(self):
        self.max_header_size = 1024
        self.max_body_size = 1024
        self.request = MockRequest()
        self._sockaddr = ('127.0.0.1', 8888)

@pytest.fixture
def mock_stream():
    return MockStream()

@pytest.fixture
def mock_http_connection():
    return MockHTTPConnection()

def test_create_connection(mock_stream, mock_http_connection):
    connection = mock_http_connection._create_connection(mock_stream)
    assert isinstance(connection, HTTP1Connection)
    assert mock_stream.nodelay == True
    assert connection.stream == mock_stream
    assert connection.params.no_keep_alive == True
    assert connection.params.max_header_size == 1024
    assert connection.params.max_body_size == 1024
    assert connection.params.decompress == True
    assert connection.context == ('127.0.0.1', 8888)
