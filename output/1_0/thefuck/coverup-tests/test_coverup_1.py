# file thefuck/rules/sl_ls.py:13-14
# lines [13, 14]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.sl_ls import get_new_command

def test_get_new_command():
    command = Command('sl', '')
    new_command = get_new_command(command)
    assert new_command == 'ls'
