# file lib/ansible/constants.py:23-30
# lines [23, 25, 26, 27, 28, 29, 30]
# branches []

import pytest
import sys
from unittest import mock

# Import the function to be tested
from ansible.constants import _warning

def test_warning_with_display(mocker):
    # Mock the Display class and its warning method
    mock_display = mocker.patch('ansible.utils.display.Display')
    mock_warning = mock_display.return_value.warning

    # Call the function with a test message
    test_msg = "Test message"
    _warning(test_msg)

    # Assert that the Display.warning method was called with the test message
    mock_warning.assert_called_once_with(test_msg)

def test_warning_without_display(mocker):
    # Mock the import of Display to raise an ImportError
    mocker.patch('ansible.utils.display.Display', side_effect=Exception)

    # Mock sys.stderr.write
    mock_stderr_write = mocker.patch('sys.stderr.write')

    # Call the function with a test message
    test_msg = "Test message"
    _warning(test_msg)

    # Assert that sys.stderr.write was called with the formatted warning message
    mock_stderr_write.assert_called_once_with(f' [WARNING] {test_msg}\n')
