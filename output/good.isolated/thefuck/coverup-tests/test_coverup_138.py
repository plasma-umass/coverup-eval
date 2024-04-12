# file thefuck/rules/sudo_command_from_user_path.py:18-21
# lines [19, 20, 21]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.sudo_command_from_user_path import get_new_command
from thefuck.rules.sudo_command_from_user_path import match
from unittest.mock import Mock

@pytest.fixture
def sudo_command():
    return Command('sudo ls', '')

def test_get_new_command_with_sudo(sudo_command, mocker):
    mocker.patch('thefuck.rules.sudo_command_from_user_path._get_command_name', return_value='ls')
    mocker.patch('thefuck.rules.sudo_command_from_user_path.replace_argument', return_value='env "PATH=$PATH" ls')

    new_command = get_new_command(sudo_command)
    assert new_command == 'env "PATH=$PATH" ls'
