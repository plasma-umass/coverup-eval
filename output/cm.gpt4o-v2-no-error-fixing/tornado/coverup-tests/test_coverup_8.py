# file: tornado/simple_httpclient.py:514-527
# asked: {"lines": [514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527], "branches": [[515, 516], [515, 517], [517, 518], [517, 521], [519, 520], [519, 521], [522, 0], [522, 523], [526, 0], [526, 527]]}
# gained: {"lines": [514], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest
from tornado.iostream import IOStream, StreamClosedError
from tornado.simple_httpclient import SimpleAsyncHTTPClient
from tornado.tcpclient import TCPClient
from unittest.mock import MagicMock, patch

@pytest.mark.asyncio
async def test_write_body_with_body():
    request = HTTPRequest(url="http://example.com", method="POST", body=b"test body")
    connection = MagicMock()
    connection.write = MagicMock()
    connection.finish = MagicMock()
    connection.read_response = MagicMock()
    
    http_conn = _HTTPConnection(
        client=None,
        request=request,
        release_callback=lambda: None,
        final_callback=lambda response: None,
        max_buffer_size=1024,
        tcp_client=TCPClient(),
        max_header_size=1024,
        max_body_size=1024
    )
    http_conn.connection = connection
    
    await http_conn._write_body(start_read=True)
    
    connection.write.assert_called_once_with(b"test body")
    connection.finish.assert_called_once()
    connection.read_response.assert_called_once_with(http_conn)

@pytest.mark.asyncio
async def test_write_body_with_body_producer():
    async def body_producer(write):
        write(b"produced body")
    
    request = HTTPRequest(url="http://example.com", method="POST", body_producer=body_producer)
    connection = MagicMock()
    connection.write = MagicMock()
    connection.finish = MagicMock()
    connection.read_response = MagicMock()
    
    http_conn = _HTTPConnection(
        client=None,
        request=request,
        release_callback=lambda: None,
        final_callback=lambda response: None,
        max_buffer_size=1024,
        tcp_client=TCPClient(),
        max_header_size=1024,
        max_body_size=1024
    )
    http_conn.connection = connection
    
    await http_conn._write_body(start_read=True)
    
    connection.write.assert_called_once_with(b"produced body")
    connection.finish.assert_called_once()
    connection.read_response.assert_called_once_with(http_conn)

@pytest.mark.asyncio
async def test_write_body_stream_closed_error():
    request = HTTPRequest(url="http://example.com", method="POST", body=b"test body")
    connection = MagicMock()
    connection.write = MagicMock()
    connection.finish = MagicMock()
    connection.read_response = MagicMock(side_effect=StreamClosedError)
    
    http_conn = _HTTPConnection(
        client=None,
        request=request,
        release_callback=lambda: None,
        final_callback=lambda response: None,
        max_buffer_size=1024,
        tcp_client=TCPClient(),
        max_header_size=1024,
        max_body_size=1024
    )
    http_conn.connection = connection
    http_conn._handle_exception = MagicMock(return_value=False)
    
    with pytest.raises(StreamClosedError):
        await http_conn._write_body(start_read=True)
    
    connection.write.assert_called_once_with(b"test body")
    connection.finish.assert_called_once()
    connection.read_response.assert_called_once_with(http_conn)
    http_conn._handle_exception.assert_called_once()
