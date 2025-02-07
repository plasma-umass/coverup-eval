# file: lib/ansible/plugins/connection/paramiko_ssh.py:238-246
# asked: {"lines": [238, 239, 240, 241, 243, 245, 246], "branches": [[240, 241], [240, 243]]}
# gained: {"lines": [238, 239, 240, 241, 243, 245, 246], "branches": [[240, 241], [240, 243]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection, SSH_CONNECTION_CACHE

@pytest.fixture
def connection():
    play_context = MagicMock()
    play_context.remote_addr = '127.0.0.1'
    play_context.remote_user = 'user'
    play_context.port = 22
    play_context.password = 'password'
    play_context.private_key_file = None
    play_context.timeout = 10
    play_context.shell = 'sh'
    play_context.executable = '/bin/sh'
    new_stdin = MagicMock()
    return Connection(play_context, new_stdin)

def test_connect_cached(connection):
    ssh_mock = MagicMock()
    cache_key = connection._cache_key()
    SSH_CONNECTION_CACHE[cache_key] = ssh_mock

    with patch.object(connection, '_connect_uncached', return_value=ssh_mock) as connect_uncached_mock:
        connection._connect()
        assert connection.ssh == ssh_mock
        assert connection._connected
        connect_uncached_mock.assert_not_called()

    del SSH_CONNECTION_CACHE[cache_key]

def test_connect_uncached(connection):
    ssh_mock = MagicMock()
    cache_key = connection._cache_key()

    with patch.object(connection, '_connect_uncached', return_value=ssh_mock) as connect_uncached_mock:
        connection._connect()
        assert connection.ssh == ssh_mock
        assert connection._connected
        connect_uncached_mock.assert_called_once()

    del SSH_CONNECTION_CACHE[cache_key]
