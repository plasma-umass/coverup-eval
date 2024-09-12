# file: lib/ansible/plugins/connection/psrp.py:350-364
# asked: {"lines": [350, 351, 352, 354, 355, 356, 358, 359, 361, 362, 363, 364], "branches": [[361, 0], [361, 362]]}
# gained: {"lines": [350, 351, 352, 354, 355, 356, 358, 359, 361, 362, 363, 364], "branches": [[361, 362]]}

import pytest
import logging
from ansible.plugins.connection.psrp import Connection
from ansible import constants as C

@pytest.fixture
def connection_instance(mocker):
    mocker.patch('ansible.plugins.connection.ConnectionBase.__init__', return_value=None)
    return Connection()

def test_connection_init_defaults(connection_instance):
    assert connection_instance.always_pipeline_modules is True
    assert connection_instance.has_native_async is True
    assert connection_instance.runspace is None
    assert connection_instance.host is None
    assert connection_instance._last_pipeline is False
    assert connection_instance._shell_type == 'powershell'

def test_connection_logging_levels(mocker):
    mocker.patch('ansible.plugins.connection.ConnectionBase.__init__', return_value=None)
    mocker.patch.object(C, 'DEFAULT_DEBUG', False)
    
    connection_instance = Connection()
    
    assert logging.getLogger('pypsrp').level == logging.WARNING
    assert logging.getLogger('requests_credssp').level == logging.INFO
    assert logging.getLogger('urllib3').level == logging.INFO
