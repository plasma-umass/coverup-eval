# file thefuck/rules/cargo.py:5-6
# lines [5, 6]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.cargo import get_new_command

def test_get_new_command():
    command = Command('cargo some-invalid-command', '')
    new_command = get_new_command(command)
    assert new_command == 'cargo build'
