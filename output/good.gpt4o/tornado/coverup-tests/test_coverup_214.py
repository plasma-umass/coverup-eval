# file tornado/simple_httpclient.py:578-586
# lines [579, 580, 581, 582, 583, 584, 585, 586]
# branches ['579->exit', '579->580', '581->582', '581->583']

import pytest
from tornado.simple_httpclient import _HTTPConnection
from tornado.httputil import HTTPMessageDelegate
from tornado.iostream import IOStream, StreamClosedError
import sys

class MockStream:
    def __init__(self, error=None):
        self.error = error

@pytest.fixture
def mock_stream():
    return MockStream()

@pytest.fixture
def http_connection(mock_stream):
    class TestHTTPConnection(_HTTPConnection):
        def __init__(self, stream):
            self.stream = stream
            self.final_callback = lambda: None
            self._handle_exception_called = False

        def _handle_exception(self, typ, value, tb):
            self._handle_exception_called = True

    return TestHTTPConnection(mock_stream)

def test_on_connection_close_no_error(http_connection):
    http_connection.final_callback = lambda: None
    http_connection.on_connection_close()
    assert http_connection._handle_exception_called

def test_on_connection_close_with_error(http_connection, mock_stream):
    mock_stream.error = ValueError("Test error")
    with pytest.raises(ValueError, match="Test error"):
        http_connection.on_connection_close()
    assert not http_connection._handle_exception_called
