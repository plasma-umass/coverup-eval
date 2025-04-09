# file: tornado/netutil.py:191-223
# asked: {"lines": [209], "branches": [[207, 209]]}
# gained: {"lines": [209], "branches": [[207, 209]]}

import os
import socket
import stat
import errno
import pytest
from unittest import mock
from tornado.netutil import bind_unix_socket

def test_bind_unix_socket_existing_non_socket_file(tmp_path):
    file_path = tmp_path / "testfile"
    file_path.write_text("This is a regular file")

    with pytest.raises(ValueError, match="File .* exists and is not a socket"):
        bind_unix_socket(str(file_path))

def test_bind_unix_socket_existing_socket_file(tmp_path):
    file_path = tmp_path / "testsocket"
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(str(file_path))
    sock.close()

    result_sock = bind_unix_socket(str(file_path))
    assert isinstance(result_sock, socket.socket)
    result_sock.close()

def test_bind_unix_socket_reuseaddr_error(monkeypatch):
    def mock_setsockopt(sock, level, optname, value):
        if optname == socket.SO_REUSEADDR:
            raise socket.error(errno.ENOPROTOOPT, "Protocol not available")

    monkeypatch.setattr(socket.socket, 'setsockopt', mock_setsockopt)

    file_path = "/tmp/testsocket"
    try:
        result_sock = bind_unix_socket(file_path)
        assert isinstance(result_sock, socket.socket)
        result_sock.close()
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

def test_bind_unix_socket_reuseaddr_other_error(monkeypatch):
    def mock_setsockopt(sock, level, optname, value):
        if optname == socket.SO_REUSEADDR:
            raise socket.error(errno.EINVAL, "Invalid argument")

    monkeypatch.setattr(socket.socket, 'setsockopt', mock_setsockopt)

    file_path = "/tmp/testsocket"
    try:
        with pytest.raises(socket.error) as excinfo:
            bind_unix_socket(file_path)
        assert excinfo.value.errno == errno.EINVAL
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
