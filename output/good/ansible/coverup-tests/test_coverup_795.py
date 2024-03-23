# file lib/ansible/module_utils/connection.py:70-72
# lines [70, 71, 72]
# branches []

import pytest
import struct
from unittest.mock import MagicMock

# Assuming the send_data function is part of a class named Connection in connection.py
# and the module path is ansible.module_utils.connection

@pytest.fixture
def socket_mock():
    return MagicMock()

def test_send_data(socket_mock):
    # Assuming Connection class has an __init__ that accepts a socket_path argument
    # and that the send_data function does not require an instance of Connection
    from ansible.module_utils.connection import send_data

    # Mock data to send
    data = b"test_data"
    packed_len = struct.pack('!Q', len(data))

    # Call the send_data function with the mock socket and data
    send_data(socket_mock, data)

    # Verify that the socket's sendall method was called with the correct arguments
    socket_mock.sendall.assert_called_once_with(packed_len + data)
