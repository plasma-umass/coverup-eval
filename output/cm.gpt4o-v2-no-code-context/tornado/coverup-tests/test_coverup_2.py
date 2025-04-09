# file: tornado/netutil.py:191-223
# asked: {"lines": [191, 192, 203, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223], "branches": [[207, 209], [207, 210], [216, 217], [216, 219]]}
# gained: {"lines": [191, 192, 203, 204, 205, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223], "branches": [[216, 217], [216, 219]]}

import os
import socket
import stat
import pytest
from tornado.netutil import bind_unix_socket

@pytest.fixture
def temp_socket_file(tmp_path):
    file_path = tmp_path / "test_socket"
    yield str(file_path)
    if file_path.exists():
        file_path.unlink()

def test_bind_unix_socket_creates_socket(temp_socket_file):
    sock = bind_unix_socket(temp_socket_file)
    assert isinstance(sock, socket.socket)
    assert sock.family == socket.AF_UNIX
    assert sock.type == socket.SOCK_STREAM
    sock.close()

def test_bind_unix_socket_removes_existing_socket(temp_socket_file):
    # Create an existing socket file
    existing_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    existing_sock.bind(temp_socket_file)
    existing_sock.close()

    # Now bind using bind_unix_socket, which should remove the existing socket
    sock = bind_unix_socket(temp_socket_file)
    assert isinstance(sock, socket.socket)
    assert sock.family == socket.AF_UNIX
    assert sock.type == socket.SOCK_STREAM
    sock.close()

def test_bind_unix_socket_raises_on_existing_non_socket_file(temp_socket_file):
    # Create a regular file
    with open(temp_socket_file, 'w') as f:
        f.write("This is a test file")

    with pytest.raises(ValueError, match="File .* exists and is not a socket"):
        bind_unix_socket(temp_socket_file)

def test_bind_unix_socket_sets_correct_permissions(temp_socket_file):
    mode = 0o644
    sock = bind_unix_socket(temp_socket_file, mode=mode)
    assert isinstance(sock, socket.socket)
    assert sock.family == socket.AF_UNIX
    assert sock.type == socket.SOCK_STREAM
    sock.close()

    # Check the file mode
    file_mode = stat.S_IMODE(os.stat(temp_socket_file).st_mode)
    assert file_mode == mode
