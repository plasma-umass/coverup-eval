# file: lib/ansible/module_utils/connection.py:75-90
# asked: {"lines": [81, 86, 87, 88, 89], "branches": [[80, 81], [85, 86], [87, 88], [87, 89]]}
# gained: {"lines": [81, 86, 87, 88, 89], "branches": [[80, 81], [85, 86], [87, 88], [87, 89]]}

import pytest
from unittest.mock import Mock
import struct
from ansible.module_utils.connection import recv_data

def test_recv_data_none_return():
    mock_socket = Mock()
    mock_socket.recv = Mock(side_effect=[b''])
    
    result = recv_data(mock_socket)
    
    assert result is None

def test_recv_data_partial_header():
    mock_socket = Mock()
    mock_socket.recv = Mock(side_effect=[b'\x00\x00\x00\x00\x00\x00\x00', b''])
    
    result = recv_data(mock_socket)
    
    assert result is None

def test_recv_data_partial_data():
    mock_socket = Mock()
    header = struct.pack('!Q', 4)
    mock_socket.recv = Mock(side_effect=[header, b'da', b''])
    
    result = recv_data(mock_socket)
    
    assert result is None

def test_recv_data_complete():
    mock_socket = Mock()
    header = struct.pack('!Q', 4)
    mock_socket.recv = Mock(side_effect=[header, b'data'])
    
    result = recv_data(mock_socket)
    
    assert result == b'data'
