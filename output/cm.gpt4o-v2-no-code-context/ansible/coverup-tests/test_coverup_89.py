# file: lib/ansible/module_utils/connection.py:75-90
# asked: {"lines": [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[78, 79], [78, 83], [80, 81], [80, 82], [85, 86], [85, 90], [87, 88], [87, 89]]}
# gained: {"lines": [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[78, 79], [78, 83], [80, 81], [80, 82], [85, 86], [85, 90], [87, 88], [87, 89]]}

import pytest
import socket
import struct
from ansible.module_utils.connection import recv_data

def to_bytes(data):
    return data.encode('utf-8')

@pytest.fixture
def mock_socket(mocker):
    mock_socket = mocker.Mock(spec=socket.socket)
    return mock_socket

def test_recv_data_complete_message(mock_socket, mocker):
    # Mock the recv method to return a complete message
    header = struct.pack('!Q', 4)
    body = to_bytes("test")
    mock_socket.recv.side_effect = [header, body]

    result = recv_data(mock_socket)
    assert result == body

def test_recv_data_incomplete_header(mock_socket, mocker):
    # Mock the recv method to return an incomplete header
    mock_socket.recv.side_effect = [b'', b'']

    result = recv_data(mock_socket)
    assert result is None

def test_recv_data_incomplete_body(mock_socket, mocker):
    # Mock the recv method to return a complete header but incomplete body
    header = struct.pack('!Q', 4)
    mock_socket.recv.side_effect = [header, to_bytes("te"), b'']

    result = recv_data(mock_socket)
    assert result is None

def test_recv_data_empty_socket(mock_socket, mocker):
    # Mock the recv method to return empty data
    mock_socket.recv.side_effect = [b'']

    result = recv_data(mock_socket)
    assert result is None
