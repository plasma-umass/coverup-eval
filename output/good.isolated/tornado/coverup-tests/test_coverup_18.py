# file tornado/netutil.py:191-223
# lines [191, 192, 203, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223]
# branches ['207->209', '207->210', '216->217', '216->219']

import os
import pytest
import socket
import stat
import tempfile
from tornado.netutil import bind_unix_socket

@pytest.fixture
def unix_socket_path():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        pass  # Just to get a temporary file name, we'll delete it immediately
    os.unlink(tmp.name)  # Ensure the file does not exist
    yield tmp.name
    if os.path.exists(tmp.name):
        os.unlink(tmp.name)  # Clean up the socket file after test

def test_bind_unix_socket_creates_socket(unix_socket_path):
    # Now, actually create a socket
    sock = bind_unix_socket(unix_socket_path)
    assert os.path.exists(unix_socket_path), "Socket file was not created"
    assert stat.S_ISSOCK(os.stat(unix_socket_path).st_mode), "File is not a socket"

    # Clean up
    sock.close()
    os.unlink(unix_socket_path)
