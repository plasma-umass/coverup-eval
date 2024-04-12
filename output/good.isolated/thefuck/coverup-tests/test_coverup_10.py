# file thefuck/rules/vagrant_up.py:10-21
# lines [10, 11, 12, 13, 14, 16, 17, 18, 20, 21]
# branches ['13->14', '13->16', '17->18', '17->20']

import pytest
from thefuck.types import Command
from thefuck.shells import shell

# Assuming the module structure is thefuck.rules.vagrant_up
from thefuck.rules import vagrant_up

@pytest.fixture
def vagrant_up_command(mocker):
    mocker.patch('thefuck.shells.shell.and_')
    return Command('vagrant up', '')

@pytest.fixture
def vagrant_up_with_machine_command(mocker):
    mocker.patch('thefuck.shells.shell.and_')
    return Command('vagrant up machine_name', '')

def test_vagrant_up_without_machine(vagrant_up_command):
    new_command = vagrant_up.get_new_command(vagrant_up_command)
    assert shell.and_.call_count == 1
    shell.and_.assert_called_once_with(u"vagrant up", vagrant_up_command.script)
    assert new_command == shell.and_.return_value

def test_vagrant_up_with_machine(vagrant_up_with_machine_command):
    new_command = vagrant_up.get_new_command(vagrant_up_with_machine_command)
    assert shell.and_.call_count == 2
    shell.and_.assert_any_call(u"vagrant up machine_name", vagrant_up_with_machine_command.script)
    shell.and_.assert_any_call(u"vagrant up", vagrant_up_with_machine_command.script)
    assert new_command == [shell.and_.return_value, shell.and_.return_value]
