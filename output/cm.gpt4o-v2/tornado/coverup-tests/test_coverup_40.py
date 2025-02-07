# file: tornado/simple_httpclient.py:260-291
# asked: {"lines": [260, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 287, 288, 289, 290], "branches": []}
# gained: {"lines": [260], "branches": []}

import pytest
from tornado.httpclient import HTTPRequest, HTTPResponse
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from tornado import httputil, gen
from unittest.mock import Mock, patch, AsyncMock
import time

from tornado.simple_httpclient import _HTTPConnection

@pytest.fixture
def mock_ioloop(mocker):
    mock_loop = mocker.patch('tornado.ioloop.IOLoop.current')
    mock_loop.return_value.time.return_value = time.time()
    return mock_loop

@pytest.fixture
def mock_tcpclient(mocker):
    return mocker.Mock(spec=TCPClient)

@pytest.fixture
def mock_http_request():
    return HTTPRequest(url="http://example.com")

@pytest.fixture
def mock_release_callback():
    return Mock()

@pytest.fixture
def mock_final_callback():
    return Mock()

@pytest.fixture
def mock_gen_convert_yielded(mocker):
    return mocker.patch('tornado.gen.convert_yielded', new_callable=AsyncMock)

@pytest.fixture
def mock_run(mocker):
    return mocker.patch('tornado.simple_httpclient._HTTPConnection.run', new_callable=AsyncMock)

@pytest.mark.asyncio
async def test_http_connection_init(mock_ioloop, mock_tcpclient, mock_http_request, mock_release_callback, mock_final_callback, mock_gen_convert_yielded, mock_run):
    connection = _HTTPConnection(
        client=None,
        request=mock_http_request,
        release_callback=mock_release_callback,
        final_callback=mock_final_callback,
        max_buffer_size=1024,
        tcp_client=mock_tcpclient,
        max_header_size=2048,
        max_body_size=4096
    )

    assert connection.io_loop == mock_ioloop.return_value
    assert connection.start_time == mock_ioloop.return_value.time.return_value
    assert connection.start_wall_time <= time.time()
    assert connection.client is None
    assert connection.request == mock_http_request
    assert connection.release_callback == mock_release_callback
    assert connection.final_callback == mock_final_callback
    assert connection.max_buffer_size == 1024
    assert connection.tcp_client == mock_tcpclient
    assert connection.max_header_size == 2048
    assert connection.max_body_size == 4096
    assert connection.code is None
    assert connection.headers is None
    assert connection.chunks == []
    assert connection._decompressor is None
    assert connection._timeout is None
    assert connection._sockaddr is None
    await mock_gen_convert_yielded.assert_called_once_with(mock_run.return_value)
    mock_ioloop.return_value.add_future.assert_called_once()
