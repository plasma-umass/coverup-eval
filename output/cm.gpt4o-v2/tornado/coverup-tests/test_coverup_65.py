# file: tornado/simple_httpclient.py:611-620
# asked: {"lines": [611, 612, 613, 614, 615, 616, 617, 618, 620], "branches": [[612, 613], [612, 620]]}
# gained: {"lines": [611, 612, 613, 614, 615, 616, 617, 618, 620], "branches": [[612, 613], [612, 620]]}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.httputil import HTTPHeaders
from tornado.simple_httpclient import SimpleAsyncHTTPClient, _HTTPConnection
from tornado.tcpclient import TCPClient
from tornado.ioloop import IOLoop
from unittest.mock import Mock

@pytest.fixture
def http_connection():
    request = HTTPRequest(url="http://example.com", follow_redirects=True, max_redirects=3)
    release_callback = Mock()
    final_callback = Mock()
    tcp_client = TCPClient()
    conn = _HTTPConnection(
        client=Mock(spec=SimpleAsyncHTTPClient),
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=104857600,
        tcp_client=tcp_client,
        max_header_size=104857600,
        max_body_size=104857600
    )
    return conn

def test_should_follow_redirect(http_connection):
    http_connection.code = 301
    http_connection.headers = HTTPHeaders({"Location": "http://example.com/redirect"})
    assert http_connection._should_follow_redirect() == True

    http_connection.code = 302
    assert http_connection._should_follow_redirect() == True

    http_connection.code = 303
    assert http_connection._should_follow_redirect() == True

    http_connection.code = 307
    assert http_connection._should_follow_redirect() == True

    http_connection.code = 308
    assert http_connection._should_follow_redirect() == True

    http_connection.code = 404
    assert http_connection._should_follow_redirect() == False

    http_connection.request.follow_redirects = False
    assert http_connection._should_follow_redirect() == False

    http_connection.request.follow_redirects = True
    http_connection.request.max_redirects = 0
    assert http_connection._should_follow_redirect() == False

    http_connection.headers = None
    assert http_connection._should_follow_redirect() == False

    http_connection.headers = HTTPHeaders()
    assert http_connection._should_follow_redirect() == False
