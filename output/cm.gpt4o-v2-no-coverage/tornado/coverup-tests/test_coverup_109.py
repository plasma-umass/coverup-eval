# file: tornado/simple_httpclient.py:529-533
# asked: {"lines": [529, 530, 531, 532, 533], "branches": [[530, 0], [530, 531]]}
# gained: {"lines": [529, 530, 531, 532, 533], "branches": [[530, 0], [530, 531]]}

import pytest
from unittest import mock
from tornado.simple_httpclient import _HTTPConnection
from tornado.httpclient import HTTPRequest
from tornado.tcpclient import TCPClient

class TestHTTPConnection:
    @pytest.fixture
    def connection(self):
        client = mock.Mock()
        request = HTTPRequest(url="http://example.com")
        release_callback = mock.Mock()
        final_callback = mock.Mock()
        max_buffer_size = 1024
        tcp_client = TCPClient()
        max_header_size = 1024
        max_body_size = 1024

        return _HTTPConnection(client, request, release_callback, final_callback, max_buffer_size, tcp_client, max_header_size, max_body_size)

    def test_release_with_callback(self, connection):
        mock_callback = mock.Mock()
        connection.release_callback = mock_callback

        connection._release()

        mock_callback.assert_called_once()
        assert connection.release_callback is None

    def test_release_without_callback(self, connection):
        connection.release_callback = None

        connection._release()

        assert connection.release_callback is None
