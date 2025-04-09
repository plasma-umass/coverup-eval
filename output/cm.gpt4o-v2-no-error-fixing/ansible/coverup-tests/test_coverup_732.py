# file: lib/ansible/module_utils/connection.py:75-90
# asked: {"lines": [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[78, 79], [78, 83], [80, 81], [80, 82], [85, 86], [85, 90], [87, 88], [87, 89]]}
# gained: {"lines": [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[78, 79], [78, 83], [80, 81], [80, 82], [85, 86], [85, 90], [87, 88], [87, 89]]}

import pytest
import struct
from unittest.mock import Mock
from ansible.module_utils._text import to_bytes
from ansible.module_utils.connection import recv_data

def test_recv_data_complete(monkeypatch):
    # Mock socket with specific recv behavior
    mock_socket = Mock()
    
    # Define the behavior of recv to simulate receiving header and data
    def mock_recv(num_bytes):
        if num_bytes == 8:
            return struct.pack('!Q', 4)  # Header indicating 4 bytes of data
        elif num_bytes == 4:
            return b'test'  # The actual data
        return b''
    
    mock_socket.recv.side_effect = mock_recv
    
    # Call the function with the mocked socket
    result = recv_data(mock_socket)
    
    # Assertions to verify the correct behavior
    assert result == b'test'

def test_recv_data_incomplete_header(monkeypatch):
    # Mock socket with specific recv behavior
    mock_socket = Mock()
    
    # Define the behavior of recv to simulate incomplete header
    def mock_recv(num_bytes):
        if num_bytes == 8:
            return b'\x00\x00\x00\x00'  # Incomplete header
        return b''
    
    mock_socket.recv.side_effect = mock_recv
    
    # Call the function with the mocked socket
    result = recv_data(mock_socket)
    
    # Assertions to verify the correct behavior
    assert result is None

def test_recv_data_incomplete_data(monkeypatch):
    # Mock socket with specific recv behavior
    mock_socket = Mock()
    
    # Define the behavior of recv to simulate receiving header but incomplete data
    def mock_recv(num_bytes):
        if num_bytes == 8:
            return struct.pack('!Q', 4)  # Header indicating 4 bytes of data
        elif num_bytes == 4:
            return b'te'  # Incomplete data
        return b''
    
    mock_socket.recv.side_effect = mock_recv
    
    # Call the function with the mocked socket
    result = recv_data(mock_socket)
    
    # Assertions to verify the correct behavior
    assert result is None
