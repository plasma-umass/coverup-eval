# file thefuck/rules/pacman_invalid_option.py:15-17
# lines [15, 16, 17]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.pacman_invalid_option import get_new_command
import re

@pytest.fixture
def pacman_invalid_option():
    return 'error: invalid option -x'

@pytest.fixture
def command(pacman_invalid_option):
    return Command('pacman -x', pacman_invalid_option)

def test_get_new_command(mocker, command):
    mocker.patch('re.findall', return_value=[' -x'])
    mocker.patch('re.sub', side_effect=lambda opt, opt_upper, script: script.replace(opt, opt_upper))
    new_command = get_new_command(command)
    assert new_command == 'pacman -X'
    re.findall.assert_called_once_with(r" -[dfqrstuv]", command.script)
    re.sub.assert_called_once_with(' -x', ' -X', command.script)
