# file thefuck/types.py:13-15
# lines [13, 14]
# branches []

import pytest
from thefuck.types import Command

def test_command_initialization():
    # Test the initialization of the Command class with required arguments
    script = 'echo hello'
    output = 'hello'
    cmd = Command(script, output)
    assert isinstance(cmd, Command)
    assert cmd.script == script
    assert cmd.output == output
