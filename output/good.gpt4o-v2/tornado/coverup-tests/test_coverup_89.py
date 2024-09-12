# file: tornado/simple_httpclient.py:529-533
# asked: {"lines": [529, 530, 531, 532, 533], "branches": [[530, 0], [530, 531]]}
# gained: {"lines": [529, 530, 531, 532, 533], "branches": [[530, 0], [530, 531]]}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.tcpclient import TCPClient
from tornado.ioloop import IOLoop
from unittest.mock import Mock
from tornado.simple_httpclient import _HTTPConnection

@pytest.fixture
def http_connection():
    release_callback = Mock()
    final_callback = Mock()
    request = HTTPRequest(url="http://example.com")
    tcp_client = TCPClient()
    conn = _HTTPConnection(
        client=None,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=104857600,
        tcp_client=tcp_client,
        max_header_size=104857600,
        max_body_size=104857600
    )
    return conn, release_callback

def test_release_callback_called(http_connection):
    conn, release_callback = http_connection
    conn._release()
    release_callback.assert_called_once()

def test_release_callback_not_called(http_connection):
    conn, release_callback = http_connection
    conn.release_callback = None
    conn._release()
    release_callback.assert_not_called()
