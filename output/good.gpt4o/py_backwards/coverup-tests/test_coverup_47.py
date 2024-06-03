# file py_backwards/utils/helpers.py:43-45
# lines [44, 45]
# branches ['44->exit', '44->45']

import pytest
import sys
from unittest.mock import Mock, patch
from py_backwards.utils.helpers import debug

def test_debug_prints_message(mocker):
    mock_get_message = Mock(return_value="Test message")
    mock_print = mocker.patch("builtins.print")
    mock_settings = mocker.patch("py_backwards.utils.helpers.settings")
    mock_messages = mocker.patch("py_backwards.utils.helpers.messages")

    mock_settings.debug = True
    mock_messages.debug = lambda msg: f"DEBUG: {msg}"

    debug(mock_get_message)

    mock_print.assert_called_once_with("DEBUG: Test message", file=sys.stderr)

    mock_settings.debug = False
    debug(mock_get_message)
    mock_print.assert_called_once()  # Ensure print is not called again
