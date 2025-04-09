# file: tornado/simple_httpclient.py:687-694
# asked: {"lines": [688, 690, 691, 692, 694], "branches": [[688, 690], [688, 691], [691, 692], [691, 694]]}
# gained: {"lines": [688, 690, 691, 692, 694], "branches": [[688, 690], [688, 691], [691, 692], [691, 694]]}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.httputil import HTTPHeaders
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.simple_httpclient import _HTTPConnection

class Test_HTTPConnection:
    @pytest.fixture
    def setup_http_connection(self, monkeypatch):
        request = HTTPRequest(url="http://example.com")
        release_callback = lambda: None
        final_callback = lambda response: None
        max_buffer_size = 104857600
        tcp_client = TCPClient()
        max_header_size = 104857600
        max_body_size = 104857600

        connection = _HTTPConnection(
            client=None,
            request=request,
            release_callback=release_callback,
            final_callback=final_callback,
            max_buffer_size=max_buffer_size,
            tcp_client=tcp_client,
            max_header_size=max_header_size,
            max_body_size=max_body_size,
        )

        yield connection

    def test_data_received_with_redirect(self, setup_http_connection, mocker):
        connection = setup_http_connection
        mocker.patch.object(connection, '_should_follow_redirect', return_value=True)
        mocker.patch.object(connection.request, 'streaming_callback', None)
        connection.chunks = []

        connection.data_received(b'test_chunk')

        assert connection.chunks == []

    def test_data_received_with_streaming_callback(self, setup_http_connection, mocker):
        connection = setup_http_connection
        mocker.patch.object(connection, '_should_follow_redirect', return_value=False)
        mock_callback = mocker.Mock()
        connection.request.streaming_callback = mock_callback
        connection.chunks = []

        connection.data_received(b'test_chunk')

        mock_callback.assert_called_once_with(b'test_chunk')
        assert connection.chunks == []

    def test_data_received_without_streaming_callback(self, setup_http_connection, mocker):
        connection = setup_http_connection
        mocker.patch.object(connection, '_should_follow_redirect', return_value=False)
        mocker.patch.object(connection.request, 'streaming_callback', None)
        connection.chunks = []

        connection.data_received(b'test_chunk')

        assert connection.chunks == [b'test_chunk']
