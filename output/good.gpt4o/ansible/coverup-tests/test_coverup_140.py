# file lib/ansible/module_utils/connection.py:75-90
# lines [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
# branches ['78->79', '78->83', '80->81', '80->82', '85->86', '85->90', '87->88', '87->89']

import pytest
import socket
import struct
from unittest import mock
from ansible.module_utils.connection import recv_data

def to_bytes(data):
    return data.encode('utf-8')

@pytest.fixture
def mock_socket():
    return mock.Mock(spec=socket.socket)

def test_recv_data_complete_message(mock_socket):
    # Mock the socket to return a complete message in two parts
    header = struct.pack('!Q', 5)  # Length of the message is 5 bytes
    message = b'hello'
    mock_socket.recv.side_effect = [header, message]

    result = recv_data(mock_socket)
    assert result == message

def test_recv_data_incomplete_header(mock_socket):
    # Mock the socket to return an incomplete header
    mock_socket.recv.side_effect = [b'\x00\x00\x00\x00', b'']

    result = recv_data(mock_socket)
    assert result is None

def test_recv_data_incomplete_message(mock_socket):
    # Mock the socket to return an incomplete message
    header = struct.pack('!Q', 5)  # Length of the message is 5 bytes
    mock_socket.recv.side_effect = [header, b'hel', b'']

    result = recv_data(mock_socket)
    assert result is None

def test_recv_data_empty_socket(mock_socket):
    # Mock the socket to return nothing
    mock_socket.recv.return_value = b''

    result = recv_data(mock_socket)
    assert result is None
