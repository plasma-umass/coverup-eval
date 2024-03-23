# file thefuck/types.py:54-56
# lines [54, 55, 56]
# branches []

import pytest
from thefuck.types import Command

def test_command_repr():
    command = Command(script="ls -la", output="total 0")
    expected_repr = "Command(script=ls -la, output=total 0)"
    assert repr(command) == expected_repr
