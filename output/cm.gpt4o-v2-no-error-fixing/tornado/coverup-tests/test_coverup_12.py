# file: tornado/tcpclient.py:217-291
# asked: {"lines": [217, 221, 222, 223, 224, 225, 226, 253, 254, 255, 256, 257, 259, 260, 261, 262, 265, 266, 267, 268, 269, 270, 271, 272, 275, 279, 280, 281, 282, 283, 284, 288, 289, 291], "branches": [[253, 254], [253, 260], [254, 255], [254, 256], [256, 257], [256, 259], [260, 261], [260, 265], [279, 280], [279, 291], [280, 281], [280, 288]]}
# gained: {"lines": [217, 221, 222, 223, 224, 225, 226], "branches": []}

import pytest
import socket
import datetime
import ssl
from unittest import mock
from tornado.ioloop import IOLoop
from tornado.iostream import IOStream
from tornado.tcpclient import TCPClient
from tornado import gen
from tornado.util import TimeoutError

@pytest.mark.asyncio
async def test_tcpclient_connect_no_timeout_no_ssl(mocker):
    mock_resolver = mocker.Mock()
    mock_resolver.resolve = mocker.AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', 8888))])
    mock_connector = mocker.Mock()
    mock_connector.start = mocker.AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 8888), IOStream(mock.Mock())))
    mocker.patch('tornado.tcpclient._Connector', return_value=mock_connector)
    
    client = TCPClient()
    client.resolver = mock_resolver
    
    stream = await client.connect('localhost', 8888)
    
    assert isinstance(stream, IOStream)
    mock_resolver.resolve.assert_awaited_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.start.assert_awaited_once()

@pytest.mark.asyncio
async def test_tcpclient_connect_with_timeout_no_ssl(mocker):
    mock_resolver = mocker.Mock()
    mock_resolver.resolve = mocker.AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', 8888))])
    mock_connector = mocker.Mock()
    mock_connector.start = mocker.AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 8888), IOStream(mock.Mock())))
    mocker.patch('tornado.tcpclient._Connector', return_value=mock_connector)
    mocker.patch('tornado.gen.with_timeout', side_effect=gen.with_timeout)
    
    client = TCPClient()
    client.resolver = mock_resolver
    
    stream = await client.connect('localhost', 8888, timeout=2)
    
    assert isinstance(stream, IOStream)
    mock_resolver.resolve.assert_awaited_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.start.assert_awaited_once()
    gen.with_timeout.assert_awaited()

@pytest.mark.asyncio
async def test_tcpclient_connect_with_timeout_with_ssl(mocker):
    mock_resolver = mocker.Mock()
    mock_resolver.resolve = mocker.AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', 8888))])
    mock_connector = mocker.Mock()
    mock_connector.start = mocker.AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 8888), IOStream(mock.Mock())))
    mocker.patch('tornado.tcpclient._Connector', return_value=mock_connector)
    mocker.patch('tornado.gen.with_timeout', side_effect=gen.with_timeout)
    mock_start_tls = mocker.AsyncMock(return_value=IOStream(mock.Mock()))
    mocker.patch.object(IOStream, 'start_tls', mock_start_tls)
    
    client = TCPClient()
    client.resolver = mock_resolver
    
    ssl_options = ssl.create_default_context()
    stream = await client.connect('localhost', 8888, timeout=2, ssl_options=ssl_options)
    
    assert isinstance(stream, IOStream)
    mock_resolver.resolve.assert_awaited_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector.start.assert_awaited_once()
    gen.with_timeout.assert_awaited()
    mock_start_tls.assert_awaited_once_with(False, ssl_options=ssl_options, server_hostname='localhost')

@pytest.mark.asyncio
async def test_tcpclient_connect_invalid_timeout(mocker):
    client = TCPClient()
    
    with pytest.raises(TypeError):
        await client.connect('localhost', 8888, timeout='invalid')
