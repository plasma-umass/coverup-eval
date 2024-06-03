# file tornado/simple_httpclient.py:514-527
# lines [514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527]
# branches ['515->516', '515->517', '517->518', '517->521', '519->520', '519->521', '522->exit', '522->523', '526->exit', '526->527']

import pytest
from unittest import mock
from tornado import httputil
from tornado.simple_httpclient import SimpleAsyncHTTPClient, HTTPRequest
from tornado.iostream import StreamClosedError
import sys

@pytest.mark.asyncio
async def test_write_body_with_body(mocker):
    mock_connection = mock.Mock()
    mock_request = mock.Mock()
    mock_request.body = b"test body"
    mock_request.body_producer = None

    class _HTTPConnection(httputil.HTTPMessageDelegate):
        def __init__(self, request, connection):
            self.request = request
            self.connection = connection

        async def _write_body(self, start_read: bool) -> None:
            if self.request.body is not None:
                self.connection.write(self.request.body)
            elif self.request.body_producer is not None:
                fut = self.request.body_producer(self.connection.write)
                if fut is not None:
                    await fut
            self.connection.finish()
            if start_read:
                try:
                    await self.connection.read_response(self)
                except StreamClosedError:
                    if not self._handle_exception(*sys.exc_info()):
                        raise

    conn = _HTTPConnection(mock_request, mock_connection)
    await conn._write_body(start_read=False)

    mock_connection.write.assert_called_once_with(b"test body")
    mock_connection.finish.assert_called_once()
    mock_connection.read_response.assert_not_called()

@pytest.mark.asyncio
async def test_write_body_with_body_producer(mocker):
    mock_connection = mock.Mock()
    mock_request = mock.Mock()
    mock_request.body = None

    async def body_producer(write):
        write(b"produced body")

    mock_request.body_producer = body_producer

    class _HTTPConnection(httputil.HTTPMessageDelegate):
        def __init__(self, request, connection):
            self.request = request
            self.connection = connection

        async def _write_body(self, start_read: bool) -> None:
            if self.request.body is not None:
                self.connection.write(self.request.body)
            elif self.request.body_producer is not None:
                fut = self.request.body_producer(self.connection.write)
                if fut is not None:
                    await fut
            self.connection.finish()
            if start_read:
                try:
                    await self.connection.read_response(self)
                except StreamClosedError:
                    if not self._handle_exception(*sys.exc_info()):
                        raise

    conn = _HTTPConnection(mock_request, mock_connection)
    await conn._write_body(start_read=False)

    mock_connection.write.assert_called_once_with(b"produced body")
    mock_connection.finish.assert_called_once()
    mock_connection.read_response.assert_not_called()

@pytest.mark.asyncio
async def test_write_body_with_start_read(mocker):
    mock_connection = mock.Mock()
    mock_request = mock.Mock()
    mock_request.body = b"test body"
    mock_request.body_producer = None

    class _HTTPConnection(httputil.HTTPMessageDelegate):
        def __init__(self, request, connection):
            self.request = request
            self.connection = connection

        async def _write_body(self, start_read: bool) -> None:
            if self.request.body is not None:
                self.connection.write(self.request.body)
            elif self.request.body_producer is not None:
                fut = self.request.body_producer(self.connection.write)
                if fut is not None:
                    await fut
            self.connection.finish()
            if start_read:
                try:
                    await self.connection.read_response(self)
                except StreamClosedError:
                    if not self._handle_exception(*sys.exc_info()):
                        raise

    conn = _HTTPConnection(mock_request, mock_connection)
    await conn._write_body(start_read=True)

    mock_connection.write.assert_called_once_with(b"test body")
    mock_connection.finish.assert_called_once()
    mock_connection.read_response.assert_called_once_with(conn)

@pytest.mark.asyncio
async def test_write_body_with_stream_closed_error(mocker):
    mock_connection = mock.Mock()
    mock_request = mock.Mock()
    mock_request.body = b"test body"
    mock_request.body_producer = None

    class _HTTPConnection(httputil.HTTPMessageDelegate):
        def __init__(self, request, connection):
            self.request = request
            self.connection = connection

        async def _write_body(self, start_read: bool) -> None:
            if self.request.body is not None:
                self.connection.write(self.request.body)
            elif self.request.body_producer is not None:
                fut = self.request.body_producer(self.connection.write)
                if fut is not None:
                    await fut
            self.connection.finish()
            if start_read:
                try:
                    await self.connection.read_response(self)
                except StreamClosedError:
                    if not self._handle_exception(*sys.exc_info()):
                        raise

        def _handle_exception(self, typ, value, tb):
            return False

    mock_connection.read_response.side_effect = StreamClosedError

    conn = _HTTPConnection(mock_request, mock_connection)
    with pytest.raises(StreamClosedError):
        await conn._write_body(start_read=True)

    mock_connection.write.assert_called_once_with(b"test body")
    mock_connection.finish.assert_called_once()
    mock_connection.read_response.assert_called_once_with(conn)
