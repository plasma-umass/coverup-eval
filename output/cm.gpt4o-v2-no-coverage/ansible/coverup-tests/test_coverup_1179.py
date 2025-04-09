# file: lib/ansible/plugins/connection/paramiko_ssh.py:540-544
# asked: {"lines": [541, 542, 543, 544], "branches": [[541, 542], [541, 543]]}
# gained: {"lines": [541, 542, 543, 544], "branches": [[541, 542], [541, 543]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.paramiko_ssh import Connection

@pytest.fixture
def connection():
    play_context = MagicMock()
    new_stdin = MagicMock()
    with patch('ansible.plugins.connection.get_shell_plugin', return_value=MagicMock()):
        return Connection(play_context, new_stdin)

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
    assert connection._connected is True
