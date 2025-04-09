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
    connection._connect_uncached = lambda: "uncached_connection"
    return connection

def test_connect_cached_connection(paramiko_ssh_connection):
    # Precondition: Ensure the cache is empty
    SSH_CONNECTION_CACHE.clear()

    # First connection should use _connect_uncached
    first_connection = paramiko_ssh_connection._connect()
    assert first_connection == paramiko_ssh_connection
    assert paramiko_ssh_connection._connected
    assert SSH_CONNECTION_CACHE["test_key"] == "uncached_connection"

    # Second connection should use the cached connection
    second_connection = paramiko_ssh_connection._connect()
    assert second_connection == paramiko_ssh_connection
    assert paramiko_ssh_connection._connected
    assert SSH_CONNECTION_CACHE["test_key"] == "uncached_connection"

    # Postcondition: Ensure the cache is cleared to not affect other tests
    SSH_CONNECTION_CACHE.clear()
