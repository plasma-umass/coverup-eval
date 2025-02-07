# file: lib/ansible/plugins/connection/psrp.py:366-411
# asked: {"lines": [367, 368, 369, 370, 371, 372, 373, 374, 376, 377, 380, 381, 382, 384, 385, 386, 388, 389, 390, 391, 393, 394, 395, 396, 397, 398, 399, 400, 401, 403, 404, 405, 406, 409, 410, 411], "branches": [[367, 368], [367, 370], [376, 377], [376, 411]]}
# gained: {"lines": [367, 368, 369, 370, 371, 372, 373, 374, 376, 377, 380, 381, 382, 384, 385, 386, 388, 389, 390, 391, 393, 394, 395, 396, 397, 398, 399, 400, 401, 403, 404, 405, 406, 409, 410, 411], "branches": [[367, 368], [367, 370], [376, 377]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.connection.psrp import Connection
from ansible.errors import AnsibleConnectionFailure, AnsibleError
from pypsrp.exceptions import AuthenticationError, WinRMError
from requests.exceptions import ConnectionError, ConnectTimeout
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def connection():
    play_context = PlayContext()
    return Connection(play_context, new_stdin=None)

def test_connect_no_pypsrp(connection, monkeypatch):
    monkeypatch.setattr('ansible.plugins.connection.psrp.HAS_PYPSRP', False)
    with pytest.raises(AnsibleError, match="pypsrp or dependencies are not installed"):
        connection._connect()

def test_connect_success(connection, monkeypatch):
    monkeypatch.setattr('ansible.plugins.connection.psrp.HAS_PYPSRP', True)
    monkeypatch.setattr('ansible.plugins.connection.psrp.Connection._build_kwargs', lambda x: None)
    monkeypatch.setattr('ansible.plugins.connection.psrp.WSMan', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.PSHostUserInterface', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.PSHost', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.RunspacePool', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.RunspacePool.open', lambda x: None)
    
    connection._psrp_conn_kwargs = {}
    connection._psrp_user = 'user'
    connection._psrp_port = 5986
    connection._psrp_host = 'host'
    connection._psrp_configuration_name = 'config'
    connection._psrp_auth = 'auth'
    
    connection._connect()
    
    assert connection._connected
    assert connection._last_pipeline is None

def test_connect_authentication_error(connection, monkeypatch):
    monkeypatch.setattr('ansible.plugins.connection.psrp.HAS_PYPSRP', True)
    monkeypatch.setattr('ansible.plugins.connection.psrp.Connection._build_kwargs', lambda x: None)
    monkeypatch.setattr('ansible.plugins.connection.psrp.WSMan', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.PSHostUserInterface', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.PSHost', MagicMock())
    runspace_pool_mock = MagicMock()
    runspace_pool_mock.open.side_effect = AuthenticationError("auth error")
    monkeypatch.setattr('ansible.plugins.connection.psrp.RunspacePool', lambda *args, **kwargs: runspace_pool_mock)
    
    connection._psrp_conn_kwargs = {}
    connection._psrp_user = 'user'
    connection._psrp_port = 5986
    connection._psrp_host = 'host'
    connection._psrp_configuration_name = 'config'
    connection._psrp_auth = 'auth'
    
    with pytest.raises(AnsibleConnectionFailure, match="failed to authenticate with the server"):
        connection._connect()

def test_connect_winrm_error(connection, monkeypatch):
    monkeypatch.setattr('ansible.plugins.connection.psrp.HAS_PYPSRP', True)
    monkeypatch.setattr('ansible.plugins.connection.psrp.Connection._build_kwargs', lambda x: None)
    monkeypatch.setattr('ansible.plugins.connection.psrp.WSMan', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.PSHostUserInterface', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.PSHost', MagicMock())
    runspace_pool_mock = MagicMock()
    runspace_pool_mock.open.side_effect = WinRMError("winrm error")
    monkeypatch.setattr('ansible.plugins.connection.psrp.RunspacePool', lambda *args, **kwargs: runspace_pool_mock)
    
    connection._psrp_conn_kwargs = {}
    connection._psrp_user = 'user'
    connection._psrp_port = 5986
    connection._psrp_host = 'host'
    connection._psrp_configuration_name = 'config'
    connection._psrp_auth = 'auth'
    
    with pytest.raises(AnsibleConnectionFailure, match="psrp connection failure during runspace open"):
        connection._connect()

def test_connect_connection_error(connection, monkeypatch):
    monkeypatch.setattr('ansible.plugins.connection.psrp.HAS_PYPSRP', True)
    monkeypatch.setattr('ansible.plugins.connection.psrp.Connection._build_kwargs', lambda x: None)
    monkeypatch.setattr('ansible.plugins.connection.psrp.WSMan', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.PSHostUserInterface', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.PSHost', MagicMock())
    runspace_pool_mock = MagicMock()
    runspace_pool_mock.open.side_effect = ConnectionError("connection error")
    monkeypatch.setattr('ansible.plugins.connection.psrp.RunspacePool', lambda *args, **kwargs: runspace_pool_mock)
    
    connection._psrp_conn_kwargs = {}
    connection._psrp_user = 'user'
    connection._psrp_port = 5986
    connection._psrp_host = 'host'
    connection._psrp_configuration_name = 'config'
    connection._psrp_auth = 'auth'
    
    with pytest.raises(AnsibleConnectionFailure, match="Failed to connect to the host via PSRP"):
        connection._connect()

def test_connect_timeout_error(connection, monkeypatch):
    monkeypatch.setattr('ansible.plugins.connection.psrp.HAS_PYPSRP', True)
    monkeypatch.setattr('ansible.plugins.connection.psrp.Connection._build_kwargs', lambda x: None)
    monkeypatch.setattr('ansible.plugins.connection.psrp.WSMan', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.PSHostUserInterface', MagicMock())
    monkeypatch.setattr('ansible.plugins.connection.psrp.PSHost', MagicMock())
    runspace_pool_mock = MagicMock()
    runspace_pool_mock.open.side_effect = ConnectTimeout("timeout error")
    monkeypatch.setattr('ansible.plugins.connection.psrp.RunspacePool', lambda *args, **kwargs: runspace_pool_mock)
    
    connection._psrp_conn_kwargs = {}
    connection._psrp_user = 'user'
    connection._psrp_port = 5986
    connection._psrp_host = 'host'
    connection._psrp_configuration_name = 'config'
    connection._psrp_auth = 'auth'
    
    with pytest.raises(AnsibleConnectionFailure, match="Failed to connect to the host via PSRP"):
        connection._connect()
