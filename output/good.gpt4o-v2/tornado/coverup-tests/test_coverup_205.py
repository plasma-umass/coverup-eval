# file: tornado/simple_httpclient.py:542-576
# asked: {"lines": [548, 549, 550, 551, 552, 554, 555, 556, 557, 558, 559, 560, 561, 565, 569, 570, 576], "branches": [[548, 549], [548, 576], [550, 551], [550, 555], [551, 552], [551, 554], [565, 569], [565, 570]]}
# gained: {"lines": [548, 549, 550, 551, 552, 554, 555, 556, 557, 558, 559, 560, 561, 565, 569, 570, 576], "branches": [[548, 549], [548, 576], [550, 551], [550, 555], [551, 552], [551, 554], [565, 569]]}

import pytest
from tornado.simple_httpclient import _HTTPConnection, HTTPStreamClosedError
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.iostream import StreamClosedError
from tornado.tcpclient import TCPClient
from unittest.mock import MagicMock

@pytest.fixture
def http_connection():
    request = HTTPRequest(url="http://example.com")
    connection = _HTTPConnection(
        client=None,
        request=request,
        release_callback=MagicMock(),
        final_callback=MagicMock(),
        max_buffer_size=1024,
        tcp_client=TCPClient(),
        max_header_size=1024,
        max_body_size=1024
    )
    connection.io_loop = MagicMock()
    connection.start_time = 0
    connection.start_wall_time = 0
    return connection

def test_handle_exception_with_final_callback_and_stream_closed_error_without_real_error(http_connection):
    error = StreamClosedError()
    http_connection._remove_timeout = MagicMock()
    http_connection._run_callback = MagicMock()
    http_connection.stream = MagicMock()

    result = http_connection._handle_exception(StreamClosedError, error, None)

    http_connection._remove_timeout.assert_called_once()
    http_connection._run_callback.assert_called_once()
    assert isinstance(http_connection._run_callback.call_args[0][0], HTTPResponse)
    assert http_connection._run_callback.call_args[0][0].error.code == 599
    http_connection.stream.close.assert_called_once()
    assert result is True

def test_handle_exception_with_final_callback_and_stream_closed_error_with_real_error(http_connection):
    real_error = Exception("Real error")
    error = StreamClosedError(real_error)
    http_connection._remove_timeout = MagicMock()
    http_connection._run_callback = MagicMock()
    http_connection.stream = MagicMock()

    result = http_connection._handle_exception(StreamClosedError, error, None)

    http_connection._remove_timeout.assert_called_once()
    http_connection._run_callback.assert_called_once()
    assert http_connection._run_callback.call_args[0][0].error == real_error
    http_connection.stream.close.assert_called_once()
    assert result is True

def test_handle_exception_with_final_callback_and_other_error(http_connection):
    error = Exception("Some error")
    http_connection._remove_timeout = MagicMock()
    http_connection._run_callback = MagicMock()
    http_connection.stream = MagicMock()

    result = http_connection._handle_exception(Exception, error, None)

    http_connection._remove_timeout.assert_called_once()
    http_connection._run_callback.assert_called_once()
    assert http_connection._run_callback.call_args[0][0].error == error
    http_connection.stream.close.assert_called_once()
    assert result is True

def test_handle_exception_without_final_callback(http_connection):
    http_connection.final_callback = None
    error = Exception("Some error")

    result = http_connection._handle_exception(Exception, error, None)

    assert result is False

def test_handle_exception_without_final_callback_and_stream_closed_error(http_connection):
    http_connection.final_callback = None
    error = StreamClosedError()

    result = http_connection._handle_exception(StreamClosedError, error, None)

    assert result is True
