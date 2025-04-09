# file: tornado/simple_httpclient.py:480-492
# asked: {"lines": [480, 487, 488, 489, 490, 491], "branches": [[489, 0], [489, 490]]}
# gained: {"lines": [480, 487, 488, 489, 490, 491], "branches": [[489, 0], [489, 490]]}

import pytest
from tornado.simple_httpclient import _HTTPConnection, HTTPTimeoutError, SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado.tcpclient import TCPClient
from unittest.mock import Mock

@pytest.fixture
def http_connection():
    client = Mock(spec=SimpleAsyncHTTPClient)
    request = Mock(spec=HTTPRequest)
    release_callback = Mock()
    final_callback = Mock()
    max_buffer_size = 1024
    tcp_client = Mock(spec=TCPClient)
    max_header_size = 2048
    max_body_size = 4096

    conn = _HTTPConnection(
        client=client,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=max_buffer_size,
        tcp_client=tcp_client,
        max_header_size=max_header_size,
        max_body_size=max_body_size
    )
    conn._handle_exception = Mock()
    return conn

def test_on_timeout_with_info(http_connection):
    http_connection._on_timeout(info="test_info")
    assert http_connection._timeout is None
    http_connection._handle_exception.assert_called_once()
    args, kwargs = http_connection._handle_exception.call_args
    assert args[0] == HTTPTimeoutError
    assert isinstance(args[1], HTTPTimeoutError)
    assert str(args[1]) == "Timeout test_info"
    assert args[2] is None

def test_on_timeout_without_info(http_connection):
    http_connection._on_timeout()
    assert http_connection._timeout is None
    http_connection._handle_exception.assert_called_once()
    args, kwargs = http_connection._handle_exception.call_args
    assert args[0] == HTTPTimeoutError
    assert isinstance(args[1], HTTPTimeoutError)
    assert str(args[1]) == "Timeout"
    assert args[2] is None

def test_on_timeout_no_final_callback(monkeypatch):
    client = Mock(spec=SimpleAsyncHTTPClient)
    request = Mock(spec=HTTPRequest)
    release_callback = Mock()
    final_callback = None
    max_buffer_size = 1024
    tcp_client = Mock(spec=TCPClient)
    max_header_size = 2048
    max_body_size = 4096

    conn = _HTTPConnection(
        client=client,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=max_buffer_size,
        tcp_client=tcp_client,
        max_header_size=max_header_size,
        max_body_size=max_body_size
    )
    mock_handle_exception = Mock()
    monkeypatch.setattr(conn, "_handle_exception", mock_handle_exception)
    conn._on_timeout(info="test_info")
    assert conn._timeout is None
    mock_handle_exception.assert_not_called()
