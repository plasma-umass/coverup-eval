# file lib/ansible/plugins/connection/paramiko_ssh.py:540-544
# lines [541, 542, 543, 544]
# branches ['541->542', '541->543']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the Connection class is imported from ansible.plugins.connection.paramiko_ssh
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext
from ansible.errors import AnsibleError

@pytest.fixture
def connection():
    play_context = MagicMock(spec=PlayContext)
    play_context.shell = 'sh'
    play_context.executable = '/bin/sh'
    new_stdin = MagicMock()
    conn = Connection(play_context, new_stdin)
    conn._connected = True
    conn.close = MagicMock()
    conn._connect = MagicMock()
    return conn

def test_reset_not_connected():
    play_context = MagicMock(spec=PlayContext)
    play_context.shell = 'sh'
    play_context.executable = '/bin/sh'
    new_stdin = MagicMock()
    conn = Connection(play_context, new_stdin)
    conn._connected = False
    conn.close = MagicMock()
    conn._connect = MagicMock()
    
    conn.reset()
    
    conn.close.assert_not_called()
    conn._connect.assert_not_called()

def test_reset_connected(connection):
    connection.reset()
    
    connection.close.assert_called_once()
    connection._connect.assert_called_once()
