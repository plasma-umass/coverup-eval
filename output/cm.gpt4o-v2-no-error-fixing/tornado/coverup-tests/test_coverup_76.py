# file: tornado/simple_httpclient.py:529-533
# asked: {"lines": [529, 530, 531, 532, 533], "branches": [[530, 0], [530, 531]]}
# gained: {"lines": [529, 530, 531, 532, 533], "branches": [[530, 0], [530, 531]]}

import pytest
from unittest.mock import Mock
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from tornado.simple_httpclient import _HTTPConnection

@pytest.fixture
def setup_http_connection():
    request = HTTPRequest(url="http://example.com")
    release_callback = Mock()
    final_callback = Mock()
    tcp_client = Mock(spec=TCPClient)
    max_buffer_size = 1024
    max_header_size = 1024
    max_body_size = 1024

    connection = _HTTPConnection(
        client=None,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=max_buffer_size,
        tcp_client=tcp_client,
        max_header_size=max_header_size,
        max_body_size=max_body_size
    )
    return connection, release_callback

def test_release_callback_called(setup_http_connection):
    connection, release_callback = setup_http_connection
    connection._release()
    release_callback.assert_called_once()

def test_release_callback_not_called(setup_http_connection):
    connection, release_callback = setup_http_connection
    connection.release_callback = None
    connection._release()
    release_callback.assert_not_called()
