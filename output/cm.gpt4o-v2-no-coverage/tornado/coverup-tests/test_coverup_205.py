# file: tornado/simple_httpclient.py:542-576
# asked: {"lines": [554], "branches": [[551, 554]]}
# gained: {"lines": [554], "branches": [[551, 554]]}

import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse, HTTPError
from tornado.iostream import StreamClosedError
from tornado import httputil
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from unittest.mock import Mock, patch
from types import TracebackType
from typing import Optional, Type

class HTTPStreamClosedError(HTTPError):
    def __init__(self, message: str) -> None:
        super().__init__(599, message=message)

from tornado.simple_httpclient import _HTTPConnection

class TestHTTPConnection:
    @pytest.fixture
    def setup_http_connection(self):
        request = HTTPRequest(url="http://example.com")
        release_callback = Mock()
        final_callback = Mock()
        tcp_client = Mock(spec=TCPClient)
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
        return connection, final_callback

    def test_handle_exception_with_final_callback(self, setup_http_connection):
        connection, final_callback = setup_http_connection
        connection.final_callback = final_callback
        connection._remove_timeout = Mock()
        connection._run_callback = Mock()
        connection.io_loop = Mock(spec=IOLoop)
        connection.io_loop.time.return_value = 1000
        connection.start_time = 500
        connection.start_wall_time = 100

        value = StreamClosedError()
        value.real_error = None

        result = connection._handle_exception(StreamClosedError, value, None)
        
        connection._remove_timeout.assert_called_once()
        connection._run_callback.assert_called_once()
        assert result is True

    def test_handle_exception_without_final_callback(self, setup_http_connection):
        connection, _ = setup_http_connection
        connection.final_callback = None

        value = StreamClosedError()
        result = connection._handle_exception(StreamClosedError, value, None)
        
        assert result is True

        value = Exception()
        result = connection._handle_exception(Exception, value, None)
        
        assert result is False

    def test_handle_exception_with_real_error(self, setup_http_connection):
        connection, final_callback = setup_http_connection
        connection.final_callback = final_callback
        connection._remove_timeout = Mock()
        connection._run_callback = Mock()
        connection.io_loop = Mock(spec=IOLoop)
        connection.io_loop.time.return_value = 1000
        connection.start_time = 500
        connection.start_wall_time = 100

        real_error = Exception("Real error")
        value = StreamClosedError()
        value.real_error = real_error

        result = connection._handle_exception(StreamClosedError, value, None)
        
        connection._remove_timeout.assert_called_once()
        connection._run_callback.assert_called_once()
        assert result is True
