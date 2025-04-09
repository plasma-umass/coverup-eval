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
from tornado.concurrent import Future
from typing import Any, Union, Dict, Optional

@pytest.mark.asyncio
async def test_tcpclient_connect():
    client = TCPClient()
    host = 'localhost'
    port = 8888
    af = socket.AF_INET
    ssl_options = None
    max_buffer_size = 104857600
    source_ip = '127.0.0.1'
    source_port = 12345
    timeout = 5.0

    # Mock resolver
    client.resolver = mock.Mock()
    client.resolver.resolve = mock.AsyncMock(return_value=[(af, (host, port))])

    # Mock _create_stream
    client._create_stream = mock.Mock(return_value=mock.Mock(spec=IOStream))

    # Mock _Connector
    with mock.patch('tornado.tcpclient._Connector', autospec=True) as MockConnector:
        mock_connector = MockConnector.return_value
        mock_connector.start = mock.AsyncMock(return_value=(af, (host, port), mock.Mock(spec=IOStream)))

        # Test with timeout
        stream = await client.connect(
            host, port, af, ssl_options, max_buffer_size, source_ip, source_port, timeout
        )
        assert isinstance(stream, IOStream)
        client.resolver.resolve.assert_awaited_once_with(host, port, af)
        mock_connector.start.assert_awaited_once_with(connect_timeout=timeout)

        # Test without timeout
        stream = await client.connect(
            host, port, af, ssl_options, max_buffer_size, source_ip, source_port, None
        )
        assert isinstance(stream, IOStream)
        client.resolver.resolve.assert_awaited_with(host, port, af)
        mock_connector.start.assert_awaited_with(connect_timeout=None)

        # Test with ssl_options and timeout
        ssl_options = {'cert_reqs': ssl.CERT_NONE}
        mock_stream = mock.Mock(spec=IOStream)
        mock_stream.start_tls = mock.AsyncMock(return_value=mock_stream)
        mock_connector.start = mock.AsyncMock(return_value=(af, (host, port), mock_stream))

        stream = await client.connect(
            host, port, af, ssl_options, max_buffer_size, source_ip, source_port, timeout
        )
        assert isinstance(stream, IOStream)
        mock_stream.start_tls.assert_awaited_once_with(
            False, ssl_options=ssl_options, server_hostname=host
        )

        # Test with ssl_options and without timeout
        stream = await client.connect(
            host, port, af, ssl_options, max_buffer_size, source_ip, source_port, None
        )
        assert isinstance(stream, IOStream)
        mock_stream.start_tls.assert_awaited_with(
            False, ssl_options=ssl_options, server_hostname=host
        )

        # Test with invalid timeout type
        with pytest.raises(TypeError):
            await client.connect(
                host, port, af, ssl_options, max_buffer_size, source_ip, source_port, "invalid"
            )
