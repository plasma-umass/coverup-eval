# file: tornado/simple_httpclient.py:542-576
# asked: {"lines": [542, 548, 549, 550, 551, 552, 554, 555, 556, 557, 558, 559, 560, 561, 565, 569, 570, 576], "branches": [[548, 549], [548, 576], [550, 551], [550, 555], [551, 552], [551, 554], [565, 569], [565, 570]]}
# gained: {"lines": [542, 548, 549, 550, 551, 552, 555, 556, 557, 558, 559, 560, 561, 565, 569, 570, 576], "branches": [[548, 549], [548, 576], [550, 551], [550, 555], [551, 552], [565, 569], [565, 570]]}

import pytest
from tornado.simple_httpclient import _HTTPConnection, HTTPStreamClosedError, SimpleAsyncHTTPClient
from tornado.httpclient import HTTPResponse, HTTPRequest
from tornado.iostream import StreamClosedError
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from unittest.mock import MagicMock
from types import TracebackType
from typing import Optional, Type

@pytest.fixture
def http_connection():
    request = HTTPRequest(url="http://example.com")
    release_callback = MagicMock()
    final_callback = MagicMock()
    tcp_client = TCPClient()
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
    connection._remove_timeout = MagicMock()
    connection._run_callback = MagicMock()
    connection.start_time = connection.io_loop.time()
    connection.start_wall_time = connection.io_loop.time()
    return connection

def test_handle_exception_with_final_callback_and_stream_closed_error(http_connection):
    error = StreamClosedError()
    error.real_error = None

    result = http_connection._handle_exception(StreamClosedError, error, None)

    http_connection._remove_timeout.assert_called_once()
    http_connection._run_callback.assert_called_once()
    assert isinstance(http_connection._run_callback.call_args[0][0], HTTPResponse)
    assert http_connection._run_callback.call_args[0][0].code == 599
    assert isinstance(http_connection._run_callback.call_args[0][0].error, HTTPStreamClosedError)
    assert result is True

def test_handle_exception_with_final_callback_and_other_error(http_connection):
    error = Exception("Some error")

    result = http_connection._handle_exception(Exception, error, None)

    http_connection._remove_timeout.assert_called_once()
    http_connection._run_callback.assert_called_once()
    assert isinstance(http_connection._run_callback.call_args[0][0], HTTPResponse)
    assert http_connection._run_callback.call_args[0][0].code == 599
    assert http_connection._run_callback.call_args[0][0].error == error
    assert result is True

def test_handle_exception_without_final_callback_and_stream_closed_error(http_connection):
    http_connection.final_callback = None
    error = StreamClosedError()

    result = http_connection._handle_exception(StreamClosedError, error, None)

    assert result is True

def test_handle_exception_without_final_callback_and_other_error(http_connection):
    http_connection.final_callback = None
    error = Exception("Some error")

    result = http_connection._handle_exception(Exception, error, None)

    assert result is False

def test_handle_exception_with_stream(http_connection):
    http_connection.stream = MagicMock()
    error = StreamClosedError()
    error.real_error = None

    result = http_connection._handle_exception(StreamClosedError, error, None)

    http_connection.stream.close.assert_called_once()
    assert result is True
