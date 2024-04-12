# file tornado/netutil.py:191-223
# lines [206, 207, 209, 216, 217, 219]
# branches ['207->209', '207->210', '216->217', '216->219']

import errno
import os
import pytest
import socket
from unittest.mock import patch
from tornado.netutil import bind_unix_socket

@pytest.fixture
def unix_socket_path(tmp_path):
    # Use a unique file name to avoid conflicts with other tests
    return str(tmp_path / "test_socket.sock")

def test_bind_unix_socket_error_handling(unix_socket_path):
    # Test the case where SO_REUSEADDR is not supported (simulating Hurd)
    with patch('socket.socket.setsockopt') as mock_setsockopt:
        mock_setsockopt.side_effect = OSError(errno.ENOPROTOOPT, "Protocol not available")
        bind_unix_socket(unix_socket_path)  # Should not raise an exception

    # Ensure the socket file is removed before creating a regular file
    if os.path.exists(unix_socket_path):
        os.remove(unix_socket_path)

    # Test the case where the file exists and is not a socket
    with open(unix_socket_path, 'w') as f:
        f.write('not a socket')
    with pytest.raises(ValueError):
        bind_unix_socket(unix_socket_path)

    # Clean up
    os.remove(unix_socket_path)

def test_bind_unix_socket_existing_socket(unix_socket_path):
    # Create a dummy socket file
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(unix_socket_path)
    sock.close()

    # Test the case where the file exists and is a socket
    new_sock = bind_unix_socket(unix_socket_path)
    assert os.path.exists(unix_socket_path)
    new_sock.close()

    # Clean up
    os.remove(unix_socket_path)
