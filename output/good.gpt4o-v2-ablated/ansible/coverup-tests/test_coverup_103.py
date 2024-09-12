# file: lib/ansible/plugins/connection/psrp.py:350-364
# asked: {"lines": [350, 351, 352, 354, 355, 356, 358, 359, 361, 362, 363, 364], "branches": [[361, 0], [361, 362]]}
# gained: {"lines": [350, 351, 352, 354, 355, 356, 358, 359, 361, 362, 363, 364], "branches": [[361, 0], [361, 362]]}

import pytest
import logging
from ansible.plugins.connection.psrp import Connection
from ansible.plugins.connection import ConnectionBase
from ansible import constants as C

@pytest.fixture
def mock_connection_base(mocker):
    mocker.patch.object(ConnectionBase, '__init__', return_value=None)

def test_connection_init_debug_on(mock_connection_base, monkeypatch):
    monkeypatch.setattr(C, 'DEFAULT_DEBUG', True)
    conn = Connection()
    
    assert conn.always_pipeline_modules is True
    assert conn.has_native_async is True
    assert conn.runspace is None
    assert conn.host is None
    assert conn._last_pipeline is False
    assert conn._shell_type == 'powershell'

def test_connection_init_debug_off(mock_connection_base, monkeypatch):
    monkeypatch.setattr(C, 'DEFAULT_DEBUG', False)
    conn = Connection()
    
    assert conn.always_pipeline_modules is True
    assert conn.has_native_async is True
    assert conn.runspace is None
    assert conn.host is None
    assert conn._last_pipeline is False
    assert conn._shell_type == 'powershell'
    
    assert logging.getLogger('pypsrp').level == logging.WARNING
    assert logging.getLogger('requests_credssp').level == logging.INFO
    assert logging.getLogger('urllib3').level == logging.INFO
