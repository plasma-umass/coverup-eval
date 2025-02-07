# file: lib/ansible/plugins/connection/paramiko_ssh.py:235-236
# asked: {"lines": [235, 236], "branches": []}
# gained: {"lines": [235, 236], "branches": []}

import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
from unittest.mock import Mock, patch

@pytest.fixture
def mock_play_context():
    mock = Mock()
    mock.remote_addr = '127.0.0.1'
    mock.remote_user = 'test_user'
    mock.shell = '/bin/sh'
    mock.executable = '/bin/sh'
    return mock

@pytest.fixture
def connection(mock_play_context):
    with patch('ansible.plugins.connection.get_shell_plugin', return_value=Mock()):
        return Connection(mock_play_context, new_stdin=Mock())

def test_cache_key(connection):
    expected_key = "127.0.0.1__test_user__"
    assert connection._cache_key() == expected_key
