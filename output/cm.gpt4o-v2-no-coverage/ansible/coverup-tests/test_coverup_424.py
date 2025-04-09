# file: lib/ansible/plugins/connection/psrp.py:413-427
# asked: {"lines": [413, 414, 415, 416, 419, 420, 421, 423, 425, 426, 427], "branches": [[414, 415], [414, 419]]}
# gained: {"lines": [413, 414, 415, 416, 419, 420, 421, 423, 425, 426, 427], "branches": [[414, 415], [414, 419]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.psrp import Connection
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def connection(mocker):
    play_context = PlayContext()
    play_context.shell = 'sh'
    play_context.executable = '/bin/sh'
    mocker.patch('ansible.plugins.loader.shell_loader.get', return_value=MagicMock())
    conn = Connection(play_context, None)
    conn._connected = False
    conn.runspace = "initial_runspace"
    conn._psrp_host = "test_host"
    return conn

def test_reset_not_connected(connection):
    connection.reset()
    assert connection.runspace is None

def test_reset_connected(connection, mocker):
    connection._connected = True
    mock_close = mocker.patch.object(connection, 'close', side_effect=Exception("close error"))
    mock_connect = mocker.patch.object(connection, '_connect')
    mock_debug = mocker.patch('ansible.plugins.connection.psrp.display.debug')
    mock_vvvvv = mocker.patch('ansible.plugins.connection.psrp.display.vvvvv')

    connection.reset()

    mock_close.assert_called_once()
    mock_debug.assert_called_once_with("PSRP reset - failed to closed runspace: close error")
    mock_vvvvv.assert_called_once_with("PSRP: Reset Connection", host="test_host")
    assert connection.runspace is None
    mock_connect.assert_called_once()
