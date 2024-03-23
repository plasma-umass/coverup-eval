# file thefuck/rules/cd_parent.py:15-16
# lines [15, 16]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.cd_parent import get_new_command

def test_get_new_command():
    command = Command('cd..', '')
    new_command = get_new_command(command)
    assert new_command == 'cd ..'
