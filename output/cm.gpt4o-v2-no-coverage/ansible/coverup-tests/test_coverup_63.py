# file: lib/ansible/plugins/connection/psrp.py:366-411
# asked: {"lines": [366, 367, 368, 369, 370, 371, 372, 373, 374, 376, 377, 380, 381, 382, 384, 385, 386, 388, 389, 390, 391, 393, 394, 395, 396, 397, 398, 399, 400, 401, 403, 404, 405, 406, 409, 410, 411], "branches": [[367, 368], [367, 370], [376, 377], [376, 411]]}
# gained: {"lines": [366, 367, 368, 369, 370, 371, 372, 373, 374, 376, 377, 380, 381, 382, 384, 385, 386, 388, 389, 390, 391, 393, 394, 395, 396, 397, 398, 399, 400, 401, 403, 404, 405, 406, 409, 410, 411], "branches": [[367, 368], [367, 370], [376, 377]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleConnectionFailure, AnsibleError
from ansible.plugins.connection.psrp import Connection
from pypsrp.exceptions import AuthenticationError, WinRMError
from requests.exceptions import ConnectionError, ConnectTimeout
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def connection():
    play_context = PlayContext()
    play_context.shell = 'powershell'
    conn = Connection(play_context, new_stdin=None)
    conn._psrp_user = "test_user"
    conn._psrp_port = 5986
    conn._psrp_host = "test_host"
    conn._psrp_conn_kwargs = {"server": "test_server"}
    conn._psrp_configuration_name = "test_config"
    conn._psrp_auth = "test_auth"
    return conn

def test_connect_no_pypsrp(connection, monkeypatch):
    monkeypatch.setattr("ansible.plugins.connection.psrp.HAS_PYPSRP", False)
    with pytest.raises(AnsibleError, match="pypsrp or dependencies are not installed"):
        connection._connect()

def test_connect_success(connection, monkeypatch):
    monkeypatch.setattr("ansible.plugins.connection.psrp.HAS_PYPSRP", True)
    monkeypatch.setattr("ansible.plugins.connection.psrp.ConnectionBase._connect", MagicMock())
    monkeypatch.setattr("ansible.plugins.connection.psrp.Connection._build_kwargs", MagicMock())
    monkeypatch.setattr("ansible.plugins.connection.psrp.WSMan", MagicMock())
    monkeypatch.setattr("ansible.plugins.connection.psrp.PSHostUserInterface", MagicMock())
    monkeypatch.setattr("ansible.plugins.connection.psrp.PSHost", MagicMock())
    monkeypatch.setattr("ansible.plugins.connection.psrp.RunspacePool", MagicMock())
    
    connection.runspace = None
    connection._connect()
    
    assert connection._connected
    assert connection._last_pipeline is None

def test_connect_authentication_error(connection, monkeypatch):
    monkeypatch.setattr("ansible.plugins.connection.psrp.HAS_PYPSRP", True)
    monkeypatch.setattr("ansible.plugins.connection.psrp.ConnectionBase._connect", MagicMock())
    monkeypatch.setattr("ansible.plugins.connection.psrp.Connection._build_kwargs", MagicMock())
    mock_runspace = MagicMock()
    mock_runspace.open.side_effect = AuthenticationError("auth error")
    monkeypatch.setattr("ansible.plugins.connection.psrp.RunspacePool", MagicMock(return_value=mock_runspace))
    
    connection.runspace = None
    with pytest.raises(AnsibleConnectionFailure, match="failed to authenticate with the server"):
        connection._connect()

def test_connect_winrm_error(connection, monkeypatch):
    monkeypatch.setattr("ansible.plugins.connection.psrp.HAS_PYPSRP", True)
    monkeypatch.setattr("ansible.plugins.connection.psrp.ConnectionBase._connect", MagicMock())
    monkeypatch.setattr("ansible.plugins.connection.psrp.Connection._build_kwargs", MagicMock())
    mock_runspace = MagicMock()
    mock_runspace.open.side_effect = WinRMError("winrm error")
    monkeypatch.setattr("ansible.plugins.connection.psrp.RunspacePool", MagicMock(return_value=mock_runspace))
    
    connection.runspace = None
    with pytest.raises(AnsibleConnectionFailure, match="psrp connection failure during runspace open"):
        connection._connect()

def test_connect_connection_error(connection, monkeypatch):
    monkeypatch.setattr("ansible.plugins.connection.psrp.HAS_PYPSRP", True)
    monkeypatch.setattr("ansible.plugins.connection.psrp.ConnectionBase._connect", MagicMock())
    monkeypatch.setattr("ansible.plugins.connection.psrp.Connection._build_kwargs", MagicMock())
    mock_runspace = MagicMock()
    mock_runspace.open.side_effect = ConnectionError("connection error")
    monkeypatch.setattr("ansible.plugins.connection.psrp.RunspacePool", MagicMock(return_value=mock_runspace))
    
    connection.runspace = None
    with pytest.raises(AnsibleConnectionFailure, match="Failed to connect to the host via PSRP"):
        connection._connect()

def test_connect_connect_timeout(connection, monkeypatch):
    monkeypatch.setattr("ansible.plugins.connection.psrp.HAS_PYPSRP", True)
    monkeypatch.setattr("ansible.plugins.connection.psrp.ConnectionBase._connect", MagicMock())
    monkeypatch.setattr("ansible.plugins.connection.psrp.Connection._build_kwargs", MagicMock())
    mock_runspace = MagicMock()
    mock_runspace.open.side_effect = ConnectTimeout("timeout error")
    monkeypatch.setattr("ansible.plugins.connection.psrp.RunspacePool", MagicMock(return_value=mock_runspace))
    
    connection.runspace = None
    with pytest.raises(AnsibleConnectionFailure, match="Failed to connect to the host via PSRP"):
        connection._connect()
