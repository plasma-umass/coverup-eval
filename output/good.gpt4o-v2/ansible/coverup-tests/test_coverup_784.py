# file: lib/ansible/module_utils/connection.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
import socket
import struct
from unittest import mock
from ansible.module_utils.connection import send_data

def test_send_data():
    # Create a mock socket object
    mock_socket = mock.Mock(spec=socket.socket)
    
    # Data to be sent
    data = b"test data"
    
    # Call the function
    send_data(mock_socket, data)
    
    # Calculate the expected packed length
    packed_len = struct.pack('!Q', len(data))
    
    # Assert sendall was called with the correct parameters
    mock_socket.sendall.assert_called_once_with(packed_len + data)
