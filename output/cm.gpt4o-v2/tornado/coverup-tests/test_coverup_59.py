# file: tornado/simple_httpclient.py:578-586
# asked: {"lines": [578, 579, 580, 581, 582, 583, 584, 585, 586], "branches": [[579, 0], [579, 580], [581, 582], [581, 583]]}
# gained: {"lines": [578], "branches": []}

import pytest
from tornado import httputil
from tornado.iostream import IOStream
from tornado.httpclient import HTTPRequest, HTTPResponse, HTTPError
from tornado.simple_httpclient import HTTPStreamClosedError
from tornado.tcpclient import TCPClient
from tornado.ioloop import IOLoop
from unittest.mock import Mock, patch
import sys

class _HTTPConnection(httputil.HTTPMessageDelegate):
    def __init__(self, final_callback=None):
        self.final_callback = final_callback
        self.stream = Mock()
        self.stream.error = None

    def on_connection_close(self) -> None:
        if self.final_callback is not None:
            message = "Connection closed"
            if self.stream.error:
                raise self.stream.error
            try:
                raise HTTPStreamClosedError(message)
            except HTTPStreamClosedError:
                self._handle_exception(*sys.exc_info())

    def _handle_exception(self, typ, value, tb):
        pass

@pytest.fixture
def connection():
    return _HTTPConnection(final_callback=Mock())

def test_on_connection_close_no_error(connection):
    with patch.object(connection, '_handle_exception') as mock_handle_exception:
        connection.on_connection_close()
        mock_handle_exception.assert_called_once()
        assert isinstance(mock_handle_exception.call_args[0][1], HTTPStreamClosedError)

def test_on_connection_close_with_error(connection):
    connection.stream.error = ValueError("Stream error")
    with pytest.raises(ValueError, match="Stream error"):
        connection.on_connection_close()
