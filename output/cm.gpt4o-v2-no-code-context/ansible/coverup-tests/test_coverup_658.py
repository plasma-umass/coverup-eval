# file: lib/ansible/module_utils/connection.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
import struct
import socket

# Mock socket class to simulate sendall behavior
class MockSocket:
    def __init__(self):
        self.data = b''

    def sendall(self, data):
        self.data += data

def test_send_data(monkeypatch):
    from ansible.module_utils.connection import send_data

    # Create a mock socket instance
    mock_socket = MockSocket()

    # Define the data to be sent
    data = b'test_data'

    # Use monkeypatch to replace the socket with our mock socket
    monkeypatch.setattr(socket, 'socket', lambda *args, **kwargs: mock_socket)

    # Call the function with the mock socket and data
    send_data(mock_socket, data)

    # Verify that the data was sent correctly
    packed_len = struct.pack('!Q', len(data))
    assert mock_socket.data == packed_len + data
