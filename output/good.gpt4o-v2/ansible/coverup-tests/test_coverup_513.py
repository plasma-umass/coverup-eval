# file: lib/ansible/plugins/connection/paramiko_ssh.py:475-482
# asked: {"lines": [475, 477, 478, 479, 481, 482], "branches": [[478, 479], [478, 481]]}
# gained: {"lines": [475, 477, 478, 479, 481, 482], "branches": [[478, 479], [478, 481]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.paramiko_ssh import Connection, SFTP_CONNECTION_CACHE

class MockPlayContext:
    remote_addr = '127.0.0.1'
    remote_user = 'test_user'
    shell = None
    executable = '/bin/sh'

@pytest.fixture
def connection():
    play_context = MockPlayContext()
    new_stdin = MagicMock()
    return Connection(play_context, new_stdin)

def test_connect_sftp_cache_hit(connection):
    cache_key = f"{connection._play_context.remote_addr}__{connection._play_context.remote_user}__"
    mock_sftp = MagicMock()
    SFTP_CONNECTION_CACHE[cache_key] = mock_sftp

    result = connection._connect_sftp()

    assert result == mock_sftp
    assert SFTP_CONNECTION_CACHE[cache_key] == mock_sftp

def test_connect_sftp_cache_miss(connection):
    cache_key = f"{connection._play_context.remote_addr}__{connection._play_context.remote_user}__"
    mock_ssh = MagicMock()
    mock_ssh.open_sftp.return_value = 'sftp_connection'
    mock_connect = MagicMock()
    mock_connect.ssh = mock_ssh

    with patch.object(connection, '_connect', return_value=mock_connect):
        result = connection._connect_sftp()

    assert result == 'sftp_connection'
    assert SFTP_CONNECTION_CACHE[cache_key] == 'sftp_connection'
