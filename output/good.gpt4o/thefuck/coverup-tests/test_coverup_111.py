# file thefuck/shells/generic.py:82-91
# lines [88, 89]
# branches []

import pytest
from thefuck.shells.generic import Generic

def test_split_command_handles_value_error(mocker):
    generic = Generic()
    command = 'unclosed "quote'
    
    mocker.patch('shlex.split', side_effect=ValueError)
    
    result = generic.split_command(command)
    
    assert result == command.split(' ')
