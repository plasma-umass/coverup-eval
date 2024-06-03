# file lib/ansible/plugins/connection/paramiko_ssh.py:238-246
# lines [238, 239, 240, 241, 243, 245, 246]
# branches ['240->241', '240->243']

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection, SSH_CONNECTION_CACHE
from ansible.playbook.play_context import PlayContext
from ansible.errors import AnsibleError

@pytest.fixture
def mock_cache_key(mocker):
    return mocker.patch('ansible.plugins.connection.paramiko_ssh.Connection._cache_key', return_value='test_key')

@pytest.fixture
def mock_connect_uncached(mocker):
    return mocker.patch('ansible.plugins.connection.paramiko_ssh.Connection._connect_uncached', return_value='mock_ssh_connection')

@pytest.fixture
def play_context():
    context = MagicMock(spec=PlayContext)
    context.shell = 'sh'
    context.executable = '/bin/sh'
    return context

@pytest.fixture
def new_stdin():
    return MagicMock()

def test_connect_with_cache(mock_cache_key, mock_connect_uncached, play_context, new_stdin):
    conn = Connection(play_context, new_stdin)
    SSH_CONNECTION_CACHE['test_key'] = 'cached_ssh_connection'
    
    conn._connect()
    
    assert conn.ssh == 'cached_ssh_connection'
    assert conn._connected is True

def test_connect_without_cache(mock_cache_key, mock_connect_uncached, play_context, new_stdin):
    conn = Connection(play_context, new_stdin)
    
    conn._connect()
    
    assert conn.ssh == 'mock_ssh_connection'
    assert conn._connected is True
    assert SSH_CONNECTION_CACHE['test_key'] == 'mock_ssh_connection'

@pytest.fixture(autouse=True)
def clear_cache():
    yield
    SSH_CONNECTION_CACHE.clear()
