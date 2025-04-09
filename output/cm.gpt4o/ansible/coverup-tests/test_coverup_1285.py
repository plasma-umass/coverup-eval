# file lib/ansible/plugins/connection/paramiko_ssh.py:510-538
# lines [517]
# branches ['516->517']

import pytest
import os
from unittest import mock
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def connection():
    play_context = PlayContext()
    new_stdin = mock.Mock()
    conn = Connection(play_context, new_stdin)
    conn.ssh = mock.Mock()
    conn.ssh._host_keys = {}
    return conn

def test_save_ssh_host_keys_no_keys_added(connection, mocker):
    mocker.patch.object(connection, '_any_keys_added', return_value=False)
    filename = '/tmp/test_ssh_host_keys'
    
    result = connection._save_ssh_host_keys(filename)
    
    assert result is False
    assert not os.path.exists(filename)
