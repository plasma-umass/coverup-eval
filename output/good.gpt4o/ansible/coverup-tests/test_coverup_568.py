# file lib/ansible/plugins/connection/psrp.py:342-349
# lines [342, 344, 345, 346, 347, 348]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.plugins.connection.psrp import Connection

@pytest.fixture
def mock_play_context():
    mock = MagicMock()
    mock.shell = 'powershell'
    return mock

def test_connection_class_attributes(mock_play_context):
    conn = Connection(mock_play_context, None)
    
    assert conn.transport == 'psrp'
    assert conn.module_implementation_preferences == ('.ps1', '.exe', '')
    assert conn.allow_executable is False
    assert conn.has_pipelining is True
    assert conn.allow_extras is True
