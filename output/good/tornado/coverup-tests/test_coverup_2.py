# file tornado/tcpclient.py:293-328
# lines [293, 298, 299, 303, 304, 305, 308, 312, 313, 315, 316, 317, 318, 320, 321, 322, 323, 324, 325, 326, 328]
# branches ['305->308', '305->312', '313->315', '313->321']

import pytest
import socket
from unittest.mock import patch
from tornado.tcpclient import TCPClient
from tornado.iostream import IOStream
from tornado.concurrent import Future

@pytest.fixture
def mock_socket(mocker):
    mock = mocker.patch('socket.socket')
    mock.return_value.bind.side_effect = socket.error
    return mock

def test_create_stream_bind_exception(mock_socket):
    tcp_client = TCPClient()
    with pytest.raises(socket.error):
        stream, future = tcp_client._create_stream(
            max_buffer_size=1024,
            af=socket.AF_INET,
            addr=('127.0.0.1', 80),
            source_ip='127.0.0.1',
            source_port=12345
        )
    mock_socket.assert_called_once()
    mock_socket.return_value.bind.assert_called_once_with(('127.0.0.1', 12345))
    mock_socket.return_value.close.assert_called_once()
