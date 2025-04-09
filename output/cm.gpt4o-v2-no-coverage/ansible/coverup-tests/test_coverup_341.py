# file: lib/ansible/plugins/connection/psrp.py:350-364
# asked: {"lines": [350, 351, 352, 354, 355, 356, 358, 359, 361, 362, 363, 364], "branches": [[361, 0], [361, 362]]}
# gained: {"lines": [350, 351, 352, 354, 355, 356, 358, 359, 361, 362, 363, 364], "branches": [[361, 0], [361, 362]]}

import pytest
import logging
from ansible.plugins.connection.psrp import Connection
from ansible import constants as C
from unittest.mock import patch

@pytest.fixture
def mock_connection_base_init(mocker):
    return mocker.patch('ansible.plugins.connection.ConnectionBase.__init__', return_value=None)

def test_connection_init_debug_enabled(mock_connection_base_init, mocker):
    mocker.patch('ansible.constants.DEFAULT_DEBUG', True)
    with patch.object(logging.getLogger('pypsrp'), 'setLevel') as mock_pypsrp_setLevel, \
         patch.object(logging.getLogger('requests_credssp'), 'setLevel') as mock_requests_credssp_setLevel, \
         patch.object(logging.getLogger('urllib3'), 'setLevel') as mock_urllib3_setLevel:
        
        conn = Connection()
        
        mock_connection_base_init.assert_called_once()
        mock_pypsrp_setLevel.assert_not_called()
        mock_requests_credssp_setLevel.assert_not_called()
        mock_urllib3_setLevel.assert_not_called()
        
        assert conn.always_pipeline_modules is True
        assert conn.has_native_async is True
        assert conn.runspace is None
        assert conn.host is None
        assert conn._last_pipeline is False
        assert conn._shell_type == 'powershell'

def test_connection_init_debug_disabled(mock_connection_base_init, mocker):
    mocker.patch('ansible.constants.DEFAULT_DEBUG', False)
    with patch.object(logging.getLogger('pypsrp'), 'setLevel') as mock_pypsrp_setLevel, \
         patch.object(logging.getLogger('requests_credssp'), 'setLevel') as mock_requests_credssp_setLevel, \
         patch.object(logging.getLogger('urllib3'), 'setLevel') as mock_urllib3_setLevel:
        
        conn = Connection()
        
        mock_connection_base_init.assert_called_once()
        mock_pypsrp_setLevel.assert_called_once_with(logging.WARNING)
        mock_requests_credssp_setLevel.assert_called_once_with(logging.INFO)
        mock_urllib3_setLevel.assert_called_once_with(logging.INFO)
        
        assert conn.always_pipeline_modules is True
        assert conn.has_native_async is True
        assert conn.runspace is None
        assert conn.host is None
        assert conn._last_pipeline is False
        assert conn._shell_type == 'powershell'
