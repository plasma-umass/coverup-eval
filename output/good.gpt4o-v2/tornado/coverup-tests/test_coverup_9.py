# file: tornado/tcpclient.py:217-291
# asked: {"lines": [217, 221, 222, 223, 224, 225, 226, 253, 254, 255, 256, 257, 259, 260, 261, 262, 265, 266, 267, 268, 269, 270, 271, 272, 275, 279, 280, 281, 282, 283, 284, 288, 289, 291], "branches": [[253, 254], [253, 260], [254, 255], [254, 256], [256, 257], [256, 259], [260, 261], [260, 265], [279, 280], [279, 291], [280, 281], [280, 288]]}
# gained: {"lines": [217, 221, 222, 223, 224, 225, 226], "branches": []}

import pytest
import socket
import datetime
from unittest.mock import patch, AsyncMock, MagicMock
from tornado.iostream import IOStream
from tornado.tcpclient import TCPClient

@pytest.mark.asyncio
async def test_connect_no_timeout():
    client = TCPClient()
    host = 'localhost'
    port = 8888

    with patch.object(client.resolver, 'resolve', new=AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', port))])):
        with patch('tornado.tcpclient._Connector.start', new=AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', port), IOStream(socket.socket())))):
            stream = await client.connect(host, port)
            assert isinstance(stream, IOStream)

@pytest.mark.asyncio
async def test_connect_with_timeout():
    client = TCPClient()
    host = 'localhost'
    port = 8888
    timeout = 5.0

    with patch.object(client.resolver, 'resolve', new=AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', port))])):
        with patch('tornado.tcpclient._Connector.start', new=AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', port), IOStream(socket.socket())))):
            stream = await client.connect(host, port, timeout=timeout)
            assert isinstance(stream, IOStream)

@pytest.mark.asyncio
async def test_connect_with_ssl_options():
    client = TCPClient()
    host = 'localhost'
    port = 8888
    ssl_options = {'cert_reqs': ssl.CERT_NONE}

    with patch.object(client.resolver, 'resolve', new=AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', port))])):
        with patch('tornado.tcpclient._Connector.start', new=AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', port), IOStream(socket.socket())))):
            with patch.object(IOStream, 'start_tls', new=AsyncMock(return_value=IOStream(socket.socket()))):
                stream = await client.connect(host, port, ssl_options=ssl_options)
                assert isinstance(stream, IOStream)

@pytest.mark.asyncio
async def test_connect_with_invalid_timeout():
    client = TCPClient()
    host = 'localhost'
    port = 8888
    timeout = 'invalid'

    with pytest.raises(TypeError):
        await client.connect(host, port, timeout=timeout)

@pytest.mark.asyncio
async def test_connect_with_datetime_timeout():
    client = TCPClient()
    host = 'localhost'
    port = 8888
    timeout = datetime.timedelta(seconds=5)

    with patch.object(client.resolver, 'resolve', new=AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', port))])):
        with patch('tornado.tcpclient._Connector.start', new=AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', port), IOStream(socket.socket())))):
            stream = await client.connect(host, port, timeout=timeout)
            assert isinstance(stream, IOStream)
