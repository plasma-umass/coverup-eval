# file: lib/ansible/plugins/connection/psrp.py:350-364
# asked: {"lines": [350, 351, 352, 354, 355, 356, 358, 359, 361, 362, 363, 364], "branches": [[361, 0], [361, 362]]}
# gained: {"lines": [350, 351, 352, 354, 355, 356, 358, 359, 361, 362, 363, 364], "branches": [[361, 362]]}

import pytest
import logging
from ansible.plugins.connection.psrp import Connection
from ansible.plugins.connection import ConnectionBase
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def mock_default_debug(monkeypatch):
    class MockC:
        DEFAULT_DEBUG = False
    monkeypatch.setattr('ansible.plugins.connection.psrp.C', MockC)

@pytest.fixture
def mock_play_context():
    return PlayContext()

@pytest.fixture
def mock_new_stdin():
    return None

def test_connection_init(mock_default_debug, mock_play_context, mock_new_stdin):
    conn = Connection(play_context=mock_play_context, new_stdin=mock_new_stdin)
    
    assert conn.always_pipeline_modules is True
    assert conn.has_native_async is True
    assert conn.runspace is None
    assert conn.host is None
    assert conn._last_pipeline is False
    assert conn._shell_type == 'powershell'
    
    pypsrp_logger = logging.getLogger('pypsrp')
    requests_credssp_logger = logging.getLogger('requests_credssp')
    urllib3_logger = logging.getLogger('urllib3')
    
    assert pypsrp_logger.level == logging.WARNING
    assert requests_credssp_logger.level == logging.INFO
    assert urllib3_logger.level == logging.INFO
