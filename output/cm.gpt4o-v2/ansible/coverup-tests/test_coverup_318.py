# file: lib/ansible/plugins/connection/psrp.py:413-427
# asked: {"lines": [413, 414, 415, 416, 419, 420, 421, 423, 425, 426, 427], "branches": [[414, 415], [414, 419]]}
# gained: {"lines": [413, 414, 415, 416, 419, 420, 421, 423, 425, 426, 427], "branches": [[414, 415], [414, 419]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.connection.psrp import Connection

@pytest.fixture
def connection():
    play_context = MagicMock()
    play_context.shell = 'sh'
    play_context.executable = '/bin/sh'
    conn = Connection(play_context=play_context, new_stdin=MagicMock())
    conn._connected = True
    conn._psrp_host = 'localhost'
    return conn

def test_reset_not_connected(connection):
    connection._connected = False
    connection.reset()
    assert connection.runspace is None

@patch('ansible.plugins.connection.psrp.display')
def test_reset_connected(mock_display, connection):
    connection.close = MagicMock()
    connection._connect = MagicMock()

    connection.reset()

    connection.close.assert_called_once()
    mock_display.vvvvv.assert_called_once_with('PSRP: Reset Connection', host='localhost')
    assert connection.runspace is None
    connection._connect.assert_called_once()

@patch('ansible.plugins.connection.psrp.display')
def test_reset_connected_with_exception(mock_display, connection):
    connection.close = MagicMock(side_effect=Exception('Test Exception'))
    connection._connect = MagicMock()

    connection.reset()

    connection.close.assert_called_once()
    mock_display.debug.assert_called_once_with('PSRP reset - failed to closed runspace: Test Exception')
    mock_display.vvvvv.assert_called_once_with('PSRP: Reset Connection', host='localhost')
    assert connection.runspace is None
    connection._connect.assert_called_once()
