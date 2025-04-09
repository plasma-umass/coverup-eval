# file: tornado/simple_httpclient.py:514-527
# asked: {"lines": [514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527], "branches": [[515, 516], [515, 517], [517, 518], [517, 521], [519, 520], [519, 521], [522, 0], [522, 523], [526, 0], [526, 527]]}
# gained: {"lines": [514], "branches": []}

import pytest
from unittest.mock import AsyncMock, Mock, patch
from tornado.iostream import StreamClosedError
from tornado import httputil
from tornado.httpclient import HTTPRequest
from tornado.tcpclient import TCPClient
from tornado.ioloop import IOLoop
from tornado.simple_httpclient import _HTTPConnection

class TestHTTPConnection:
    @pytest.fixture
    def setup_http_connection(self):
        self.connection = Mock()
        self.request = Mock(spec=HTTPRequest)
        self.request.body = None
        self.request.body_producer = None
        self.http_connection = _HTTPConnection(
            client=None,
            request=self.request,
            release_callback=Mock(),
            final_callback=Mock(),
            max_buffer_size=1024,
            tcp_client=Mock(spec=TCPClient),
            max_header_size=1024,
            max_body_size=1024
        )
        self.http_connection.connection = self.connection

    @pytest.mark.asyncio
    async def test_write_body_with_body(self, setup_http_connection):
        self.request.body = b"test body"
        self.request.body_producer = None

        await self.http_connection._write_body(start_read=False)

        self.connection.write.assert_called_once_with(b"test body")
        self.connection.finish.assert_called_once()
        self.connection.read_response.assert_not_called()

    @pytest.mark.asyncio
    async def test_write_body_with_body_producer(self, setup_http_connection):
        self.request.body = None
        self.request.body_producer = AsyncMock()
        self.request.body_producer.return_value = None

        await self.http_connection._write_body(start_read=False)

        self.request.body_producer.assert_called_once_with(self.connection.write)
        self.connection.finish.assert_called_once()
        self.connection.read_response.assert_not_called()

    @pytest.mark.asyncio
    async def test_write_body_with_body_producer_future(self, setup_http_connection):
        self.request.body = None
        self.request.body_producer = AsyncMock()
        fut = AsyncMock()
        self.request.body_producer.return_value = fut

        await self.http_connection._write_body(start_read=False)

        self.request.body_producer.assert_called_once_with(self.connection.write)
        fut.assert_awaited_once()
        self.connection.finish.assert_called_once()
        self.connection.read_response.assert_not_called()

    @pytest.mark.asyncio
    async def test_write_body_start_read(self, setup_http_connection):
        self.request.body = None
        self.request.body_producer = None

        await self.http_connection._write_body(start_read=True)

        self.connection.finish.assert_called_once()
        self.connection.read_response.assert_awaited_once_with(self)

    @pytest.mark.asyncio
    async def test_write_body_stream_closed_error(self, setup_http_connection):
        self.request.body = None
        self.request.body_producer = None
        self.connection.read_response = AsyncMock(side_effect=StreamClosedError)
        self.http_connection._handle_exception = Mock(return_value=False)

        with pytest.raises(StreamClosedError):
            await self.http_connection._write_body(start_read=True)

        self.connection.finish.assert_called_once()
        self.connection.read_response.assert_awaited_once_with(self)
        self.http_connection._handle_exception.assert_called_once()
