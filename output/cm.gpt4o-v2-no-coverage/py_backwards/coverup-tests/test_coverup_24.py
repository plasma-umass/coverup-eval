# file: py_backwards/utils/helpers.py:43-45
# asked: {"lines": [43, 44, 45], "branches": [[44, 0], [44, 45]]}
# gained: {"lines": [43, 44, 45], "branches": [[44, 0], [44, 45]]}

import pytest
from unittest.mock import patch, MagicMock
from py_backwards.utils.helpers import debug
from py_backwards.conf import settings
from py_backwards import messages

def test_debug_with_debug_enabled(monkeypatch):
    # Arrange
    monkeypatch.setattr(settings, 'debug', True)
    mock_get_message = MagicMock(return_value="Test message")
    mock_print = MagicMock()
    
    with patch('sys.stderr', new_callable=MagicMock()) as mock_stderr:
        with patch('builtins.print', mock_print):
            # Act
            debug(mock_get_message)
            
            # Assert
            mock_get_message.assert_called_once()
            mock_print.assert_called_once_with(messages.debug("Test message"), file=mock_stderr)

def test_debug_with_debug_disabled(monkeypatch):
    # Arrange
    monkeypatch.setattr(settings, 'debug', False)
    mock_get_message = MagicMock()
    mock_print = MagicMock()
    
    with patch('builtins.print', mock_print):
        # Act
        debug(mock_get_message)
        
        # Assert
        mock_get_message.assert_not_called()
        mock_print.assert_not_called()
