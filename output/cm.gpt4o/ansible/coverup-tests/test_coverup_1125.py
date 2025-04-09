# file lib/ansible/module_utils/connection.py:204-222
# lines [205, 206, 207, 209, 210, 212, 213, 214, 215, 216, 217, 220, 222]
# branches []

import pytest
import socket
from unittest import mock
from ansible.module_utils.connection import Connection, ConnectionError

@pytest.fixture
def mock_socket_path(tmp_path):
    return str(tmp_path / "mock_socket")

@pytest.fixture
def connection(mock_socket_path):
    conn = Connection(mock_socket_path)
    return conn

def test_send_success(mocker, connection):
    mock_socket = mocker.patch('socket.socket')
    mock_sf = mock_socket.return_value
    mock_sf.recv.return_value = b'response_data'
    
    mocker.patch('ansible.module_utils.connection.send_data')
    mocker.patch('ansible.module_utils.connection.recv_data', return_value=b'response_data')
    
    response = connection.send('test_data')
    
    mock_socket.assert_called_once_with(socket.AF_UNIX, socket.SOCK_STREAM)
    mock_sf.connect.assert_called_once_with(connection.socket_path)
    mock_sf.close.assert_called_once()
    assert response == 'response_data'

def test_send_socket_error(mocker, connection):
    mock_socket = mocker.patch('socket.socket')
    mock_sf = mock_socket.return_value
    mock_sf.connect.side_effect = socket.error("Connection error")
    
    with pytest.raises(ConnectionError) as excinfo:
        connection.send('test_data')
    
    mock_socket.assert_called_once_with(socket.AF_UNIX, socket.SOCK_STREAM)
    mock_sf.connect.assert_called_once_with(connection.socket_path)
    mock_sf.close.assert_called_once()
    assert 'unable to connect to socket' in str(excinfo.value)
