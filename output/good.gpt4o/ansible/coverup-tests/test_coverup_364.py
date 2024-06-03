# file lib/ansible/plugins/connection/psrp.py:413-427
# lines [413, 414, 415, 416, 419, 420, 421, 423, 425, 426, 427]
# branches ['414->415', '414->419']

import pytest
from unittest import mock
from ansible.plugins.connection.psrp import Connection
from ansible.playbook.play_context import PlayContext
from ansible.utils.display import Display

@pytest.fixture
def connection():
    play_context = PlayContext()
    new_stdin = mock.Mock()
    conn = Connection(play_context, new_stdin)
    conn._connected = True
    conn._psrp_host = 'localhost'
    conn.runspace = mock.Mock()
    return conn

def test_reset_not_connected():
    play_context = PlayContext()
    new_stdin = mock.Mock()
    conn = Connection(play_context, new_stdin)
    conn._connected = False
    conn.runspace = mock.Mock()

    conn.reset()

    assert conn.runspace is None

def test_reset_connected(mocker, connection):
    mocker.patch.object(connection, 'close', side_effect=Exception('Connection already closed'))
    mocker.patch.object(Display, 'debug')
    mocker.patch.object(Display, 'vvvvv')
    mocker.patch.object(connection, '_connect')

    connection.reset()

    connection.close.assert_called_once()
    assert connection.runspace is None
    connection._connect.assert_called_once()
    Display.debug.assert_called_once_with(
        "PSRP reset - failed to closed runspace: Connection already closed"
    )
    Display.vvvvv.assert_called_once_with(
        "PSRP: Reset Connection", host='localhost'
    )
