# file lib/ansible/plugins/connection/psrp.py:350-364
# lines [362, 363, 364]
# branches ['361->362']

import logging
from unittest.mock import MagicMock
import pytest

# Assuming the Connection class is imported from the correct module
from ansible.plugins.connection.psrp import Connection
from ansible.playbook.play_context import PlayContext

# Test function to cover lines 362-364
def test_connection_init_sets_log_levels(mocker):
    # Mock the constants to force the condition to be True
    mocker.patch('ansible.plugins.connection.psrp.C.DEFAULT_DEBUG', False)

    # Mock the getLogger method to return a mock logger
    mock_logger = mocker.MagicMock()
    mocker.patch('logging.getLogger', return_value=mock_logger)

    # Mock the PlayContext and stdin, which are required by ConnectionBase
    mock_play_context = MagicMock(spec=PlayContext)
    mock_play_context.shell = 'powershell'
    mock_stdin = mocker.MagicMock()

    # Instantiate the Connection object to trigger the __init__ method
    connection = Connection(play_context=mock_play_context, new_stdin=mock_stdin)

    # Assert that the log levels were set correctly
    assert mock_logger.setLevel.call_count == 3
    calls = [mocker.call(logging.WARNING), mocker.call(logging.INFO), mocker.call(logging.INFO)]
    mock_logger.setLevel.assert_has_calls(calls, any_order=True)

    # Clean up by resetting the loggers to their default levels
    logging.getLogger('pypsrp').setLevel(logging.NOTSET)
    logging.getLogger('requests_credssp').setLevel(logging.NOTSET)
    logging.getLogger('urllib3').setLevel(logging.NOTSET)
