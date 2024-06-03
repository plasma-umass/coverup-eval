# file thefuck/entrypoints/not_configured.py:82-88
# lines [82, 84, 85, 86, 87, 88]
# branches []

import pytest
from unittest.mock import mock_open, patch
from pathlib import Path

# Assuming the _configure function is imported from thefuck.entrypoints.not_configured
from thefuck.entrypoints.not_configured import _configure

class ConfigurationDetails:
    def __init__(self, path, content):
        self.path = path
        self.content = content

def test_configure(mocker):
    # Mock the Path object and its methods
    mock_path = mocker.patch('thefuck.entrypoints.not_configured.Path')
    mock_open_func = mock_open()
    mock_path.return_value.expanduser.return_value.open = mock_open_func

    # Create a ConfigurationDetails instance
    config_details = ConfigurationDetails('~/.bashrc', 'alias fuck="thefuck"')

    # Call the _configure function
    _configure(config_details)

    # Assert that the file was opened in append mode
    mock_open_func.assert_called_once_with('a')

    # Assert that the correct content was written to the file
    handle = mock_open_func()
    handle.write.assert_any_call(u'\n')
    handle.write.assert_any_call('alias fuck="thefuck"')
    handle.write.assert_any_call(u'\n')
