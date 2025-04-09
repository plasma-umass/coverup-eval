# file: tornado/simple_httpclient.py:684-685
# asked: {"lines": [684, 685], "branches": []}
# gained: {"lines": [684, 685], "branches": []}

import pytest
from tornado.iostream import IOStream
from tornado.simple_httpclient import _HTTPConnection
from tornado.httpclient import HTTPRequest
from tornado.tcpclient import TCPClient
from tornado.ioloop import IOLoop
from unittest.mock import MagicMock

@pytest.fixture
def http_connection(monkeypatch):
    request = HTTPRequest(url="http://example.com")
    release_callback = MagicMock()
    final_callback = MagicMock()
    tcp_client = TCPClient()
    max_buffer_size = 104857600
    max_header_size = 104857600
    max_body_size = 104857600

    conn = _HTTPConnection(
        client=None,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=max_buffer_size,
        tcp_client=tcp_client,
        max_header_size=max_header_size,
        max_body_size=max_body_size
    )

    stream = MagicMock(spec=IOStream)
    conn.stream = stream

    yield conn

    # Clean up
    IOLoop.current().stop()
    stream.close.assert_called_once()

def test_on_end_request(http_connection):
    http_connection._on_end_request()
    http_connection.stream.close.assert_called_once()
