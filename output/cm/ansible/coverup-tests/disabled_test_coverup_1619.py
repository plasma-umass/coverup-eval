# file lib/ansible/plugins/connection/paramiko_ssh.py:238-246
# lines [239, 240, 241, 243, 245, 246]
# branches ['240->241', '240->243']

import pytest
from unittest.mock import MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection as ParamikoSSHConnection
from ansible.playbook.play_context import PlayContext

# Mock the connection cache
SSH_CONNECTION_CACHE = {}

@pytest.fixture
def paramiko_ssh_connection(mocker):
    mocker.patch('ansible.plugins.connection.paramiko_ssh.SSH_CONNECTION_CACHE', SSH_CONNECTION_CACHE)
    play_context = PlayContext()
    play_context.shell = 'sh'
    new_stdin = MagicMock()
    connection = ParamikoSSHConnection(play_context, new_stdin)
    connection._cache_key = lambda: "test_key"
    connection._connect_uncached = mocker.Mock(return_value="SSH_CONNECTION_OBJECT")
    return connection

def test_connect_caches_connection(paramiko_ssh_connection):
    # Ensure the cache is empty before the test
    SSH_CONNECTION_CACHE.clear()

    # Connect for the first time, should use _connect_uncached
    conn1 = paramiko_ssh_connection._connect()
    assert conn1.ssh == "SSH_CONNECTION_OBJECT"
    assert conn1._connected
    assert SSH_CONNECTION_CACHE["test_key"] == "SSH_CONNECTION_OBJECT"

    # Connect again, should use the cached connection
    conn2 = paramiko_ssh_connection._connect()
    assert conn2.ssh == "SSH_CONNECTION_OBJECT"
    assert conn2._connected
    assert SSH_CONNECTION_CACHE["test_key"] == "SSH_CONNECTION_OBJECT"
    assert paramiko_ssh_connection._connect_uncached.call_count == 1  # Ensure uncached connect was only called once

    # Clean up after the test
    SSH_CONNECTION_CACHE.clear()
