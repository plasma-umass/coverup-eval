# file tornado/tcpclient.py:293-328
# lines [308, 323, 324, 325, 326]
# branches ['305->308']

import pytest
import socket
from tornado.tcpclient import TCPClient
from tornado.iostream import IOStream
from tornado.concurrent import Future
from unittest.mock import patch

@pytest.fixture
def mock_socket(mocker):
    mock = mocker.patch('socket.socket')
    mock.return_value.bind.side_effect = socket.error
    return mock

def test_create_stream_bind_exception_ipv4(mock_socket):
    tcp_client = TCPClient()
    with pytest.raises(socket.error):
        tcp_client._create_stream(
            max_buffer_size=1024,
            af=socket.AF_INET,
            addr=('127.0.0.1', 80),
            source_port=12345
        )
    mock_socket.assert_called_once_with(socket.AF_INET)

def test_create_stream_bind_exception_ipv6(mock_socket):
    tcp_client = TCPClient()
    with pytest.raises(socket.error):
        tcp_client._create_stream(
            max_buffer_size=1024,
            af=socket.AF_INET6,
            addr=('::1', 80),
            source_port=12345
        )
    mock_socket.assert_called_once_with(socket.AF_INET6)

def test_create_stream_bind_exception_no_source_ip(mock_socket):
    tcp_client = TCPClient()
    with pytest.raises(socket.error):
        tcp_client._create_stream(
            max_buffer_size=1024,
            af=socket.AF_INET,
            addr=('127.0.0.1', 80),
            source_port=12345
        )
    mock_socket.assert_called_once_with(socket.AF_INET)

def test_create_stream_bind_exception_no_source_ip_ipv6(mock_socket):
    tcp_client = TCPClient()
    with pytest.raises(socket.error):
        tcp_client._create_stream(
            max_buffer_size=1024,
            af=socket.AF_INET6,
            addr=('::1', 80),
            source_port=12345
        )
    mock_socket.assert_called_once_with(socket.AF_INET6)
