# file: lib/ansible/module_utils/connection.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
import socket
import struct

from ansible.module_utils.connection import send_data

@pytest.fixture
def mock_socket(mocker):
    mock_socket = mocker.Mock(spec=socket.socket)
    return mock_socket

def test_send_data_success(mock_socket):
    data = b"test data"
    packed_len = struct.pack('!Q', len(data))
    mock_socket.sendall.return_value = None  # Simulate successful sendall

    result = send_data(mock_socket, data)

    mock_socket.sendall.assert_called_once_with(packed_len + data)
    assert result is None

def test_send_data_failure(mock_socket):
    data = b"test data"
    packed_len = struct.pack('!Q', len(data))
    mock_socket.sendall.side_effect = socket.error  # Simulate sendall failure

    with pytest.raises(socket.error):
        send_data(mock_socket, data)

    mock_socket.sendall.assert_called_once_with(packed_len + data)
