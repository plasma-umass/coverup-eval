# file: py_backwards/utils/helpers.py:43-45
# asked: {"lines": [44, 45], "branches": [[44, 0], [44, 45]]}
# gained: {"lines": [44, 45], "branches": [[44, 0], [44, 45]]}

import pytest
from unittest.mock import patch, MagicMock
from py_backwards.utils.helpers import debug

def test_debug_with_debug_enabled(monkeypatch):
    # Mock settings.debug to be True
    monkeypatch.setattr('py_backwards.utils.helpers.settings.debug', True)
    
    # Mock the get_message callable
    get_message = MagicMock(return_value="Test message")
    
    # Mock the print function to capture its output
    with patch('py_backwards.utils.helpers.messages.debug', return_value="DEBUG: Test message") as mock_debug:
        with patch('sys.stderr', new_callable=MagicMock()) as mock_stderr:
            debug(get_message)
            mock_debug.assert_called_once_with("Test message")
            mock_stderr.write.assert_any_call("DEBUG: Test message")
            mock_stderr.write.assert_any_call("\n")

def test_debug_with_debug_disabled(monkeypatch):
    # Mock settings.debug to be False
    monkeypatch.setattr('py_backwards.utils.helpers.settings.debug', False)
    
    # Mock the get_message callable
    get_message = MagicMock(return_value="Test message")
    
    # Mock the print function to ensure it is not called
    with patch('sys.stderr', new_callable=MagicMock()) as mock_stderr:
        debug(get_message)
        mock_stderr.write.assert_not_called()
