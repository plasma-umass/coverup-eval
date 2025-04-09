# file: lib/ansible/plugins/connection/paramiko_ssh.py:238-246
# asked: {"lines": [238, 239, 240, 241, 243, 245, 246], "branches": [[240, 241], [240, 243]]}
# gained: {"lines": [238, 239, 240, 241, 243, 245, 246], "branches": [[240, 241], [240, 243]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection, SSH_CONNECTION_CACHE

@pytest.fixture
def play_context():
    class PlayContext:
        remote_addr = '127.0.0.1'
        remote_user = 'user'
        port = 22
        private_key_file = None
        password = None
        timeout = 10
        shell = None
        executable = '/bin/sh'
    return PlayContext()

@pytest.fixture
def connection(play_context):
    return Connection(play_context, new_stdin=None)

def test_connect_cached(connection, monkeypatch):
    mock_ssh = MagicMock()
    cache_key = connection._cache_key()
    SSH_CONNECTION_CACHE[cache_key] = mock_ssh

    connection._connect()

    assert connection.ssh == mock_ssh
    assert connection._connected

    del SSH_CONNECTION_CACHE[cache_key]

def test_connect_uncached(connection, monkeypatch):
    mock_ssh = MagicMock()
    monkeypatch.setattr(connection, '_connect_uncached', lambda: mock_ssh)
    cache_key = connection._cache_key()

    connection._connect()

    assert connection.ssh == mock_ssh
    assert connection._connected
    assert SSH_CONNECTION_CACHE[cache_key] == mock_ssh

    del SSH_CONNECTION_CACHE[cache_key]
