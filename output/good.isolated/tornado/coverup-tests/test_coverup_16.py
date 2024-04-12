# file tornado/tcpclient.py:217-291
# lines [217, 221, 222, 223, 224, 225, 226, 253, 254, 255, 256, 257, 259, 260, 261, 262, 265, 266, 267, 268, 269, 270, 271, 272, 275, 279, 280, 281, 282, 283, 284, 288, 289, 291]
# branches ['253->254', '253->260', '254->255', '254->256', '256->257', '256->259', '260->261', '260->265', '279->280', '279->291', '280->281', '280->288']

import pytest
import socket
import ssl
from unittest.mock import Mock, patch
from tornado.tcpclient import TCPClient
from tornado.iostream import IOStream
from tornado.ioloop import IOLoop
from tornado import gen
import datetime
import numbers

@pytest.mark.asyncio
async def test_tcpclient_connect_timeout_type_error(mocker):
    # Mocking resolver and stream to avoid actual network operations
    mock_resolver = mocker.Mock()
    mock_resolver.resolve = mocker.AsyncMock()
    mock_stream = mocker.Mock(spec=IOStream)
    mock_connector = mocker.Mock()
    mock_connector.start = mocker.AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 80), mock_stream))

    # Patching _Connector to return our mock_connector
    with patch('tornado.tcpclient._Connector', return_value=mock_connector):
        tcp_client = TCPClient()
        tcp_client.resolver = mock_resolver

        # Test with an invalid timeout type
        with pytest.raises(TypeError):
            await tcp_client.connect(
                host='localhost',
                port=80,
                timeout='invalid_timeout_type'
            )

@pytest.mark.asyncio
async def test_tcpclient_connect_with_ssl_and_timeout(mocker):
    # Mocking resolver and stream to avoid actual network operations
    mock_resolver = mocker.Mock()
    mock_resolver.resolve = mocker.AsyncMock()
    mock_stream = mocker.Mock(spec=IOStream)
    mock_stream.start_tls = mocker.AsyncMock(return_value=mock_stream)
    mock_connector = mocker.Mock()
    mock_connector.start = mocker.AsyncMock(return_value=(socket.AF_INET, ('127.0.0.1', 80), mock_stream))

    # Patching _Connector to return our mock_connector
    with patch('tornado.tcpclient._Connector', return_value=mock_connector):
        tcp_client = TCPClient()
        tcp_client.resolver = mock_resolver

        # Mock IOLoop time to control the timeout
        mock_time = mocker.Mock(return_value=1000)
        mocker.patch.object(IOLoop, 'current', return_value=mocker.Mock(time=mock_time))

        # Test with SSL options and a numeric timeout
        ssl_options = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        result_stream = await tcp_client.connect(
            host='localhost',
            port=443,
            ssl_options=ssl_options,
            timeout=10
        )

        # Assertions to ensure the correct stream is returned and start_tls was called
        assert result_stream is mock_stream
        mock_stream.start_tls.assert_called_once_with(
            False, ssl_options=ssl_options, server_hostname='localhost'
        )
