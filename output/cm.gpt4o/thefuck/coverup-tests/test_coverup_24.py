# file thefuck/rules/sudo_command_from_user_path.py:11-15
# lines [11, 12, 13, 14, 15]
# branches ['13->exit', '13->14']

import pytest
from thefuck.rules.sudo_command_from_user_path import match
from thefuck.types import Command
from unittest.mock import patch

@pytest.fixture
def mock_which(mocker):
    return mocker.patch('thefuck.rules.sudo_command_from_user_path.which')

@pytest.fixture
def mock_get_command_name(mocker):
    return mocker.patch('thefuck.rules.sudo_command_from_user_path._get_command_name')

def test_match_command_not_found(mock_which, mock_get_command_name):
    command = Command('sudo somecommand', 'sudo: somecommand: command not found')
    mock_get_command_name.return_value = 'somecommand'
    mock_which.return_value = '/usr/local/bin/somecommand'

    assert match(command)
    mock_get_command_name.assert_called_once_with(command)
    mock_which.assert_called_once_with('somecommand')

def test_match_command_found(mock_which, mock_get_command_name):
    command = Command('sudo somecommand', 'some other output')
    mock_get_command_name.return_value = 'somecommand'
    mock_which.return_value = None

    assert not match(command)
    mock_get_command_name.assert_not_called()
    mock_which.assert_not_called()
