# file lib/ansible/plugins/connection/paramiko_ssh.py:475-482
# lines [477, 478, 479, 481, 482]
# branches ['478->479', '478->481']

import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext
from unittest.mock import MagicMock

# Assuming SFTP_CONNECTION_CACHE is a global variable in the module
from ansible.plugins.connection.paramiko_ssh import SFTP_CONNECTION_CACHE

@pytest.fixture
def mock_play_context():
    mock_context = MagicMock(spec=PlayContext)
    mock_context.remote_addr = 'test_addr'
    mock_context.remote_user = 'test_user'
    mock_context.shell = 'sh'
    mock_context.executable = '/bin/sh'
    return mock_context

@pytest.fixture
def mock_connection(mock_play_context):
    conn = Connection(mock_play_context, None, None, None)
    conn._connect = MagicMock()
    conn._connect().ssh = MagicMock()
    conn._connect().ssh.open_sftp = MagicMock()
    return conn

def test_connect_sftp_cache_hit(mock_connection, mock_play_context):
    # Prepopulate the cache to simulate a cache hit
    cache_key = "%s__%s__" % (mock_play_context.remote_addr, mock_play_context.remote_user)
    SFTP_CONNECTION_CACHE[cache_key] = 'cached_sftp_connection'

    # Run the method that should hit the cache
    result = mock_connection._connect_sftp()

    # Assert that the result is from the cache and the open_sftp method was not called
    assert result == 'cached_sftp_connection'
    mock_connection._connect().ssh.open_sftp.assert_not_called()

    # Clean up the cache to not affect other tests
    del SFTP_CONNECTION_CACHE[cache_key]

def test_connect_sftp_cache_miss(mock_connection, mock_play_context):
    # Ensure the cache is empty to simulate a cache miss
    cache_key = "%s__%s__" % (mock_play_context.remote_addr, mock_play_context.remote_user)
    SFTP_CONNECTION_CACHE.pop(cache_key, None)

    # Run the method that should miss the cache and create a new connection
    mock_connection._connect().ssh.open_sftp.return_value = 'new_sftp_connection'
    result = mock_connection._connect_sftp()

    # Assert that the result is a new connection and the open_sftp method was called
    assert result == 'new_sftp_connection'
    mock_connection._connect().ssh.open_sftp.assert_called_once()

    # Clean up the cache to not affect other tests
    del SFTP_CONNECTION_CACHE[cache_key]
