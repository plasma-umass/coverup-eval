# file lib/ansible/plugins/connection/psrp.py:350-364
# lines [350, 351, 352, 354, 355, 356, 358, 359, 361, 362, 363, 364]
# branches ['361->exit', '361->362']

import pytest
import logging
from ansible.plugins.connection.psrp import Connection
from ansible import constants as C
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def mock_logging(mocker):
    mocker.patch('logging.getLogger')

def test_connection_initialization(mock_logging):
    # Mocking the arguments for Connection initialization
    play_context = PlayContext()
    new_stdin = None
    args = (play_context, new_stdin)
    kwargs = {}

    # Set C.DEFAULT_DEBUG to False to test the logging level settings
    original_debug = C.DEFAULT_DEBUG
    C.DEFAULT_DEBUG = False

    try:
        conn = Connection(*args, **kwargs)

        # Assertions to verify the initialization
        assert conn.always_pipeline_modules is True
        assert conn.has_native_async is True
        assert conn.runspace is None
        assert conn.host is None
        assert conn._last_pipeline is False
        assert conn._shell_type == 'powershell'

        # Verify that logging levels are set correctly
        logging.getLogger('pypsrp').setLevel.assert_any_call(logging.WARNING)
        logging.getLogger('requests_credssp').setLevel.assert_any_call(logging.INFO)
        logging.getLogger('urllib3').setLevel.assert_any_call(logging.INFO)
    finally:
        # Restore the original value of C.DEFAULT_DEBUG
        C.DEFAULT_DEBUG = original_debug
