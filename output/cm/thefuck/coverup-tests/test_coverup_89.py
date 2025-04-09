# file thefuck/shells/generic.py:30-32
# lines [30, 32]
# branches []

import pytest
from thefuck.shells.generic import Generic

@pytest.fixture
def generic_shell():
    return Generic()

def test_from_shell_expands_aliases(mocker, generic_shell):
    mocker.patch.object(generic_shell, '_expand_aliases', return_value='expanded_command')
    command_script = 'some_command'
    result = generic_shell.from_shell(command_script)
    generic_shell._expand_aliases.assert_called_once_with(command_script)
    assert result == 'expanded_command'
