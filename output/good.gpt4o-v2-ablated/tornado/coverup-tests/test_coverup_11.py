# file: tornado/tcpclient.py:217-291
# asked: {"lines": [217, 221, 222, 223, 224, 225, 226, 253, 254, 255, 256, 257, 259, 260, 261, 262, 265, 266, 267, 268, 269, 270, 271, 272, 275, 279, 280, 281, 282, 283, 284, 288, 289, 291], "branches": [[253, 254], [253, 260], [254, 255], [254, 256], [256, 257], [256, 259], [260, 261], [260, 265], [279, 280], [279, 291], [280, 281], [280, 288]]}
# gained: {"lines": [217, 221, 222, 223, 224, 225, 226], "branches": []}

import pytest
import socket
import ssl
import datetime
import numbers
from unittest.mock import AsyncMock, patch, MagicMock
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from tornado.iostream import IOStream
from tornado import gen

@pytest.mark.asyncio
async def test_connect_no_timeout_no_ssl(mocker):
    mock_resolver = AsyncMock()
    mock_resolver.resolve.return_value = [(socket.AF_INET, ('127.0.0.1', 8888))]
    mock_connector = AsyncMock()
    mock_connector.start.return_value = (socket.AF_INET, ('127.0.0.1', 8888), IOStream())
    mocker.patch('tornado.tcpclient.TCPClient.resolver', new_callable=MagicMock, return_value=mock_resolver)
    mocker.patch('tornado.tcpclient._Connector', return_value=mock_connector)

    client = TCPClient()
    stream = await client.connect('localhost', 8888)
    
    assert isinstance(stream, IOStream)
    mock_resolver.resolve.assert_called_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.start.assert_called_once()

@pytest.mark.asyncio
async def test_connect_with_timeout_as_float(mocker):
    mock_resolver = AsyncMock()
    mock_resolver.resolve.return_value = [(socket.AF_INET, ('127.0.0.1', 8888))]
    mock_connector = AsyncMock()
    mock_connector.start.return_value = (socket.AF_INET, ('127.0.0.1', 8888), IOStream())
    mocker.patch('tornado.tcpclient.TCPClient.resolver', new_callable=MagicMock, return_value=mock_resolver)
    mocker.patch('tornado.tcpclient._Connector', return_value=mock_connector)
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=MagicMock(time=MagicMock(return_value=1000)))

    client = TCPClient()
    stream = await client.connect('localhost', 8888, timeout=10.0)
    
    assert isinstance(stream, IOStream)
    mock_resolver.resolve.assert_called_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.start.assert_called_once()

@pytest.mark.asyncio
async def test_connect_with_timeout_as_timedelta(mocker):
    mock_resolver = AsyncMock()
    mock_resolver.resolve.return_value = [(socket.AF_INET, ('127.0.0.1', 8888))]
    mock_connector = AsyncMock()
    mock_connector.start.return_value = (socket.AF_INET, ('127.0.0.1', 8888), IOStream())
    mocker.patch('tornado.tcpclient.TCPClient.resolver', new_callable=MagicMock, return_value=mock_resolver)
    mocker.patch('tornado.tcpclient._Connector', return_value=mock_connector)
    mocker.patch('tornado.ioloop.IOLoop.current', return_value=MagicMock(time=MagicMock(return_value=1000)))

    client = TCPClient()
    stream = await client.connect('localhost', 8888, timeout=datetime.timedelta(seconds=10))
    
    assert isinstance(stream, IOStream)
    mock_resolver.resolve.assert_called_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.start.assert_called_once()

@pytest.mark.asyncio
async def test_connect_with_ssl(mocker):
    mock_resolver = AsyncMock()
    mock_resolver.resolve.return_value = [(socket.AF_INET, ('127.0.0.1', 8888))]
    mock_connector = AsyncMock()
    mock_connector.start.return_value = (socket.AF_INET, ('127.0.0.1', 8888), IOStream())
    mock_stream = AsyncMock()
    mock_stream.start_tls.return_value = IOStream()
    mocker.patch('tornado.tcpclient.TCPClient.resolver', new_callable=MagicMock, return_value=mock_resolver)
    mocker.patch('tornado.tcpclient._Connector', return_value=mock_connector)
    mocker.patch('tornado.iostream.IOStream', return_value=mock_stream)

    client = TCPClient()
    stream = await client.connect('localhost', 8888, ssl_options={})
    
    assert isinstance(stream, IOStream)
    mock_resolver.resolve.assert_called_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.start.assert_called_once()
    mock_stream.start_tls.assert_called_once_with(False, ssl_options={}, server_hostname='localhost')

@pytest.mark.asyncio
async def test_connect_with_invalid_timeout_type(mocker):
    client = TCPClient()
    with pytest.raises(TypeError):
        await client.connect('localhost', 8888, timeout="invalid")
