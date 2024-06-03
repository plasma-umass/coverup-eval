# file thefuck/shells/generic.py:30-32
# lines [30, 32]
# branches []

import pytest
from unittest.mock import patch
from thefuck.shells.generic import Generic

@pytest.fixture
def generic():
    return Generic()

def test_from_shell(generic, mocker):
    command_script = "some_command"
    mock_expand_aliases = mocker.patch.object(generic, '_expand_aliases', return_value="expanded_command")
    
    result = generic.from_shell(command_script)
    
    mock_expand_aliases.assert_called_once_with(command_script)
    assert result == "expanded_command"
