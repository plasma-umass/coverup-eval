# file: tornado/netutil.py:191-223
# asked: {"lines": [203, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223], "branches": [[207, 209], [207, 210], [216, 217], [216, 219]]}
# gained: {"lines": [203, 204, 205, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223], "branches": [[216, 217], [216, 219]]}

import os
import socket
import stat
import pytest
from tornado.netutil import bind_unix_socket

def test_bind_unix_socket_creates_socket():
    file = "/tmp/test_socket"
    mode = 0o600
    backlog = 128

    # Ensure the file does not exist before the test
    if os.path.exists(file):
        os.remove(file)

    sock = bind_unix_socket(file, mode, backlog)

    # Check that the socket file is created
    assert os.path.exists(file)
    assert stat.S_ISSOCK(os.stat(file).st_mode)

    # Clean up
    sock.close()
    os.remove(file)

def test_bind_unix_socket_removes_existing_socket():
    file = "/tmp/test_socket"
    mode = 0o600
    backlog = 128

    # Create an existing socket file
    existing_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    existing_sock.bind(file)

    sock = bind_unix_socket(file, mode, backlog)

    # Check that the new socket file is created
    assert os.path.exists(file)
    assert stat.S_ISSOCK(os.stat(file).st_mode)

    # Clean up
    sock.close()
    os.remove(file)

def test_bind_unix_socket_raises_error_on_existing_non_socket_file():
    file = "/tmp/test_socket"
    mode = 0o600
    backlog = 128

    # Create a regular file
    with open(file, "w") as f:
        f.write("This is a test file.")

    with pytest.raises(ValueError, match="File .* exists and is not a socket"):
        bind_unix_socket(file, mode, backlog)

    # Clean up
    os.remove(file)
