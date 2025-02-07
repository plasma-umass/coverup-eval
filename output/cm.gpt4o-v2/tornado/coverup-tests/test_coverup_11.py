# file: tornado/netutil.py:191-223
# asked: {"lines": [191, 192, 203, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223], "branches": [[207, 209], [207, 210], [216, 217], [216, 219]]}
# gained: {"lines": [191, 192, 203, 204, 205, 206, 207, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223], "branches": [[207, 210], [216, 217], [216, 219]]}

import os
import socket
import stat
import errno
import pytest
from unittest import mock
from tornado.netutil import bind_unix_socket
from tornado.util import errno_from_exception

def test_bind_unix_socket_creates_socket():
    file = "/tmp/test_socket"
    mode = 0o600
    backlog = 128

    # Ensure the file does not exist before the test
    if os.path.exists(file):
        os.remove(file)

    sock = bind_unix_socket(file, mode, backlog)

    assert isinstance(sock, socket.socket)
    assert sock.getsockname() == file
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
    existing_sock.listen(backlog)
    existing_sock.close()

    sock = bind_unix_socket(file, mode, backlog)

    assert isinstance(sock, socket.socket)
    assert sock.getsockname() == file
    assert stat.S_ISSOCK(os.stat(file).st_mode)

    # Clean up
    sock.close()
    os.remove(file)

def test_bind_unix_socket_raises_error_on_existing_non_socket_file():
    file = "/tmp/test_socket"
    mode = 0o600
    backlog = 128

    # Create a regular file
    with open(file, 'w') as f:
        f.write("This is a test file.")

    with pytest.raises(ValueError, match="File .* exists and is not a socket"):
        bind_unix_socket(file, mode, backlog)

    # Clean up
    os.remove(file)

def test_bind_unix_socket_handles_errno_enoprotoopt(monkeypatch):
    file = "/tmp/test_socket"
    mode = 0o600
    backlog = 128

    # Mock socket to raise ENOPROTOOPT error
    class MockSocket(socket.socket):
        def setsockopt(self, level, optname, value):
            if level == socket.SOL_SOCKET and optname == socket.SO_REUSEADDR:
                err = socket.error()
                err.errno = errno.ENOPROTOOPT
                raise err
            super().setsockopt(level, optname, value)

    monkeypatch.setattr(socket, 'socket', MockSocket)

    sock = bind_unix_socket(file, mode, backlog)

    assert isinstance(sock, socket.socket)
    assert sock.getsockname() == file
    assert stat.S_ISSOCK(os.stat(file).st_mode)

    # Clean up
    sock.close()
    os.remove(file)
    monkeypatch.undo()
