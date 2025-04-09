# file: tornado/simple_httpclient.py:588-609
# asked: {"lines": [588, 593, 594, 595, 596, 597, 598, 599, 601, 602, 604, 606, 607, 608, 609], "branches": [[594, 595], [594, 597], [601, 602], [601, 604], [604, 0], [604, 606], [607, 608], [607, 609]]}
# gained: {"lines": [588], "branches": []}

import pytest
from tornado.httputil import HTTPHeaders, ResponseStartLine
from tornado.simple_httpclient import _HTTPConnection

class MockRequest:
    def __init__(self, expect_100_continue=False, header_callback=None):
        self.expect_100_continue = expect_100_continue
        self.header_callback = header_callback

@pytest.mark.asyncio
async def test_headers_received_100_continue(monkeypatch):
    async def mock_write_body(expect_continue):
        assert not expect_continue

    conn = _HTTPConnection()
    conn.request = MockRequest(expect_100_continue=True)
    conn._write_body = mock_write_body

    first_line = ResponseStartLine("HTTP/1.1", 100, "Continue")
    headers = HTTPHeaders()

    await conn.headers_received(first_line, headers)

@pytest.mark.asyncio
async def test_headers_received_follow_redirect(monkeypatch):
    def mock_should_follow_redirect():
        return True

    conn = _HTTPConnection()
    conn.request = MockRequest()
    conn._should_follow_redirect = mock_should_follow_redirect

    first_line = ResponseStartLine("HTTP/1.1", 200, "OK")
    headers = HTTPHeaders()

    await conn.headers_received(first_line, headers)

@pytest.mark.asyncio
async def test_headers_received_header_callback(monkeypatch):
    callback_results = []

    def mock_header_callback(data):
        callback_results.append(data)

    conn = _HTTPConnection()
    conn.request = MockRequest(header_callback=mock_header_callback)

    first_line = ResponseStartLine("HTTP/1.1", 200, "OK")
    headers = HTTPHeaders()
    headers.add("Content-Type", "text/html")
    headers.add("Set-Cookie", "A=B")

    await conn.headers_received(first_line, headers)

    assert callback_results == [
        "HTTP/1.1 200 OK\r\n",
        "Content-Type: text/html\r\n",
        "Set-Cookie: A=B\r\n",
        "\r\n"
    ]
