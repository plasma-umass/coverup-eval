# file tornado/netutil.py:191-223
# lines [203, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 216, 217, 219, 220, 221, 222, 223]
# branches ['207->209', '207->210', '216->217', '216->219']

import os
import socket
import stat
import pytest
from tornado.netutil import bind_unix_socket

def test_bind_unix_socket_existing_socket(mocker):
    file = "/tmp/test_socket"
    
    # Ensure the file does not exist before the test
    if os.path.exists(file):
        os.remove(file)
    
    # Create a dummy socket file
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(file)
    sock.close()
    
    # Mock os.stat to return a stat result indicating a socket
    mock_stat_result = os.stat(file)
    mocker.patch('os.stat', return_value=mock_stat_result)
    
    # Ensure the file is recognized as a socket
    assert stat.S_ISSOCK(mock_stat_result.st_mode)
    
    # Call the function and ensure it does not raise an exception
    new_sock = bind_unix_socket(file)
    
    # Ensure the new socket is created and bound to the file
    assert isinstance(new_sock, socket.socket)
    assert os.path.exists(file)
    
    # Clean up
    new_sock.close()
    os.remove(file)

def test_bind_unix_socket_existing_non_socket_file(mocker):
    file = "/tmp/test_non_socket_file"
    
    # Ensure the file does not exist before the test
    if os.path.exists(file):
        os.remove(file)
    
    # Create a dummy non-socket file
    with open(file, 'w') as f:
        f.write("This is a test file.")
    
    # Mock os.stat to return a stat result indicating a regular file
    mock_stat_result = os.stat(file)
    mocker.patch('os.stat', return_value=mock_stat_result)
    
    # Ensure the file is recognized as a regular file
    assert not stat.S_ISSOCK(mock_stat_result.st_mode)
    
    # Call the function and ensure it raises a ValueError
    with pytest.raises(ValueError, match=r"File .* exists and is not a socket"):
        bind_unix_socket(file)
    
    # Clean up
    os.remove(file)
