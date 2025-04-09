# file: lib/ansible/plugins/connection/psrp.py:413-427
# asked: {"lines": [414, 415, 416, 419, 420, 421, 423, 425, 426, 427], "branches": [[414, 415], [414, 419]]}
# gained: {"lines": [414, 415, 416, 419, 420, 421, 423, 425, 426, 427], "branches": [[414, 415], [414, 419]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the Connection class is imported from ansible.plugins.connection.psrp
from ansible.plugins.connection.psrp import Connection
from ansible.playbook.play_context import PlayContext
from ansible.errors import AnsibleError

@pytest.fixture
def connection(mocker):
    play_context = MagicMock(spec=PlayContext)
    play_context.shell = 'sh'
    play_context.executable = '/bin/sh'
    new_stdin = MagicMock()
    conn = Connection(play_context, new_stdin)
    conn._connected = False
    conn.runspace = MagicMock()
    conn._psrp_host = "test_host"
    return conn

def test_reset_not_connected(connection):
    connection.reset()
    assert connection.runspace is None

def test_reset_connected(connection, mocker):
    connection._connected = True
    mock_close = mocker.patch.object(connection, 'close', side_effect=None)
    mock_connect = mocker.patch.object(connection, '_connect', side_effect=None)
    mock_display_vvvvv = mocker.patch('ansible.plugins.connection.psrp.display.vvvvv')
    
    connection.reset()
    
    mock_close.assert_called_once()
    mock_display_vvvvv.assert_called_once_with("PSRP: Reset Connection", host="test_host")
    assert connection.runspace is None
    mock_connect.assert_called_once()

def test_reset_connected_with_exception(connection, mocker):
    connection._connected = True
    mock_close = mocker.patch.object(connection, 'close', side_effect=Exception("close error"))
    mock_connect = mocker.patch.object(connection, '_connect', side_effect=None)
    mock_display_debug = mocker.patch('ansible.plugins.connection.psrp.display.debug')
    mock_display_vvvvv = mocker.patch('ansible.plugins.connection.psrp.display.vvvvv')
    
    connection.reset()
    
    mock_close.assert_called_once()
    mock_display_debug.assert_called_once_with("PSRP reset - failed to closed runspace: close error")
    mock_display_vvvvv.assert_called_once_with("PSRP: Reset Connection", host="test_host")
    assert connection.runspace is None
    mock_connect.assert_called_once()
