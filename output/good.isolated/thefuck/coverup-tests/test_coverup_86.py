# file thefuck/rules/cp_create_destination.py:14-15
# lines [14, 15]
# branches []

import pytest
from thefuck.types import Command
from thefuck.shells import shell
from thefuck.rules.cp_create_destination import get_new_command

def test_get_new_command(mocker):
    mocker.patch('thefuck.shells.shell.and_', return_value='mkdir -p new_dir && cp file.txt new_dir')
    command = Command('cp file.txt new_dir', '')
    new_command = get_new_command(command)
    assert new_command == 'mkdir -p new_dir && cp file.txt new_dir'
    shell.and_.assert_called_once_with('mkdir -p new_dir', 'cp file.txt new_dir')
