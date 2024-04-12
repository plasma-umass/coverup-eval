# file lib/ansible/module_utils/connection.py:204-222
# lines [209, 210, 220, 222]
# branches []

import pytest
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_bytes, to_text

# Mock functions to be used in the test
def mock_send_data(socket, data):
    if data == b'raise_socket_error':
        raise OSError('Mocked socket error')  # Use OSError instead of socket.error
    socket.sendall(data)

def mock_recv_data(socket):
    return socket.recv(4096)

# Test function to cover missing lines/branches
@pytest.fixture
def mock_socket(mocker):
    mock_socket = mocker.patch('socket.socket')
    mock_socket.return_value.connect.return_value = None
    mock_socket.return_value.close.return_value = None
    mock_socket.return_value.sendall.return_value = None
    mock_socket.return_value.recv.return_value = b'response_data'
    return mock_socket

def test_connection_send_receive(mock_socket, mocker):
    mocker.patch('ansible.module_utils.connection.send_data', side_effect=mock_send_data)
    mocker.patch('ansible.module_utils.connection.recv_data', side_effect=mock_recv_data)

    # Pass the required 'socket_path' argument to the Connection constructor
    connection = Connection(socket_path='/tmp/fake_socket_path')

    # Test normal send/receive
    response = connection.send('test_data')
    assert response == 'response_data'
    mock_socket.return_value.close.assert_called_once()

    # Reset mock to test exception handling
    mock_socket.reset_mock()
    mock_socket.return_value.close.reset_mock()

    # Test exception handling
    with pytest.raises(ConnectionError) as exc_info:
        connection.send('raise_socket_error')
    assert 'unable to connect to socket' in str(exc_info.value)
    mock_socket.return_value.close.assert_called_once()
