# file: tornado/simple_httpclient.py:578-586
# asked: {"lines": [579, 580, 581, 582, 583, 584, 585, 586], "branches": [[579, 0], [579, 580], [581, 582], [581, 583]]}
# gained: {"lines": [579, 580, 581, 582, 583, 584, 585, 586], "branches": [[579, 0], [579, 580], [581, 582], [581, 583]]}

import pytest
from tornado.simple_httpclient import HTTPStreamClosedError, _HTTPConnection
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from unittest.mock import Mock, patch

class MockStream:
    def __init__(self, error=None):
        self.error = error

class TestHTTPConnection(_HTTPConnection):
    def __init__(self, final_callback=None, stream_error=None):
        self.io_loop = IOLoop.current()
        self.final_callback = final_callback
        self.stream = MockStream(error=stream_error)
        self.exception_handled = False

    def _handle_exception(self, typ, value, tb):
        self.exception_handled = True

@pytest.fixture
def mock_http_connection():
    return TestHTTPConnection(final_callback=lambda response: None)

def test_on_connection_close_with_final_callback_and_stream_error(mock_http_connection):
    mock_http_connection.stream.error = ValueError("Stream error")
    with pytest.raises(ValueError, match="Stream error"):
        mock_http_connection.on_connection_close()

def test_on_connection_close_with_final_callback_and_no_stream_error(mock_http_connection):
    mock_http_connection.on_connection_close()
    assert mock_http_connection.exception_handled

def test_on_connection_close_without_final_callback(mock_http_connection):
    mock_http_connection.final_callback = None
    mock_http_connection.on_connection_close()
    assert not mock_http_connection.exception_handled
