# file lib/ansible/module_utils/connection.py:204-222
# lines [204, 205, 206, 207, 209, 210, 212, 213, 214, 215, 216, 217, 220, 222]
# branches []

import pytest
import socket
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_bytes, to_text
import tempfile
import os

# Mock send_data and recv_data functions
def mock_send_data(sock, data):
    pass

def mock_recv_data(sock):
    return b'response data'

@pytest.fixture
def mock_socket(mocker):
    socket_mock = mocker.patch('socket.socket')
    socket_instance = socket_mock.return_value
    socket_instance.connect.side_effect = socket.error
    mocker.patch('ansible.module_utils.connection.send_data', side_effect=mock_send_data)
    mocker.patch('ansible.module_utils.connection.recv_data', side_effect=mock_recv_data)
    return socket_instance

def test_connection_send_socket_error(mock_socket):
    # Create a temporary file to simulate a Unix socket path
    with tempfile.NamedTemporaryFile() as tmp:
        socket_path = tmp.name

    conn = Connection(socket_path)

    # Expect ConnectionError to be raised due to the mocked socket.error
    with pytest.raises(ConnectionError) as exc_info:
        conn.send('test data')

    # Check if the exception message contains the socket path
    assert socket_path in str(exc_info.value)

    # Clean up: No need to close the socket manually as it's handled by the context manager
