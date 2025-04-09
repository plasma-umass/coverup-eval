# file: tornado/tcpclient.py:217-291
# asked: {"lines": [217, 221, 222, 223, 224, 225, 226, 253, 254, 255, 256, 257, 259, 260, 261, 262, 265, 266, 267, 268, 269, 270, 271, 272, 275, 279, 280, 281, 282, 283, 284, 288, 289, 291], "branches": [[253, 254], [253, 260], [254, 255], [254, 256], [256, 257], [256, 259], [260, 261], [260, 265], [279, 280], [279, 291], [280, 281], [280, 288]]}
# gained: {"lines": [217, 221, 222, 223, 224, 225, 226], "branches": []}

import pytest
import socket
import ssl
import datetime
import numbers
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from tornado.iostream import IOStream, SSLIOStream
from tornado import gen
from unittest.mock import patch, AsyncMock

@pytest.mark.asyncio
async def test_tcpclient_connect_no_timeout(mocker):
    mock_resolver = mocker.patch('tornado.tcpclient.Resolver')
    mock_resolver.return_value.resolve = AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', 8888))])
    mock_connector = mocker.patch('tornado.tcpclient._Connector')
    mock_connector.return_value.start = AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 8888), IOStream()))

    client = TCPClient()
    stream = await client.connect('localhost', 8888)

    assert isinstance(stream, IOStream)
    mock_resolver.return_value.resolve.assert_called_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.return_value.start.assert_called_once()

@pytest.mark.asyncio
async def test_tcpclient_connect_with_timeout(mocker):
    mock_resolver = mocker.patch('tornado.tcpclient.Resolver')
    mock_resolver.return_value.resolve = AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', 8888))])
    mock_connector = mocker.patch('tornado.tcpclient._Connector')
    mock_connector.return_value.start = AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 8888), IOStream()))

    client = TCPClient()
    timeout = 5
    stream = await client.connect('localhost', 8888, timeout=timeout)

    assert isinstance(stream, IOStream)
    mock_resolver.return_value.resolve.assert_called_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.return_value.start.assert_called_once()

@pytest.mark.asyncio
async def test_tcpclient_connect_with_ssl(mocker):
    mock_resolver = mocker.patch('tornado.tcpclient.Resolver')
    mock_resolver.return_value.resolve = AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', 8888))])
    mock_connector = mocker.patch('tornado.tcpclient._Connector')
    mock_connector.return_value.start = AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 8888), IOStream()))
    mock_start_tls = mocker.patch.object(IOStream, 'start_tls', AsyncMock(return_value=SSLIOStream()))

    client = TCPClient()
    ssl_options = ssl.create_default_context()
    stream = await client.connect('localhost', 8888, ssl_options=ssl_options)

    assert isinstance(stream, SSLIOStream)
    mock_resolver.return_value.resolve.assert_called_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.return_value.start.assert_called_once()
    mock_start_tls.assert_called_once_with(False, ssl_options=ssl_options, server_hostname='localhost')

@pytest.mark.asyncio
async def test_tcpclient_connect_with_invalid_timeout(mocker):
    client = TCPClient()
    with pytest.raises(TypeError):
        await client.connect('localhost', 8888, timeout='invalid')

@pytest.mark.asyncio
async def test_tcpclient_connect_with_timedelta_timeout(mocker):
    mock_resolver = mocker.patch('tornado.tcpclient.Resolver')
    mock_resolver.return_value.resolve = AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', 8888))])
    mock_connector = mocker.patch('tornado.tcpclient._Connector')
    mock_connector.return_value.start = AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 8888), IOStream()))

    client = TCPClient()
    timeout = datetime.timedelta(seconds=5)
    stream = await client.connect('localhost', 8888, timeout=timeout)

    assert isinstance(stream, IOStream)
    mock_resolver.return_value.resolve.assert_called_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.return_value.start.assert_called_once()
