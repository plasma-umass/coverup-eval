# file: tornado/simple_httpclient.py:588-609
# asked: {"lines": [588, 593, 594, 595, 596, 597, 598, 599, 601, 602, 604, 606, 607, 608, 609], "branches": [[594, 595], [594, 597], [601, 602], [601, 604], [604, 0], [604, 606], [607, 608], [607, 609]]}
# gained: {"lines": [588], "branches": []}

import pytest
from tornado import httputil
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from unittest.mock import Mock, AsyncMock

@pytest.mark.asyncio
async def test_headers_received(monkeypatch):
    # Mocking the request and its attributes
    request = Mock()
    request.expect_100_continue = False
    request.header_callback = Mock()

    # Mocking the _should_follow_redirect method
    _HTTPConnection = SimpleAsyncHTTPClient._HTTPConnection
    connection = _HTTPConnection(request, None, None, None, None)
    monkeypatch.setattr(connection, "_should_follow_redirect", Mock(return_value=False))
    monkeypatch.setattr(connection, "_write_body", AsyncMock())

    # Creating a mock response start line and headers
    first_line = httputil.ResponseStartLine('HTTP/1.1', 200, 'OK')
    headers = httputil.HTTPHeaders({"Content-Type": "text/html"})

    # Call the method
    await connection.headers_received(first_line, headers)

    # Assertions
    assert connection.code == 200
    assert connection.reason == 'OK'
    assert connection.headers == headers
    request.header_callback.assert_called()
    request.header_callback.assert_any_call("HTTP/1.1 200 OK\r\n")
    request.header_callback.assert_any_call("Content-Type: text/html\r\n")
    request.header_callback.assert_any_call("\r\n")

@pytest.mark.asyncio
async def test_headers_received_100_continue(monkeypatch):
    # Mocking the request and its attributes
    request = Mock()
    request.expect_100_continue = True
    request.header_callback = Mock()

    # Mocking the _should_follow_redirect method
    _HTTPConnection = SimpleAsyncHTTPClient._HTTPConnection
    connection = _HTTPConnection(request, None, None, None, None)
    monkeypatch.setattr(connection, "_should_follow_redirect", Mock(return_value=False))
    monkeypatch.setattr(connection, "_write_body", AsyncMock())

    # Creating a mock response start line and headers
    first_line = httputil.ResponseStartLine('HTTP/1.1', 100, 'Continue')
    headers = httputil.HTTPHeaders({"Content-Type": "text/html"})

    # Call the method
    await connection.headers_received(first_line, headers)

    # Assertions
    connection._write_body.assert_awaited_once_with(False)
    assert not hasattr(connection, 'code')
    assert not hasattr(connection, 'reason')
    assert not hasattr(connection, 'headers')
    request.header_callback.assert_not_called()

@pytest.mark.asyncio
async def test_headers_received_follow_redirect(monkeypatch):
    # Mocking the request and its attributes
    request = Mock()
    request.expect_100_continue = False
    request.header_callback = Mock()

    # Mocking the _should_follow_redirect method
    _HTTPConnection = SimpleAsyncHTTPClient._HTTPConnection
    connection = _HTTPConnection(request, None, None, None, None)
    monkeypatch.setattr(connection, "_should_follow_redirect", Mock(return_value=True))
    monkeypatch.setattr(connection, "_write_body", AsyncMock())

    # Creating a mock response start line and headers
    first_line = httputil.ResponseStartLine('HTTP/1.1', 200, 'OK')
    headers = httputil.HTTPHeaders({"Content-Type": "text/html"})

    # Call the method
    await connection.headers_received(first_line, headers)

    # Assertions
    assert connection.code == 200
    assert connection.reason == 'OK'
    assert connection.headers == headers
    request.header_callback.assert_not_called()
