# file: tornado/simple_httpclient.py:542-576
# asked: {"lines": [], "branches": [[565, 570]]}
# gained: {"lines": [], "branches": [[565, 570]]}

import pytest
from tornado.simple_httpclient import _HTTPConnection, HTTPStreamClosedError
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpclient import TCPClient
from unittest.mock import MagicMock, patch

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
    connection.stream = MagicMock()
    return connection

def test_handle_exception_with_stream_closed_error(http_connection):
    error = StreamClosedError()
    error.real_error = None

    with patch.object(http_connection, '_remove_timeout') as mock_remove_timeout, \
         patch.object(http_connection, '_run_callback') as mock_run_callback:
        result = http_connection._handle_exception(StreamClosedError, error, None)

    mock_remove_timeout.assert_called_once()
    mock_run_callback.assert_called_once()
    http_connection.stream.close.assert_called_once()
    assert result is True

def test_handle_exception_with_other_error(http_connection):
    error = Exception("Some other error")

    with patch.object(http_connection, '_remove_timeout') as mock_remove_timeout, \
         patch.object(http_connection, '_run_callback') as mock_run_callback:
        result = http_connection._handle_exception(Exception, error, None)

    mock_remove_timeout.assert_called_once()
    mock_run_callback.assert_called_once()
    http_connection.stream.close.assert_called_once()
    assert result is True

def test_handle_exception_without_final_callback():
    request = HTTPRequest(url="http://example.com")
    release_callback = MagicMock()
    tcp_client = TCPClient()
    connection = _HTTPConnection(
        client=None,
        request=request,
        release_callback=release_callback,
        final_callback=None,
        max_buffer_size=104857600,
        tcp_client=tcp_client,
        max_header_size=104857600,
        max_body_size=104857600
    )
    error = StreamClosedError()

    result = connection._handle_exception(StreamClosedError, error, None)
    assert result is True

    error = Exception("Some other error")
    result = connection._handle_exception(Exception, error, None)
    assert result is False

def test_handle_exception_with_stream(http_connection):
    error = StreamClosedError()
    error.real_error = None

    with patch.object(http_connection, '_remove_timeout') as mock_remove_timeout, \
         patch.object(http_connection, '_run_callback') as mock_run_callback:
        delattr(http_connection, 'stream')
        result = http_connection._handle_exception(StreamClosedError, error, None)

    mock_remove_timeout.assert_called_once()
    mock_run_callback.assert_called_once()
    assert result is True
