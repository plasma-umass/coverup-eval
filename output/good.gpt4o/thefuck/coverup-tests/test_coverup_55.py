# file thefuck/rules/tsuru_not_command.py:11-15
# lines [11, 12, 13, 14, 15]
# branches []

import pytest
import re
from thefuck.rules.tsuru_not_command import get_new_command
from thefuck.types import Command

@pytest.fixture
def mock_replace_command(mocker):
    return mocker.patch('thefuck.rules.tsuru_not_command.replace_command')

@pytest.fixture
def mock_get_all_matched_commands(mocker):
    return mocker.patch('thefuck.rules.tsuru_not_command.get_all_matched_commands')

def test_get_new_command(mock_replace_command, mock_get_all_matched_commands):
    command = Command('tsuru somecmd', 'tsuru: "somecmd" is not a tsuru command')
    broken_cmd = 'somecmd'
    matched_commands = ['someothercmd']
    
    mock_get_all_matched_commands.return_value = matched_commands
    
    new_command = get_new_command(command)
    
    mock_replace_command.assert_called_once_with(command, broken_cmd, matched_commands)
    assert new_command == mock_replace_command.return_value
