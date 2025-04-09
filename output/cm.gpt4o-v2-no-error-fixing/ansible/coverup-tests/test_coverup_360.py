# file: lib/ansible/constants.py:23-30
# asked: {"lines": [23, 25, 26, 27, 28, 29, 30], "branches": []}
# gained: {"lines": [23, 25, 26, 27, 28, 29, 30], "branches": []}

import pytest
import sys
from unittest.mock import patch, MagicMock

def test_warning_display(monkeypatch):
    from ansible.constants import _warning

    # Mock the Display class and its warning method
    mock_display = MagicMock()
    monkeypatch.setattr('ansible.utils.display.Display', mock_display)

    # Call the _warning function
    _warning("Test message")

    # Assert that Display.warning was called with the correct message
    mock_display().warning.assert_called_once_with("Test message")

def test_warning_sys_stderr(monkeypatch):
    from ansible.constants import _warning

    # Mock the import of Display to raise an ImportError
    monkeypatch.setattr('ansible.utils.display.Display', None)

    # Capture the output to sys.stderr
    with patch('sys.stderr.write') as mock_stderr:
        _warning("Test message")

    # Assert that sys.stderr.write was called with the correct message
    mock_stderr.assert_called_once_with(' [WARNING] Test message\n')
