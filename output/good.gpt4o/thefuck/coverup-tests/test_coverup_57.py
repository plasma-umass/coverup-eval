# file thefuck/types.py:16-24
# lines [16, 23, 24]
# branches []

import pytest
from thefuck.types import Command

def test_command_initialization():
    script = "echo 'Hello, World!'"
    output = "Hello, World!\n"
    
    command = Command(script, output)
    
    assert command.script == script
    assert command.output == output
