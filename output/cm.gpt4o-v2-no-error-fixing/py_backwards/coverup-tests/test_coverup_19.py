# file: py_backwards/utils/helpers.py:43-45
# asked: {"lines": [43, 44, 45], "branches": [[44, 0], [44, 45]]}
# gained: {"lines": [43, 44, 45], "branches": [[44, 0], [44, 45]]}

import pytest
import sys
from py_backwards.utils.helpers import debug
from py_backwards.conf import settings
from py_backwards import messages

def test_debug_message_printed(monkeypatch, capsys):
    # Arrange
    settings.debug = True
    test_message = "Test debug message"
    
    def mock_get_message():
        return test_message
    
    # Act
    debug(mock_get_message)
    
    # Assert
    captured = capsys.readouterr()
    assert messages.debug(test_message) in captured.err
    
    # Cleanup
    settings.debug = False

def test_debug_message_not_printed(monkeypatch, capsys):
    # Arrange
    settings.debug = False
    test_message = "Test debug message"
    
    def mock_get_message():
        return test_message
    
    # Act
    debug(mock_get_message)
    
    # Assert
    captured = capsys.readouterr()
    assert messages.debug(test_message) not in captured.err
