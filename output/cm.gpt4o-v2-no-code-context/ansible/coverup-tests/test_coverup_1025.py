# file: lib/ansible/plugins/connection/paramiko_ssh.py:475-482
# asked: {"lines": [477, 478, 479, 481, 482], "branches": [[478, 479], [478, 481]]}
# gained: {"lines": [477, 478, 479, 481, 482], "branches": [[478, 479], [478, 481]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming ConnectionBase and SFTP_CONNECTION_CACHE are imported from the appropriate module
from ansible.plugins.connection.paramiko_ssh import Connection, SFTP_CONNECTION_CACHE

@pytest.fixture
def connection():
    play_context = MagicMock()
    play_context.remote_addr = '127.0.0.1'
    play_context.remote_user = 'user'
    play_context.executable = '/bin/sh'
    play_context.shell = 'sh'
    new_stdin = MagicMock()
    conn = Connection(play_context, new_stdin)
    return conn

def test_connect_sftp_cache_hit(connection):
    cache_key = "127.0.0.1__user__"
    mock_sftp = MagicMock()
    SFTP_CONNECTION_CACHE[cache_key] = mock_sftp

    result = connection._connect_sftp()

    assert result == mock_sftp
    assert SFTP_CONNECTION_CACHE[cache_key] == mock_sftp

def test_connect_sftp_cache_miss(connection):
    cache_key = "127.0.0.1__user__"
    mock_ssh = MagicMock()
    mock_sftp = MagicMock()
    mock_ssh.open_sftp.return_value = mock_sftp

    with patch.object(connection, '_connect', return_value=MagicMock(ssh=mock_ssh)):
        result = connection._connect_sftp()

    assert result == mock_sftp
    assert SFTP_CONNECTION_CACHE[cache_key] == mock_sftp

@pytest.fixture(autouse=True)
def cleanup():
    yield
    SFTP_CONNECTION_CACHE.clear()
