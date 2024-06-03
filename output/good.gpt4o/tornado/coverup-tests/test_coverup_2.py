# file tornado/simple_httpclient.py:588-609
# lines [588, 593, 594, 595, 596, 597, 598, 599, 601, 602, 604, 606, 607, 608, 609]
# branches ['594->595', '594->597', '601->602', '601->604', '604->exit', '604->606', '607->608', '607->609']

import pytest
from tornado import httputil
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.httpclient import HTTPRequest, HTTPResponse
from unittest.mock import Mock

@pytest.mark.asyncio
async def test_headers_received(mocker):
    # Mock the request and its properties
    request = Mock()
    request.expect_100_continue = False
    request.header_callback = Mock()

    # Create an instance of the _HTTPConnection class
    client = SimpleAsyncHTTPClient()
    connection = client._HTTPConnection(request)

    # Mock the first_line and headers
    first_line = httputil.ResponseStartLine('HTTP/1.1', 200, 'OK')
    headers = httputil.HTTPHeaders({"Content-Type": "text/html"})

    # Call headers_received
    await connection.headers_received(first_line, headers)

    # Assertions to verify the postconditions
    assert connection.code == 200
    assert connection.reason == 'OK'
    assert connection.headers == headers

    # Verify that header_callback was called with the correct arguments
    request.header_callback.assert_any_call("HTTP/1.1 200 OK\r\n")
    request.header_callback.assert_any_call("Content-Type: text/html\r\n")
    request.header_callback.assert_any_call("\r\n")

    # Clean up
    await client.close()
