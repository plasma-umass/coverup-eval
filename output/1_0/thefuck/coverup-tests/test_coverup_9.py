# file thefuck/rules/remove_trailing_cedilla.py:10-11
# lines [10, 11]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.remove_trailing_cedilla import get_new_command

def test_get_new_command():
    command_with_cedilla = Command('ls ç', '')
    new_command = get_new_command(command_with_cedilla)
    assert new_command == 'ls '
