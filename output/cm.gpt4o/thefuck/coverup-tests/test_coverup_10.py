# file thefuck/types.py:68-83
# lines [68, 69, 77, 78, 79, 81, 82, 83]
# branches ['78->79', '78->81']

import pytest
from unittest import mock
from thefuck.types import Command, EmptyCommand

def format_raw_script(raw_script):
    return ' '.join(raw_script)

def shell_from_shell(script):
    return script

def get_output(script, expanded):
    return f"Output of {expanded}"

@pytest.fixture
def mock_dependencies(mocker):
    mocker.patch('thefuck.types.format_raw_script', side_effect=format_raw_script)
    mocker.patch('thefuck.types.shell.from_shell', side_effect=shell_from_shell)
    mocker.patch('thefuck.types.get_output', side_effect=get_output)

def test_command_from_raw_script(mock_dependencies):
    raw_script = ['echo', 'hello']
    command = Command.from_raw_script(raw_script)
    assert command.script == 'echo hello'
    assert command.output == 'Output of echo hello'

def test_command_from_raw_script_empty(mock_dependencies):
    raw_script = []
    with pytest.raises(EmptyCommand):
        Command.from_raw_script(raw_script)
