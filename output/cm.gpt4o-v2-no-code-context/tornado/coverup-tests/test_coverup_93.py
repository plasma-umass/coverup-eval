# file: tornado/simple_httpclient.py:529-533
# asked: {"lines": [529, 530, 531, 532, 533], "branches": [[530, 0], [530, 531]]}
# gained: {"lines": [529, 530, 531, 532, 533], "branches": [[530, 0], [530, 531]]}

import pytest
from tornado.simple_httpclient import SimpleAsyncHTTPClient, _HTTPConnection
from tornado.httputil import HTTPHeaders, HTTPMessageDelegate
from unittest.mock import Mock

class MockHTTPMessageDelegate(HTTPMessageDelegate):
    def headers_received(self, start_line, headers):
        pass

    def data_received(self, chunk):
        pass

    def finish(self):
        pass

@pytest.fixture
def mock_http_connection():
    delegate = MockHTTPMessageDelegate()
    request = Mock()
    release_callback = Mock()
    final_callback = Mock()
    max_buffer_size = 1024
    tcp_client = Mock()
    max_header_size = 1024
    max_body_size = 1024
    connection = _HTTPConnection(
        delegate, request, release_callback, final_callback,
        max_buffer_size, tcp_client, max_header_size, max_body_size
    )
    return connection

def test_release_callback_called(mock_http_connection):
    release_callback = Mock()
    mock_http_connection.release_callback = release_callback

    mock_http_connection._release()

    release_callback.assert_called_once()
    assert mock_http_connection.release_callback is None

def test_release_callback_not_called(mock_http_connection):
    mock_http_connection.release_callback = None

    mock_http_connection._release()

    assert mock_http_connection.release_callback is None
