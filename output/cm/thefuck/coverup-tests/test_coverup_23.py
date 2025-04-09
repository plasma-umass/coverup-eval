# file thefuck/shells/generic.py:82-91
# lines [82, 84, 86, 87, 88, 89, 91]
# branches []

import pytest
from thefuck.shells.generic import Generic

@pytest.fixture
def generic_shell():
    return Generic()

def test_split_command_with_shlex_exception(generic_shell, mocker):
    mocker.patch('shlex.split', side_effect=ValueError)
    command = 'ls -la /some/path with\\ space'
    expected = ['ls', '-la', '/some/path', 'with\\', 'space']
    result = generic_shell.split_command(command)
    assert result == expected
