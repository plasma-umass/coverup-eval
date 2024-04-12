# file lib/ansible/plugins/connection/paramiko_ssh.py:235-236
# lines [235, 236]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext

# Mocking the PlayContext to provide remote_addr and remote_user
@pytest.fixture
def mock_play_context():
    mock_context = MagicMock(spec=PlayContext)
    mock_context.remote_addr = '127.0.0.1'
    mock_context.remote_user = 'testuser'
    return mock_context

# Test function to check if _cache_key method generates the correct key
def test_cache_key(mock_play_context):
    connection = Connection(mock_play_context, MagicMock(), MagicMock())
    expected_cache_key = "127.0.0.1__testuser__"
    assert connection._cache_key() == expected_cache_key
