# file: tornado/simple_httpclient.py:684-685
# asked: {"lines": [684, 685], "branches": []}
# gained: {"lines": [684, 685], "branches": []}

import pytest
from unittest.mock import MagicMock
from tornado.simple_httpclient import _HTTPConnection
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from tornado.iostream import IOStream

@pytest.fixture
def http_connection(mocker):
    request = HTTPRequest(url="http://example.com")
    release_callback = mocker.Mock()
    final_callback = mocker.Mock()
    tcp_client = mocker.Mock(spec=TCPClient)
    connection = _HTTPConnection(
        client=None,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=1024,
        tcp_client=tcp_client,
        max_header_size=1024,
        max_body_size=1024
    )
    connection.stream = mocker.Mock(spec=IOStream)
    return connection

def test_on_end_request(http_connection):
    http_connection._on_end_request()
    http_connection.stream.close.assert_called_once()
