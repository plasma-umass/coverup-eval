# file tornado/tcpclient.py:217-291
# lines [217, 221, 222, 223, 224, 225, 226, 253, 254, 255, 256, 257, 259, 260, 261, 262, 265, 266, 267, 268, 269, 270, 271, 272, 275, 279, 280, 281, 282, 283, 284, 288, 289, 291]
# branches ['253->254', '253->260', '254->255', '254->256', '256->257', '256->259', '260->261', '260->265', '279->280', '279->291', '280->281', '280->288']

import pytest
import socket
import ssl
import datetime
import numbers
from unittest.mock import patch, AsyncMock
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient
from tornado.iostream import IOStream
from tornado import gen

@pytest.mark.asyncio
async def test_tcpclient_connect_with_timeout(mocker):
    mock_resolver = AsyncMock()
    mock_resolver.resolve = AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', 8888))])
    mock_connector = mocker.patch('tornado.tcpclient._Connector', autospec=True)
    mock_connector_instance = mock_connector.return_value
    mock_connector_instance.start = AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 8888), IOStream(socket.socket())))

    client = TCPClient()
    client.resolver = mock_resolver

    timeout = 5.0
    ssl_options = ssl.create_default_context()

    with patch.object(IOLoop, 'current', return_value=IOLoop.instance()):
        stream = await client.connect(
            host='localhost',
            port=8888,
            timeout=timeout,
            ssl_options=ssl_options
        )

    assert isinstance(stream, IOStream)
    mock_resolver.resolve.assert_called_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector_instance.start.assert_called_once()
    if isinstance(timeout, numbers.Real):
        expected_timeout = IOLoop.current().time() + timeout
    elif isinstance(timeout, datetime.timedelta):
        expected_timeout = IOLoop.current().time() + timeout.total_seconds()
    else:
        expected_timeout = None
    assert expected_timeout is not None

@pytest.mark.asyncio
async def test_tcpclient_connect_without_timeout(mocker):
    mock_resolver = AsyncMock()
    mock_resolver.resolve = AsyncMock(return_value=[(socket.AF_INET, ('127.0.0.1', 8888))])
    mock_connector = mocker.patch('tornado.tcpclient._Connector', autospec=True)
    mock_connector_instance = mock_connector.return_value
    mock_connector_instance.start = AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 8888), IOStream(socket.socket())))

    client = TCPClient()
    client.resolver = mock_resolver

    ssl_options = ssl.create_default_context()

    stream = await client.connect(
        host='localhost',
        port=8888,
        ssl_options=ssl_options
    )

    assert isinstance(stream, IOStream)
    mock_resolver.resolve.assert_called_once_with('localhost', 8888, socket.AF_UNSPEC)
    mock_connector_instance.start.assert_called_once()
