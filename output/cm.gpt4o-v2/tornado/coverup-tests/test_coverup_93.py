# file: tornado/simple_httpclient.py:480-492
# asked: {"lines": [480, 487, 488, 489, 490, 491], "branches": [[489, 0], [489, 490]]}
# gained: {"lines": [480, 487, 488, 489, 490, 491], "branches": [[489, 0], [489, 490]]}

import pytest
from tornado.simple_httpclient import _HTTPConnection, HTTPTimeoutError
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.tcpclient import TCPClient
from tornado.ioloop import IOLoop
from unittest.mock import Mock

@pytest.fixture
def http_connection():
    client = Mock()
    request = HTTPRequest(url="http://example.com")
    release_callback = Mock()
    final_callback = Mock()
    max_buffer_size = 104857600
    tcp_client = TCPClient()
    max_header_size = 104857600
    max_body_size = 104857600

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
    connection._timeout = Mock()
    connection._handle_exception = Mock()
    return connection

def test_on_timeout_with_info(http_connection):
    http_connection._on_timeout(info="test_info")
    assert http_connection._timeout is None
    http_connection._handle_exception.assert_called_once()
    args, kwargs = http_connection._handle_exception.call_args
    assert args[0] == HTTPTimeoutError
    assert isinstance(args[1], HTTPTimeoutError)
    assert str(args[1]) == "Timeout test_info"

def test_on_timeout_without_info(http_connection):
    http_connection._on_timeout()
    assert http_connection._timeout is None
    http_connection._handle_exception.assert_called_once()
    args, kwargs = http_connection._handle_exception.call_args
    assert args[0] == HTTPTimeoutError
    assert isinstance(args[1], HTTPTimeoutError)
    assert str(args[1]) == "Timeout"

def test_on_timeout_no_final_callback(http_connection):
    http_connection.final_callback = None
    http_connection._on_timeout()
    assert http_connection._timeout is None
    http_connection._handle_exception.assert_not_called()
