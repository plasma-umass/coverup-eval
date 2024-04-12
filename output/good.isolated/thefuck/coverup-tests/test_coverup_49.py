# file thefuck/types.py:58-66
# lines [58, 64, 65, 66]
# branches []

import pytest
from thefuck.types import Command

def test_command_update():
    original_command = Command('ls', 'total 0')
    updated_command = original_command.update(script='ls -la')

    assert updated_command.script == 'ls -la'
    assert updated_command.output == 'total 0'

    # Ensure that the original command is not modified
    assert original_command.script == 'ls'
    assert original_command.output == 'total 0'

    # Test updating with no changes
    same_command = original_command.update()
    assert same_command.script == 'ls'
    assert same_command.output == 'total 0'
