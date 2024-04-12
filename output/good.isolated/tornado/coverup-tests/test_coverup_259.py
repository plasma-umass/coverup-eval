# file tornado/tcpclient.py:293-328
# lines [323, 324, 325, 326]
# branches []

import pytest
import socket
from tornado.tcpclient import TCPClient
from tornado.iostream import IOStream
from tornado.concurrent import Future
from unittest.mock import patch

@pytest.fixture
def mock_socket_error():
    with patch('socket.socket') as mock_socket:
        mock_socket.return_value.connect.side_effect = socket.error("Mocked socket error")
        yield mock_socket

def test_create_stream_socket_error(mock_socket_error):
    tcp_client = TCPClient()
    with pytest.raises(socket.error):
        stream, future = tcp_client._create_stream(
            max_buffer_size=1024,
            af=socket.AF_INET,
            addr=('127.0.0.1', 80),
            source_ip='127.0.0.1',
            source_port=12345
        )
        assert isinstance(stream, IOStream)
        assert isinstance(future, Future)
        assert future.done() and not future.result(), "Future should be set with an exception"
