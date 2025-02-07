# file: tornado/simple_httpclient.py:588-609
# asked: {"lines": [588, 593, 594, 595, 596, 597, 598, 599, 601, 602, 604, 606, 607, 608, 609], "branches": [[594, 595], [594, 597], [601, 602], [601, 604], [604, 0], [604, 606], [607, 608], [607, 609]]}
# gained: {"lines": [588], "branches": []}

import pytest
from tornado import httputil
from tornado.simple_httpclient import _HTTPConnection
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from unittest.mock import Mock

@pytest.mark.gen_test
async def test_headers_received():
    request = Mock(spec=HTTPRequest)
    request.expect_100_continue = False
    request.header_callback = Mock()

    release_callback = Mock()
    final_callback = Mock()
    tcp_client = Mock(spec=TCPClient)

    connection = _HTTPConnection(
        client=None,
        request=request,
        release_callback=release_callback,
        final_callback=final_callback,
        max_buffer_size=104857600,
        tcp_client=tcp_client,
        max_header_size=104857600,
        max_body_size=104857600
    )

    first_line = httputil.ResponseStartLine(version="HTTP/1.1", code=200, reason="OK")
    headers = httputil.HTTPHeaders({"Content-Type": "text/html"})

    await connection.headers_received(first_line, headers)

    assert connection.code == 200
    assert connection.reason == "OK"
    assert connection.headers == headers

    if connection._should_follow_redirect():
        assert not request.header_callback.called
    else:
        request.header_callback.assert_any_call("HTTP/1.1 200 OK\r\n")
        request.header_callback.assert_any_call("Content-Type: text/html\r\n")
        request.header_callback.assert_any_call("\r\n")

    # Clean up
    request.header_callback.reset_mock()
    release_callback.reset_mock()
    final_callback.reset_mock()
