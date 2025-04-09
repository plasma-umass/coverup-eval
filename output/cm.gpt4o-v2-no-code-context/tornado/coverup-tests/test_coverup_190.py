# file: tornado/netutil.py:191-223
# asked: {"lines": [206, 207, 209], "branches": [[207, 209], [207, 210]]}
# gained: {"lines": [206, 207], "branches": [[207, 210]]}

import os
import socket
import errno
import stat
import pytest
from unittest import mock
from tornado.netutil import bind_unix_socket

def test_bind_unix_socket_reuseaddr_error(monkeypatch):
    # Mock socket creation and setsockopt to raise an error
    mock_socket = mock.Mock()
    mock_socket.setsockopt.side_effect = socket.error(errno.ENOPROTOOPT, "Protocol not available")
    
    def mock_socket_init(*args, **kwargs):
        return mock_socket
    
    monkeypatch.setattr(socket, 'socket', mock_socket_init)
    
    # Ensure the function runs without raising an exception
    with pytest.raises(socket.error):
        bind_unix_socket("/tmp/test_socket")
    
    # Verify that setsockopt was called with SO_REUSEADDR
    mock_socket.setsockopt.assert_called_with(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def test_bind_unix_socket_cleanup(monkeypatch):
    # Create a temporary file to act as the socket
    test_socket_path = "/tmp/test_socket"
    with open(test_socket_path, 'w') as f:
        f.write("test")
    
    # Ensure the file is not a socket
    assert not stat.S_ISSOCK(os.stat(test_socket_path).st_mode)
    
    # Mock socket creation
    mock_socket = mock.Mock()
    
    def mock_socket_init(*args, **kwargs):
        return mock_socket
    
    monkeypatch.setattr(socket, 'socket', mock_socket_init)
    
    # Ensure the function raises a ValueError
    with pytest.raises(ValueError):
        bind_unix_socket(test_socket_path)
    
    # Clean up
    os.remove(test_socket_path)
    
    # Verify that bind and listen were not called
    mock_socket.bind.assert_not_called()
    mock_socket.listen.assert_not_called()
