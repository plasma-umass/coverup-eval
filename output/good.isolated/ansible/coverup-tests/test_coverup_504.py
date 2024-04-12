# file lib/ansible/plugins/connection/paramiko_ssh.py:238-246
# lines [238, 239, 240, 241, 243, 245, 246]
# branches ['240->241', '240->243']

import pytest
from unittest.mock import patch, MagicMock

# Assuming the ConnectionBase and SSH_CONNECTION_CACHE are defined elsewhere in the module
# and that _connect_uncached is a method of the Connection class that returns an SSH connection object.

# Import the Connection class from the actual module
from ansible.plugins.connection.paramiko_ssh import Connection, SSH_CONNECTION_CACHE

# Define a test case for the Connection class
@pytest.fixture
def connection():
    mock_play_context = MagicMock()
    mock_play_context.shell = 'sh'
    mock_new_stdin = MagicMock()
    with patch.object(Connection, '_connect_uncached', return_value=MagicMock()) as mock_connect_uncached:
        yield Connection(mock_play_context, mock_new_stdin)

def test_connect_with_cache_hit(connection):
    # Mock the cache key method to return a consistent key
    cache_key = "test_cache_key"
    with patch.object(connection, '_cache_key', return_value=cache_key):
        # Pre-populate the SSH_CONNECTION_CACHE with a mock SSH connection object
        mock_ssh_connection = MagicMock()
        SSH_CONNECTION_CACHE[cache_key] = mock_ssh_connection

        # Call the _connect method which should retrieve the connection from the cache
        connection._connect()

        # Assert that the connection was retrieved from the cache and not created anew
        assert connection.ssh is mock_ssh_connection
        assert connection._connected is True

        # Clean up the SSH_CONNECTION_CACHE to ensure no side effects for other tests
        del SSH_CONNECTION_CACHE[cache_key]

def test_connect_with_cache_miss(connection):
    # Mock the cache key method to return a consistent key
    cache_key = "test_cache_key"
    with patch.object(connection, '_cache_key', return_value=cache_key):
        # Ensure the cache is empty to simulate a cache miss
        SSH_CONNECTION_CACHE.clear()

        # Call the _connect method which should create a new connection
        connection._connect()

        # Assert that the connection was created and added to the cache
        assert connection.ssh is not None
        assert SSH_CONNECTION_CACHE[cache_key] is connection.ssh
        assert connection._connected is True

        # Clean up the SSH_CONNECTION_CACHE to ensure no side effects for other tests
        del SSH_CONNECTION_CACHE[cache_key]
