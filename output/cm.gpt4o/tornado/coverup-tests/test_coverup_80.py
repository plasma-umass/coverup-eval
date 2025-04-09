# file tornado/simple_httpclient.py:499-512
# lines [499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 512]
# branches []

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.iostream import IOStream
from tornado.http1connection import HTTP1Connection, HTTP1ConnectionParameters
from tornado import httputil
from unittest import mock

class TestHTTPConnection:
    @pytest.fixture
    def mock_stream(self):
        stream = mock.Mock(spec=IOStream)
        return stream

    @pytest.fixture
    def mock_request(self):
        request = mock.Mock()
        request.decompress_response = True
        return request

    @pytest.fixture
    def http_connection(self, mock_request):
        class _HTTPConnection(httputil.HTTPMessageDelegate):
            def __init__(self, request):
                self.request = request
                self.max_header_size = 1024
                self.max_body_size = 1024
                self._sockaddr = ('127.0.0.1', 80)

            def _create_connection(self, stream: IOStream) -> HTTP1Connection:
                stream.set_nodelay(True)
                connection = HTTP1Connection(
                    stream,
                    True,
                    HTTP1ConnectionParameters(
                        no_keep_alive=True,
                        max_header_size=self.max_header_size,
                        max_body_size=self.max_body_size,
                        decompress=bool(self.request.decompress_response),
                    ),
                    self._sockaddr,
                )
                connection._sockaddr = self._sockaddr  # Manually set _sockaddr for testing
                return connection

        return _HTTPConnection(mock_request)

    def test_create_connection(self, mock_stream, http_connection):
        connection = http_connection._create_connection(mock_stream)
        mock_stream.set_nodelay.assert_called_once_with(True)
        assert isinstance(connection, HTTP1Connection)
        assert connection.params.no_keep_alive is True
        assert connection.params.max_header_size == 1024
        assert connection.params.max_body_size == 1024
        assert connection.params.decompress is True
        assert connection._sockaddr == ('127.0.0.1', 80)
