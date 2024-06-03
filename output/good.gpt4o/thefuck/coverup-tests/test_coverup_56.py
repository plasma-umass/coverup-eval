# file thefuck/rules/sudo_command_from_user_path.py:18-21
# lines [18, 19, 20, 21]
# branches []

import pytest
from unittest.mock import Mock
from thefuck.rules.sudo_command_from_user_path import get_new_command

def test_get_new_command(mocker):
    # Mock the _get_command_name and replace_argument functions
    mock_get_command_name = mocker.patch('thefuck.rules.sudo_command_from_user_path._get_command_name')
    mock_replace_argument = mocker.patch('thefuck.rules.sudo_command_from_user_path.replace_argument')

    # Set up the mock return values
    mock_get_command_name.return_value = 'mock_command'
    mock_replace_argument.return_value = 'env "PATH=$PATH" mock_command'

    # Create a mock command object
    command = Mock()
    command.script = 'sudo mock_command'

    # Call the function
    result = get_new_command(command)

    # Assertions to verify the behavior
    mock_get_command_name.assert_called_once_with(command)
    mock_replace_argument.assert_called_once_with('sudo mock_command', 'mock_command', 'env "PATH=$PATH" mock_command')
    assert result == 'env "PATH=$PATH" mock_command'
