# file tornado/simple_httpclient.py:588-609
# lines [588, 593, 594, 595, 596, 597, 598, 599, 601, 602, 604, 606, 607, 608, 609]
# branches ['594->595', '594->597', '601->602', '601->604', '604->exit', '604->606', '607->608', '607->609']

import pytest
from tornado import httputil, simple_httpclient
from unittest.mock import Mock

@pytest.mark.asyncio
async def test_headers_received_with_100_continue(mocker):
    # Mocking the necessary parts of the _HTTPConnection
    connection = simple_httpclient._HTTPConnection(Mock(), Mock(), Mock(), Mock(), Mock())
    connection._write_body = mocker.AsyncMock()
    connection._should_follow_redirect = mocker.Mock(return_value=False)
    connection.request = Mock()
    connection.request.expect_100_continue = True
    connection.request.header_callback = None

    # Creating a ResponseStartLine with a 100 Continue status code
    response_start_line = httputil.ResponseStartLine('HTTP/1.1', 100, 'Continue')

    # Creating dummy headers
    headers = httputil.HTTPHeaders()

    # Call the headers_received method
    await connection.headers_received(response_start_line, headers)

    # Assert that _write_body was called
    connection._write_body.assert_called_once_with(False)

@pytest.mark.asyncio
async def test_headers_received_with_header_callback(mocker):
    # Mocking the necessary parts of the _HTTPConnection
    connection = simple_httpclient._HTTPConnection(Mock(), Mock(), Mock(), Mock(), Mock())
    connection._write_body = mocker.AsyncMock()
    connection._should_follow_redirect = mocker.Mock(return_value=False)
    connection.request = Mock()
    connection.request.expect_100_continue = False
    connection.request.header_callback = mocker.Mock()

    # Creating a ResponseStartLine with a non-100 status code
    response_start_line = httputil.ResponseStartLine('HTTP/1.1', 200, 'OK')

    # Creating dummy headers
    headers = httputil.HTTPHeaders()
    headers.add('Content-Type', 'text/html')

    # Call the headers_received method
    await connection.headers_received(response_start_line, headers)

    # Assert that the header_callback was called with the correct start line and headers
    expected_start_line = "HTTP/1.1 200 OK\r\n"
    expected_header = "Content-Type: text/html\r\n"
    connection.request.header_callback.assert_has_calls([
        mocker.call(expected_start_line),
        mocker.call(expected_header),
        mocker.call("\r\n")
    ])
