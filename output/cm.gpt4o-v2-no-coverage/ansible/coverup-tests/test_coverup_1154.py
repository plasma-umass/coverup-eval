# file: lib/ansible/plugins/connection/psrp.py:768-775
# asked: {"lines": [769, 770, 771, 772, 773, 774, 775], "branches": [[769, 770], [769, 773]]}
# gained: {"lines": [769, 770, 771, 772, 773, 774, 775], "branches": [[769, 770], [769, 773]]}

import pytest
from unittest.mock import Mock, patch
from ansible.plugins.connection.psrp import Connection
from ansible.playbook.play_context import PlayContext
from pypsrp.complex_objects import RunspacePoolState

@pytest.fixture
def connection():
    play_context = PlayContext()
    return Connection(play_context, new_stdin=None)

def test_close_with_opened_runspace(connection, mocker):
    mock_runspace = Mock()
    mock_runspace.state = RunspacePoolState.OPENED
    mock_runspace.id = "test_id"
    connection.runspace = mock_runspace
    connection._psrp_host = "test_host"
    mock_display = mocker.patch("ansible.plugins.connection.psrp.display.vvvvv")
    
    connection.close()
    
    mock_display.assert_called_once_with("PSRP CLOSE RUNSPACE: test_id", host="test_host")
    mock_runspace.close.assert_called_once()
    assert connection.runspace is None
    assert connection._connected is False
    assert connection._last_pipeline is None

def test_close_with_non_opened_runspace(connection):
    mock_runspace = Mock()
    mock_runspace.state = RunspacePoolState.CLOSED
    connection.runspace = mock_runspace
    
    connection.close()
    
    assert connection.runspace is None
    assert connection._connected is False
    assert connection._last_pipeline is None

def test_close_with_no_runspace(connection):
    connection.runspace = None
    
    connection.close()
    
    assert connection.runspace is None
    assert connection._connected is False
    assert connection._last_pipeline is None
