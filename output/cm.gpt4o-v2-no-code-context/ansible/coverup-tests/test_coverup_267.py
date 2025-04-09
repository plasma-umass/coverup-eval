# file: lib/ansible/module_utils/connection.py:204-222
# asked: {"lines": [204, 205, 206, 207, 209, 210, 212, 213, 214, 215, 216, 217, 220, 222], "branches": []}
# gained: {"lines": [204, 205, 206, 207, 209, 210, 212, 213, 214, 215, 216, 217, 220, 222], "branches": []}

import pytest
import socket
from unittest import mock
from ansible.module_utils.connection import Connection, ConnectionError
from ansible.module_utils._text import to_bytes, to_text

@pytest.fixture
def connection():
    conn = Connection(socket_path="/tmp/test_socket")
    return conn

def test_send_success(monkeypatch, connection):
    mock_socket = mock.Mock()
    mock_socket.recv.return_value = to_bytes("response")
    
    def mock_socket_create(*args, **kwargs):
        return mock_socket
    
    monkeypatch.setattr(socket, 'socket', mock_socket_create)
    
    def mock_send_data(sock, data):
        assert data == to_bytes("test_data")
    
    def mock_recv_data(sock):
        return to_bytes("response")
    
    monkeypatch.setattr('ansible.module_utils.connection.send_data', mock_send_data)
    monkeypatch.setattr('ansible.module_utils.connection.recv_data', mock_recv_data)
    
    response = connection.send("test_data")
    assert response == "response"
    mock_socket.connect.assert_called_once_with("/tmp/test_socket")
    mock_socket.close.assert_called_once()

def test_send_socket_error(monkeypatch, connection):
    mock_socket = mock.Mock()
    mock_socket.connect.side_effect = socket.error("Connection error")
    
    def mock_socket_create(*args, **kwargs):
        return mock_socket
    
    monkeypatch.setattr(socket, 'socket', mock_socket_create)
    
    with pytest.raises(ConnectionError) as excinfo:
        connection.send("test_data")
    
    assert "unable to connect to socket" in str(excinfo.value)
    assert mock_socket.close.call_count == 1
