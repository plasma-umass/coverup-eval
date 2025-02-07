# file: tornado/tcpclient.py:293-328
# asked: {"lines": [293, 298, 299, 303, 304, 305, 308, 312, 313, 315, 316, 317, 318, 320, 321, 322, 323, 324, 325, 326, 328], "branches": [[305, 308], [305, 312], [313, 315], [313, 321]]}
# gained: {"lines": [293, 298, 299], "branches": []}

import pytest
import socket
from tornado.tcpclient import TCPClient
from tornado.iostream import IOStream
from tornado.concurrent import Future
from unittest.mock import patch, MagicMock
import asyncio

@pytest.fixture
def tcp_client():
    return TCPClient()

@pytest.fixture
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.mark.asyncio
async def test_create_stream_no_source_ip_no_source_port(tcp_client, event_loop):
    with patch('socket.socket') as mock_socket:
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance
        mock_iostream = MagicMock(spec=IOStream)
        with patch('tornado.iostream.IOStream', return_value=mock_iostream):
            addr = ('localhost', 8888)
            stream, future = tcp_client._create_stream(1024, socket.AF_INET, addr)
            assert stream == mock_iostream
            assert future == mock_iostream.connect.return_value
            mock_socket_instance.bind.assert_not_called()

@pytest.mark.asyncio
async def test_create_stream_with_source_ip_and_port(tcp_client, event_loop):
    with patch('socket.socket') as mock_socket:
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance
        mock_iostream = MagicMock(spec=IOStream)
        with patch('tornado.iostream.IOStream', return_value=mock_iostream):
            addr = ('localhost', 8888)
            stream, future = tcp_client._create_stream(1024, socket.AF_INET, addr, source_ip='127.0.0.1', source_port=9999)
            assert stream == mock_iostream
            assert future == mock_iostream.connect.return_value
            mock_socket_instance.bind.assert_called_once_with(('127.0.0.1', 9999))

@pytest.mark.asyncio
async def test_create_stream_with_source_port_no_ip(tcp_client, event_loop):
    with patch('socket.socket') as mock_socket:
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance
        mock_iostream = MagicMock(spec=IOStream)
        with patch('tornado.iostream.IOStream', return_value=mock_iostream):
            addr = ('localhost', 8888)
            stream, future = tcp_client._create_stream(1024, socket.AF_INET, addr, source_port=9999)
            assert stream == mock_iostream
            assert future == mock_iostream.connect.return_value
            mock_socket_instance.bind.assert_called_once_with(('127.0.0.1', 9999))

@pytest.mark.asyncio
async def test_create_stream_bind_raises_error(tcp_client, event_loop):
    with patch('socket.socket') as mock_socket:
        mock_socket_instance = MagicMock()
        mock_socket_instance.bind.side_effect = socket.error
        mock_socket.return_value = mock_socket_instance
        addr = ('localhost', 8888)
        with pytest.raises(socket.error):
            tcp_client._create_stream(1024, socket.AF_INET, addr, source_ip='127.0.0.1', source_port=9999)
        mock_socket_instance.close.assert_called_once()

@pytest.mark.asyncio
async def test_create_stream_iostream_raises_error(tcp_client, event_loop):
    with patch('socket.socket') as mock_socket:
        mock_socket_instance = MagicMock()
        mock_socket.return_value = mock_socket_instance
        with patch('tornado.iostream.IOStream', side_effect=socket.error):
            addr = ('localhost', 8888)
            stream, future = tcp_client._create_stream(1024, socket.AF_INET, addr)
            assert isinstance(future, Future)
            assert future.done()
            assert isinstance(future.exception(), socket.error)
