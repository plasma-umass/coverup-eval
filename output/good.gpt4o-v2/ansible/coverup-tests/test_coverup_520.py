# file: lib/ansible/constants.py:23-30
# asked: {"lines": [23, 25, 26, 27, 28, 29, 30], "branches": []}
# gained: {"lines": [23, 25, 26, 27, 28, 29, 30], "branches": []}

import pytest
import sys
from unittest import mock

# Import the _warning function from the module where it is defined
from ansible.constants import _warning

def test_warning_with_display(monkeypatch):
    # Mock the Display class and its warning method
    mock_display = mock.Mock()
    monkeypatch.setattr('ansible.utils.display.Display', mock_display)

    # Call the _warning function
    _warning("Test message")

    # Assert that the Display.warning method was called with the correct message
    mock_display().warning.assert_called_once_with("Test message")

def test_warning_without_display(monkeypatch):
    # Mock the import of Display to raise an ImportError
    monkeypatch.delattr('ansible.utils.display.Display', raising=False)

    # Mock sys.stderr to capture the output
    mock_stderr = mock.Mock()
    monkeypatch.setattr(sys, 'stderr', mock_stderr)

    # Call the _warning function
    _warning("Test message")

    # Assert that sys.stderr.write was called with the correct message
    mock_stderr.write.assert_called_once_with(' [WARNING] Test message\n')
