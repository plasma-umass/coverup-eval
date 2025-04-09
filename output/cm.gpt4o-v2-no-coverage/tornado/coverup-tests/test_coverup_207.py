# file: tornado/netutil.py:191-223
# asked: {"lines": [203, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223], "branches": [[207, 209], [207, 210], [216, 217], [216, 219]]}
# gained: {"lines": [203, 204, 205, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223], "branches": [[216, 217], [216, 219]]}

import os
import socket
import stat
import pytest
from tornado.netutil import bind_unix_socket

_DEFAULT_BACKLOG = 128

@pytest.fixture
def temp_socket_file(tmp_path):
    return str(tmp_path / "test_socket")

def test_bind_unix_socket_creates_socket(temp_socket_file):
    sock = bind_unix_socket(temp_socket_file)
    assert os.path.exists(temp_socket_file)
    assert stat.S_ISSOCK(os.stat(temp_socket_file).st_mode)
    sock.close()
    os.remove(temp_socket_file)

def test_bind_unix_socket_removes_existing_socket(temp_socket_file):
    initial_sock = bind_unix_socket(temp_socket_file)
    initial_sock.close()
    new_sock = bind_unix_socket(temp_socket_file)
    assert os.path.exists(temp_socket_file)
    assert stat.S_ISSOCK(os.stat(temp_socket_file).st_mode)
    new_sock.close()
    os.remove(temp_socket_file)

def test_bind_unix_socket_raises_on_existing_non_socket_file(temp_socket_file):
    with open(temp_socket_file, 'w') as f:
        f.write("This is a test file and not a socket.")
    with pytest.raises(ValueError, match="File .* exists and is not a socket"):
        bind_unix_socket(temp_socket_file)
    os.remove(temp_socket_file)

def test_bind_unix_socket_sets_correct_mode(temp_socket_file):
    mode = 0o777
    sock = bind_unix_socket(temp_socket_file, mode=mode)
    assert os.stat(temp_socket_file).st_mode & 0o777 == mode
    sock.close()
    os.remove(temp_socket_file)

def test_bind_unix_socket_sets_backlog(temp_socket_file, mocker):
    mock_listen = mocker.patch.object(socket.socket, 'listen')
    backlog = 50
    sock = bind_unix_socket(temp_socket_file, backlog=backlog)
    mock_listen.assert_called_with(backlog)
    sock.close()
    os.remove(temp_socket_file)
