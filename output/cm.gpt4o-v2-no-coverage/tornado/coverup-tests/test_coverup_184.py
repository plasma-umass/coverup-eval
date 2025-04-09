# file: tornado/simple_httpclient.py:578-586
# asked: {"lines": [579, 580, 581, 582, 583, 584, 585, 586], "branches": [[579, 0], [579, 580], [581, 582], [581, 583]]}
# gained: {"lines": [579, 580, 581, 582, 583, 584, 585, 586], "branches": [[579, 580], [581, 582], [581, 583]]}

import pytest
from tornado.simple_httpclient import _HTTPConnection, HTTPStreamClosedError
from tornado.httputil import HTTPMessageDelegate
from unittest import mock

class MockStream:
    def __init__(self, error=None):
        self.error = error

class TestHTTPConnection:
    @pytest.fixture
    def setup_http_connection(self):
        self.connection = _HTTPConnection(
            client=None,
            request=mock.Mock(),
            release_callback=mock.Mock(),
            final_callback=mock.Mock(),
            max_buffer_size=mock.Mock(),
            tcp_client=mock.Mock(),
            max_header_size=mock.Mock(),
            max_body_size=mock.Mock()
        )
        self.connection.stream = MockStream()

    def test_on_connection_close_no_error(self, setup_http_connection):
        self.connection.stream.error = None
        with mock.patch.object(self.connection, '_handle_exception', autospec=True) as mock_handle_exception:
            self.connection.on_connection_close()
            mock_handle_exception.assert_called_once()
            exc_info = mock_handle_exception.call_args[0]
            assert isinstance(exc_info[1], HTTPStreamClosedError)
            assert str(exc_info[1]) == "Connection closed"

    def test_on_connection_close_with_error(self, setup_http_connection):
        self.connection.stream.error = ValueError("Stream error")
        with pytest.raises(ValueError, match="Stream error"):
            self.connection.on_connection_close()
