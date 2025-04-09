# file: lib/ansible/plugins/connection/paramiko_ssh.py:475-482
# asked: {"lines": [477, 478, 479, 481, 482], "branches": [[478, 479], [478, 481]]}
# gained: {"lines": [477, 478, 479, 481, 482], "branches": [[478, 479], [478, 481]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.paramiko_ssh import Connection, SFTP_CONNECTION_CACHE

@pytest.fixture
def mock_play_context():
    mock = MagicMock()
    mock.remote_addr = '127.0.0.1'
    mock.remote_user = 'user'
    mock.shell = 'sh'
    mock.executable = '/bin/sh'
    return mock

@pytest.fixture
def connection(mock_play_context):
    with patch('ansible.plugins.connection.get_shell_plugin', return_value=MagicMock()):
        return Connection(mock_play_context, new_stdin=None)

def test_connect_sftp_cache_hit(connection, mock_play_context):
    cache_key = f"{mock_play_context.remote_addr}__{mock_play_context.remote_user}__"
    mock_sftp = MagicMock()
    SFTP_CONNECTION_CACHE[cache_key] = mock_sftp

    result = connection._connect_sftp()

    assert result == mock_sftp
    assert SFTP_CONNECTION_CACHE[cache_key] == mock_sftp

def test_connect_sftp_cache_miss(connection, mock_play_context):
    cache_key = f"{mock_play_context.remote_addr}__{mock_play_context.remote_user}__"
    mock_ssh = MagicMock()
    mock_sftp = MagicMock()
    mock_ssh.open_sftp.return_value = mock_sftp
    connection._connect = MagicMock(return_value=MagicMock(ssh=mock_ssh))

    result = connection._connect_sftp()

    assert result == mock_sftp
    assert SFTP_CONNECTION_CACHE[cache_key] == mock_sftp
