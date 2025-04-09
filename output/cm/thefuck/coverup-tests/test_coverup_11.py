# file thefuck/types.py:68-83
# lines [68, 69, 77, 78, 79, 81, 82, 83]
# branches ['78->79', '78->81']

import pytest
from thefuck.types import Command, EmptyCommand
from thefuck.shells import shell
from unittest.mock import Mock

# Mocking the shell.from_shell and get_output functions
@pytest.fixture
def mock_shell(mocker):
    mocker.patch('thefuck.types.shell.from_shell', return_value='mocked_expanded')
    mocker.patch('thefuck.types.get_output', return_value='mocked_output')

def test_command_from_raw_script_with_non_empty_script(mock_shell):
    raw_script = ['echo', 'Hello, World!']
    command = Command.from_raw_script(raw_script)
    assert command.script == 'mocked_expanded'
    assert command.output == 'mocked_output'

def test_command_from_raw_script_with_empty_script_raises_exception(mock_shell):
    raw_script = []
    with pytest.raises(EmptyCommand):
        Command.from_raw_script(raw_script)
