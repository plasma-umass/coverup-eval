# file: lib/ansible/plugins/connection/paramiko_ssh.py:540-544
# asked: {"lines": [540, 541, 542, 543, 544], "branches": [[541, 542], [541, 543]]}
# gained: {"lines": [540, 541, 542, 543, 544], "branches": [[541, 542], [541, 543]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.paramiko_ssh import Connection

@pytest.fixture
def connection():
    play_context = MagicMock()
    play_context.shell = '/bin/sh'
    play_context.executable = '/bin/sh'
    new_stdin = MagicMock()
    with patch('ansible.plugins.connection.get_shell_plugin', return_value=MagicMock()):
        conn = Connection(play_context, new_stdin)
    return conn

def test_reset_not_connected(connection):
    connection._connected = False
    connection.close = MagicMock()
    connection._connect = MagicMock()

    connection.reset()

    connection.close.assert_not_called()
    connection._connect.assert_not_called()

def test_reset_connected(connection):
    connection._connected = True
    connection.close = MagicMock()
    connection._connect = MagicMock()

    connection.reset()

    connection.close.assert_called_once()
    connection._connect.assert_called_once()
