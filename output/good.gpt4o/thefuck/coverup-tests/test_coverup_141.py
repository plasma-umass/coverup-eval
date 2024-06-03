# file thefuck/rules/vagrant_up.py:10-21
# lines [11, 12, 13, 14, 16, 17, 18, 20, 21]
# branches ['13->14', '13->16', '17->18', '17->20']

import pytest
from thefuck.rules.vagrant_up import get_new_command
from thefuck.types import Command
from unittest import mock

@pytest.fixture
def mock_shell_and(mocker):
    return mocker.patch('thefuck.rules.vagrant_up.shell.and_')

def test_get_new_command_with_machine(mock_shell_and):
    command = Command('vagrant up machine_name', ['vagrant', 'up', 'machine_name'])
    mock_shell_and.side_effect = lambda *args: ' && '.join(args)
    
    result = get_new_command(command)
    
    assert result == ['vagrant up machine_name && vagrant up machine_name', 'vagrant up && vagrant up machine_name']

def test_get_new_command_without_machine(mock_shell_and):
    command = Command('vagrant up', ['vagrant', 'up'])
    mock_shell_and.side_effect = lambda *args: ' && '.join(args)
    
    result = get_new_command(command)
    
    assert result == 'vagrant up && vagrant up'
