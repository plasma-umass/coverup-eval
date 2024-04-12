# file lib/ansible/module_utils/connection.py:122-125
# lines [122, 123, 124, 125]
# branches ['123->124', '123->125']

import pytest
from ansible.module_utils.connection import Connection

def test_connection_initialization_success():
    socket_path = '/tmp/ansible-socket'
    conn = Connection(socket_path)
    assert conn.socket_path == socket_path

def test_connection_initialization_failure(mocker):
    with pytest.raises(AssertionError) as excinfo:
        conn = Connection(None)
    assert 'socket_path must be a value' in str(excinfo.value)
