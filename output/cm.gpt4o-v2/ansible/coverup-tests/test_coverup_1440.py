# file: lib/ansible/plugins/connection/psrp.py:366-411
# asked: {"lines": [], "branches": [[376, 411]]}
# gained: {"lines": [], "branches": [[376, 411]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.connection.psrp import Connection
from ansible.errors import AnsibleConnectionFailure
from pypsrp.exceptions import AuthenticationError, WinRMError
from requests.exceptions import ConnectionError, ConnectTimeout
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def connection():
    play_context = PlayContext()
    play_context.shell = 'powershell'
    conn = Connection(play_context, new_stdin=None)
    conn._psrp_conn_kwargs = {}
    conn._psrp_user = "user"
    conn._psrp_port = 5986
    conn._psrp_host = "host"
    conn._psrp_auth = "auth"
    conn._psrp_configuration_name = "configuration"
    return conn

def test_connect_no_runspace(connection):
    with patch("ansible.plugins.connection.psrp.WSMan") as MockWSMan, \
         patch("ansible.plugins.connection.psrp.PSHostUserInterface") as MockPSHostUserInterface, \
         patch("ansible.plugins.connection.psrp.PSHost") as MockPSHost, \
         patch("ansible.plugins.connection.psrp.RunspacePool") as MockRunspacePool, \
         patch.object(connection, "_build_kwargs"), \
         patch("ansible.plugins.connection.psrp.display.vvv"), \
         patch("ansible.plugins.connection.psrp.display.vvvvv"):
        
        mock_runspace = MockRunspacePool.return_value
        connection.runspace = None

        connection._connect()

        MockWSMan.assert_called_once_with(**connection._psrp_conn_kwargs)
        MockPSHostUserInterface.assert_called_once()
        MockPSHost.assert_called_once_with(None, None, False, "Ansible PSRP Host", None, MockPSHostUserInterface.return_value, None)
        MockRunspacePool.assert_called_once_with(MockWSMan.return_value, host=MockPSHost.return_value, configuration_name=connection._psrp_configuration_name)
        mock_runspace.open.assert_called_once()
        assert connection._connected
        assert connection._last_pipeline is None

def test_connect_with_runspace(connection):
    with patch("ansible.plugins.connection.psrp.WSMan") as MockWSMan, \
         patch("ansible.plugins.connection.psrp.PSHostUserInterface") as MockPSHostUserInterface, \
         patch("ansible.plugins.connection.psrp.PSHost"), \
         patch("ansible.plugins.connection.psrp.RunspacePool"), \
         patch.object(connection, "_build_kwargs"), \
         patch("ansible.plugins.connection.psrp.display.vvv"), \
         patch("ansible.plugins.connection.psrp.display.vvvvv"):
        
        connection.runspace = MagicMock()

        connection._connect()

        MockWSMan.assert_not_called()
        MockPSHostUserInterface.assert_not_called()
        assert connection._connected is False

def test_connect_authentication_error(connection):
    with patch("ansible.plugins.connection.psrp.WSMan"), \
         patch("ansible.plugins.connection.psrp.PSHostUserInterface"), \
         patch("ansible.plugins.connection.psrp.PSHost"), \
         patch("ansible.plugins.connection.psrp.RunspacePool") as MockRunspacePool, \
         patch.object(connection, "_build_kwargs"), \
         patch("ansible.plugins.connection.psrp.display.vvv"), \
         patch("ansible.plugins.connection.psrp.display.vvvvv"):
        
        mock_runspace = MockRunspacePool.return_value
        mock_runspace.open.side_effect = AuthenticationError("auth error")
        connection.runspace = None

        with pytest.raises(AnsibleConnectionFailure, match="failed to authenticate with the server: auth error"):
            connection._connect()

def test_connect_winrm_error(connection):
    with patch("ansible.plugins.connection.psrp.WSMan"), \
         patch("ansible.plugins.connection.psrp.PSHostUserInterface"), \
         patch("ansible.plugins.connection.psrp.PSHost"), \
         patch("ansible.plugins.connection.psrp.RunspacePool") as MockRunspacePool, \
         patch.object(connection, "_build_kwargs"), \
         patch("ansible.plugins.connection.psrp.display.vvv"), \
         patch("ansible.plugins.connection.psrp.display.vvvvv"):
        
        mock_runspace = MockRunspacePool.return_value
        mock_runspace.open.side_effect = WinRMError("winrm error")
        connection.runspace = None

        with pytest.raises(AnsibleConnectionFailure, match="psrp connection failure during runspace open: winrm error"):
            connection._connect()

def test_connect_connection_error(connection):
    with patch("ansible.plugins.connection.psrp.WSMan"), \
         patch("ansible.plugins.connection.psrp.PSHostUserInterface"), \
         patch("ansible.plugins.connection.psrp.PSHost"), \
         patch("ansible.plugins.connection.psrp.RunspacePool") as MockRunspacePool, \
         patch.object(connection, "_build_kwargs"), \
         patch("ansible.plugins.connection.psrp.display.vvv"), \
         patch("ansible.plugins.connection.psrp.display.vvvvv"):
        
        mock_runspace = MockRunspacePool.return_value
        mock_runspace.open.side_effect = ConnectionError("connection error")
        connection.runspace = None

        with pytest.raises(AnsibleConnectionFailure, match="Failed to connect to the host via PSRP: connection error"):
            connection._connect()

def test_connect_connect_timeout(connection):
    with patch("ansible.plugins.connection.psrp.WSMan"), \
         patch("ansible.plugins.connection.psrp.PSHostUserInterface"), \
         patch("ansible.plugins.connection.psrp.PSHost"), \
         patch("ansible.plugins.connection.psrp.RunspacePool") as MockRunspacePool, \
         patch.object(connection, "_build_kwargs"), \
         patch("ansible.plugins.connection.psrp.display.vvv"), \
         patch("ansible.plugins.connection.psrp.display.vvvvv"):
        
        mock_runspace = MockRunspacePool.return_value
        mock_runspace.open.side_effect = ConnectTimeout("timeout error")
        connection.runspace = None

        with pytest.raises(AnsibleConnectionFailure, match="Failed to connect to the host via PSRP: timeout error"):
            connection._connect()
