# file: tornado/simple_httpclient.py:535-540
# asked: {"lines": [], "branches": [[537, 0]]}
# gained: {"lines": [], "branches": [[537, 0]]}

import pytest
from unittest.mock import Mock, call
from tornado.httpclient import HTTPResponse, HTTPRequest
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import _HTTPConnection
from tornado.tcpclient import TCPClient

@pytest.fixture
def http_connection():
    io_loop = IOLoop.current()
    request = Mock(spec=HTTPRequest)
    release_callback = Mock()
    final_callback = Mock()
    tcp_client = Mock(spec=TCPClient)
    conn = _HTTPConnection(
        client=None,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=104857600,
        tcp_client=tcp_client,
        max_header_size=104857600,
        max_body_size=104857600
    )
    conn._release = Mock()
    conn.io_loop.add_callback = Mock()
    return conn

def test_run_callback_with_final_callback(http_connection):
    response = Mock(spec=HTTPResponse)
    final_callback = http_connection.final_callback
    http_connection._run_callback(response)
    
    http_connection._release.assert_called_once()
    http_connection.io_loop.add_callback.assert_called_once_with(final_callback, response)
    assert http_connection.final_callback is None

def test_run_callback_without_final_callback(http_connection):
    response = Mock(spec=HTTPResponse)
    http_connection.final_callback = None
    http_connection._run_callback(response)
    
    http_connection._release.assert_called_once()
    assert http_connection.final_callback is None
