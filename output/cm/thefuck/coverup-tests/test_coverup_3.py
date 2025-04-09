# file thefuck/shells/generic.py:22-28
# lines [22, 23, 24, 25, 26, 28]
# branches ['25->26', '25->28']

import pytest
from thefuck.shells.generic import Generic

@pytest.fixture
def generic_shell(mocker):
    mocker.patch.object(Generic, 'get_aliases', return_value={'ls': 'ls -G'})
    return Generic()

def test_expand_aliases_with_alias(generic_shell):
    command_script = 'ls /home'
    expanded_script = generic_shell._expand_aliases(command_script)
    assert expanded_script == 'ls -G /home'

def test_expand_aliases_without_alias(generic_shell):
    command_script = 'cd /home'
    expanded_script = generic_shell._expand_aliases(command_script)
    assert expanded_script == 'cd /home'
