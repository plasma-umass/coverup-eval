# file: lib/ansible/module_utils/connection.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import struct
import socket
import pytest
from unittest import mock

from ansible.module_utils.connection import send_data

def test_send_data():
    # Create a mock socket object
    mock_socket = mock.Mock(spec=socket.socket)
    
    # Define the data to be sent
    data = b"test data"
    
    # Call the function with the mock socket and data
    send_data(mock_socket, data)
    
    # Check that the socket's sendall method was called with the correct arguments
    packed_len = struct.pack('!Q', len(data))
    mock_socket.sendall.assert_called_once_with(packed_len + data)
