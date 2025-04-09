# file lib/ansible/module_utils/connection.py:122-125
# lines [122, 123, 124, 125]
# branches ['123->124', '123->125']

import pytest
from ansible.module_utils.connection import Connection

def test_connection_init_with_none_socket_path():
    with pytest.raises(AssertionError, match='socket_path must be a value'):
        Connection(None)

def test_connection_init_with_valid_socket_path():
    socket_path = '/valid/socket/path'
    conn = Connection(socket_path)
    assert conn.socket_path == socket_path
