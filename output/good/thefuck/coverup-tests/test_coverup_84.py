# file thefuck/shells/generic.py:34-36
# lines [34, 36]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_generic_to_shell():
    generic_shell = Generic()
    command_script = "echo 'Hello, World!'"
    result = generic_shell.to_shell(command_script)
    assert result == command_script
