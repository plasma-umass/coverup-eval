# file: lib/ansible/module_utils/connection.py:204-222
# asked: {"lines": [204, 205, 206, 207, 209, 210, 212, 213, 214, 215, 216, 217, 220, 222], "branches": []}
# gained: {"lines": [204, 205, 206, 207, 209, 210, 212, 213, 214, 215, 216, 217, 220, 222], "branches": []}

import pytest
import socket
import struct
from unittest.mock import patch, MagicMock
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_bytes, to_text

@pytest.fixture
def mock_socket_path():
    return "/mock/socket/path"

@pytest.fixture
def connection(mock_socket_path):
    return Connection(mock_socket_path)

def test_send_success(connection, mocker):
    mock_socket = mocker.patch('socket.socket')
    mock_sf = MagicMock()
    mock_socket.return_value = mock_sf
    mock_sf.recv.return_value = struct.pack('!Q', len(b'response')) + b'response'

    data = 'test data'
    response = connection.send(data)

    mock_socket.assert_called_once_with(socket.AF_UNIX, socket.SOCK_STREAM)
    mock_sf.connect.assert_called_once_with(connection.socket_path)
    mock_sf.sendall.assert_called_once_with(struct.pack('!Q', len(to_bytes(data))) + to_bytes(data))
    assert response == 'response'
    mock_sf.close.assert_called_once()

def test_send_socket_error(connection, mocker):
    mock_socket = mocker.patch('socket.socket')
    mock_sf = MagicMock()
    mock_socket.return_value = mock_sf
    mock_sf.connect.side_effect = socket.error("Connection error")

    data = 'test data'
    with pytest.raises(ConnectionError) as excinfo:
        connection.send(data)

    assert "unable to connect to socket" in str(excinfo.value)
    assert excinfo.value.err == "Connection error"
    assert mock_sf.close.called
