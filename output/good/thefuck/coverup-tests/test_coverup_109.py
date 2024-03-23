# file thefuck/shells/generic.py:124-134
# lines [124, 126]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_get_builtin_commands():
    shell = Generic()
    builtins = shell.get_builtin_commands()
    assert isinstance(builtins, list)
    assert 'alias' in builtins
    assert 'cd' in builtins
    assert 'exit' in builtins
    assert 'export' in builtins
    assert 'echo' in builtins
    assert 'pwd' in builtins
    assert 'unset' in builtins
    assert 'while' in builtins
