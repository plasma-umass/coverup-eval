# file lib/ansible/module_utils/connection.py:75-90
# lines [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
# branches ['78->79', '78->83', '80->81', '80->82', '85->86', '85->90', '87->88', '87->89']

import pytest
import struct
from unittest.mock import MagicMock

# Assuming the recv_data function is part of a class or module named `connection`
from ansible.module_utils import connection

@pytest.fixture
def mock_socket():
    s = MagicMock()
    s.recv.side_effect = [
        struct.pack('!Q', 4),  # header indicating 4 bytes of data
        b'test',               # 4 bytes of actual data
        b''                    # simulate end of stream
    ]
    return s

def test_recv_data_full_coverage(mock_socket):
    # Test the recv_data function to ensure full coverage
    data = connection.recv_data(mock_socket)
    assert data == b'test', "Data received does not match expected value"

    # Test the recv_data function with a closed socket
    mock_socket.recv.side_effect = [b'', b'']  # simulate closed socket
    data = connection.recv_data(mock_socket)
    assert data is None, "Data should be None when socket is closed"

    # Test the recv_data function with partial header
    mock_socket.recv.side_effect = [
        struct.pack('!Q', 4)[:4],  # partial header
        struct.pack('!Q', 4)[4:],  # rest of the header
        b'test',                   # 4 bytes of actual data
    ]
    data = connection.recv_data(mock_socket)
    assert data == b'test', "Data received does not match expected value after partial header"

    # Test the recv_data function with partial data
    mock_socket.recv.side_effect = [
        struct.pack('!Q', 4),  # header indicating 4 bytes of data
        b'te',                 # 2 bytes of actual data
        b'st',                 # remaining 2 bytes of actual data
    ]
    data = connection.recv_data(mock_socket)
    assert data == b'test', "Data received does not match expected value after partial data"

    # Test the recv_data function with no data after header
    mock_socket.recv.side_effect = [
        struct.pack('!Q', 4),  # header indicating 4 bytes of data
        b''                    # simulate no data after header
    ]
    data = connection.recv_data(mock_socket)
    assert data is None, "Data should be None when no data is received after header"
