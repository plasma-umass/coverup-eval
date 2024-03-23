# file lib/ansible/plugins/connection/psrp.py:413-427
# lines [414, 415, 416, 419, 420, 421, 423, 425, 426, 427]
# branches ['414->415', '414->419']

import pytest
from ansible.plugins.connection.psrp import Connection
from ansible.utils.display import Display
from unittest.mock import MagicMock, patch
from ansible.playbook.play_context import PlayContext

# Mock the Display class to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'debug')
    mocker.patch.object(Display, 'vvvvv')

@pytest.fixture
def psrp_connection(mocker):
    # Create a mock PSRP connection object with the required arguments
    play_context = PlayContext()
    new_stdin = MagicMock()
    connection = Connection(play_context, new_stdin)
    connection._connected = True
    connection._psrp_host = 'fake_host'
    connection.runspace = MagicMock()
    connection.close = MagicMock()
    connection._connect = MagicMock()
    return connection

def test_reset_connection_when_connected(mock_display, psrp_connection):
    # Simulate an exception when closing the runspace
    psrp_connection.close.side_effect = Exception("Runspace close error")

    # Call the reset method which should handle the exception
    psrp_connection.reset()

    # Assert that the close method was called
    psrp_connection.close.assert_called_once()

    # Assert that the debug method was called with the expected message
    Display.debug.assert_called_with("PSRP reset - failed to closed runspace: Runspace close error")

    # Assert that the verbose method was called with the expected message
    Display.vvvvv.assert_called_with("PSRP: Reset Connection", host='fake_host')

    # Assert that the runspace was set to None
    assert psrp_connection.runspace is None

    # Assert that the _connect method was called
    psrp_connection._connect.assert_called_once()

    # Cleanup
    psrp_connection.close.side_effect = None
