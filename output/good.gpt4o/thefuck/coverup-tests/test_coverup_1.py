# file thefuck/shells/generic.py:22-28
# lines [22, 23, 24, 25, 26, 28]
# branches ['25->26', '25->28']

import pytest
from unittest.mock import patch

# Assuming the Generic class is imported from thefuck.shells.generic
from thefuck.shells.generic import Generic

@pytest.fixture
def generic():
    return Generic()

def test_expand_aliases_with_alias(generic, mocker):
    mocker.patch.object(generic, 'get_aliases', return_value={'ls': 'ls --color=auto'})
    command_script = 'ls -l'
    expanded_script = generic._expand_aliases(command_script)
    assert expanded_script == 'ls --color=auto -l'

def test_expand_aliases_without_alias(generic, mocker):
    mocker.patch.object(generic, 'get_aliases', return_value={'ls': 'ls --color=auto'})
    command_script = 'cat file.txt'
    expanded_script = generic._expand_aliases(command_script)
    assert expanded_script == 'cat file.txt'
