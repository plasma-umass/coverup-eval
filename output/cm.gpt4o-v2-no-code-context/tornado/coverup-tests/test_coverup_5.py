# file: tornado/simple_httpclient.py:514-527
# asked: {"lines": [514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527], "branches": [[515, 516], [515, 517], [517, 518], [517, 521], [519, 520], [519, 521], [522, 0], [522, 523], [526, 0], [526, 527]]}
# gained: {"lines": [514], "branches": []}

import pytest
from unittest.mock import Mock, patch, AsyncMock
from tornado.simple_httpclient import SimpleAsyncHTTPClient, HTTPRequest, httputil, StreamClosedError

@pytest.mark.asyncio
async def test_write_body_with_body(monkeypatch):
    request = HTTPRequest(url="http://example.com", body=b"test body")
    connection = Mock()
    connection.write = Mock()
    connection.finish = Mock()
    connection.read_response = AsyncMock()

    http_connection = SimpleAsyncHTTPClient._HTTPConnection(request, connection)
    await http_connection._write_body(start_read=True)

    connection.write.assert_called_once_with(b"test body")
    connection.finish.assert_called_once()
    connection.read_response.assert_awaited_once_with(http_connection)

@pytest.mark.asyncio
async def test_write_body_with_body_producer(monkeypatch):
    async def body_producer(write):
        write(b"produced body")
        return

    request = HTTPRequest(url="http://example.com", body_producer=body_producer)
    connection = Mock()
    connection.write = Mock()
    connection.finish = Mock()
    connection.read_response = AsyncMock()

    http_connection = SimpleAsyncHTTPClient._HTTPConnection(request, connection)
    await http_connection._write_body(start_read=True)

    connection.write.assert_called_once_with(b"produced body")
    connection.finish.assert_called_once()
    connection.read_response.assert_awaited_once_with(http_connection)

@pytest.mark.asyncio
async def test_write_body_with_body_producer_future(monkeypatch):
    async def body_producer(write):
        write(b"produced body")
        return

    request = HTTPRequest(url="http://example.com", body_producer=body_producer)
    connection = Mock()
    connection.write = Mock()
    connection.finish = Mock()
    connection.read_response = AsyncMock()

    http_connection = SimpleAsyncHTTPClient._HTTPConnection(request, connection)
    await http_connection._write_body(start_read=True)

    connection.write.assert_called_once_with(b"produced body")
    connection.finish.assert_called_once()
    connection.read_response.assert_awaited_once_with(http_connection)

@pytest.mark.asyncio
async def test_write_body_with_stream_closed_error(monkeypatch):
    request = HTTPRequest(url="http://example.com", body=b"test body")
    connection = Mock()
    connection.write = Mock()
    connection.finish = Mock()
    connection.read_response = AsyncMock(side_effect=StreamClosedError)

    http_connection = SimpleAsyncHTTPClient._HTTPConnection(request, connection)
    http_connection._handle_exception = Mock(return_value=False)

    with pytest.raises(StreamClosedError):
        await http_connection._write_body(start_read=True)

    connection.write.assert_called_once_with(b"test body")
    connection.finish.assert_called_once()
    connection.read_response.assert_awaited_once_with(http_connection)
    http_connection._handle_exception.assert_called_once()
