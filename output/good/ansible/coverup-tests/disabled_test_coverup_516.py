# file lib/ansible/plugins/connection/paramiko_ssh.py:475-482
# lines [475, 477, 478, 479, 481, 482]
# branches ['478->479', '478->481']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext

# Mock the SFTP_CONNECTION_CACHE to be used in the test
SFTP_CONNECTION_CACHE = {}

@pytest.fixture
def mock_play_context():
    mock_context = MagicMock(spec=PlayContext)
    mock_context.remote_addr = 'test_addr'
    mock_context.remote_user = 'test_user'
    mock_context.shell = 'sh'
    return mock_context

@pytest.fixture
def mock_connection(mock_play_context):
    with patch('ansible.plugins.connection.paramiko_ssh.Connection._connect') as mock_connect, \
         patch('ansible.plugins.connection.paramiko_ssh.SFTP_CONNECTION_CACHE', SFTP_CONNECTION_CACHE):
        mock_connect.return_value = MagicMock(ssh=MagicMock(open_sftp=MagicMock(return_value='sftp_connection')))
        conn = Connection(mock_play_context, None, None)
        yield conn

def test_connect_sftp_first_time(mock_connection, mock_play_context):
    # Test the branch where the SFTP connection is not in the cache
    sftp = mock_connection._connect_sftp()
    assert sftp == 'sftp_connection'
    cache_key = "%s__%s__" % (mock_play_context.remote_addr, mock_play_context.remote_user)
    assert cache_key in SFTP_CONNECTION_CACHE
    assert SFTP_CONNECTION_CACHE[cache_key] == 'sftp_connection'

def test_connect_sftp_from_cache(mock_connection, mock_play_context):
    # Test the branch where the SFTP connection is retrieved from the cache
    cache_key = "%s__%s__" % (mock_play_context.remote_addr, mock_play_context.remote_user)
    SFTP_CONNECTION_CACHE[cache_key] = 'cached_sftp_connection'
    sftp = mock_connection._connect_sftp()
    assert sftp == 'cached_sftp_connection'
