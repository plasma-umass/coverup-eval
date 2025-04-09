# file lib/ansible/plugins/connection/paramiko_ssh.py:235-236
# lines [236]
# branches []

import pytest
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext
from ansible.plugins.loader import shell_loader

@pytest.fixture
def mock_play_context(mocker):
    play_context = mocker.Mock(spec=PlayContext)
    play_context.remote_addr = '127.0.0.1'
    play_context.remote_user = 'test_user'
    play_context.shell = 'sh'
    return play_context

@pytest.fixture
def mock_shell_loader(mocker):
    mocker.patch.object(shell_loader, 'get', return_value=mocker.Mock())

def test_cache_key(mock_play_context, mock_shell_loader):
    connection = Connection(play_context=mock_play_context, new_stdin=None)
    cache_key = connection._cache_key()
    assert cache_key == "127.0.0.1__test_user__"
