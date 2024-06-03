# file thefuck/types.py:36-46
# lines [36, 37, 38, 39, 40, 41, 42, 43, 44, 46]
# branches ['38->39', '38->46']

import pytest
from unittest import mock
import sys

# Assuming the Command class is imported from thefuck.types
from thefuck.types import Command

@pytest.fixture
def mock_shell_split_command(mocker):
    return mocker.patch('thefuck.types.shell.split_command')

@pytest.fixture
def mock_logs_debug(mocker):
    return mocker.patch('thefuck.types.logs.debug')

def test_script_parts_success(mock_shell_split_command):
    cmd = Command(script='echo "Hello, World!"', output='')
    mock_shell_split_command.return_value = ['echo', 'Hello, World!']
    
    result = cmd.script_parts
    
    assert result == ['echo', 'Hello, World!']
    assert hasattr(cmd, '_script_parts')
    assert cmd._script_parts == ['echo', 'Hello, World!']

def test_script_parts_exception(mock_shell_split_command, mock_logs_debug):
    cmd = Command(script='invalid command', output='')
    mock_shell_split_command.side_effect = Exception('split error')
    
    result = cmd.script_parts
    
    assert result == []
    assert hasattr(cmd, '_script_parts')
    assert cmd._script_parts == []
    mock_logs_debug.assert_called_once()
    call_args = mock_logs_debug.call_args[0][0]
    assert call_args.startswith("Can't split command script Command(script=invalid command, output=) because:\n")
    assert "Exception('split error')" in call_args
