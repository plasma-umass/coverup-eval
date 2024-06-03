# file thefuck/types.py:26-29
# lines [26, 27, 28, 29]
# branches []

import pytest
import logging
from unittest.mock import patch

# Assuming the Command class is imported from thefuck.types
from thefuck.types import Command

def test_command_stdout_deprecation_warning(mocker):
    # Mock the logger to capture the warning message
    mock_warn = mocker.patch('thefuck.types.logs.warn')

    # Create an instance of Command with required arguments
    cmd = Command(script="test script", output="test output")

    # Access the stdout property to trigger the warning
    result = cmd.stdout

    # Assert that the warning was logged
    mock_warn.assert_called_once_with('`stdout` is deprecated, please use `output` instead')

    # Assert that the stdout property returns the correct output
    assert result == "test output"
