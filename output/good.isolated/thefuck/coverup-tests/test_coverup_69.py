# file thefuck/rules/choco_install.py:10-22
# lines [10, 12, 13, 14, 16, 18, 21, 22]
# branches ['12->13', '12->22', '13->12', '13->21']

import pytest
from thefuck.types import Command
from thefuck.rules.choco_install import get_new_command

@pytest.fixture
def choco_install_command():
    return Command('choco install package', '')

def test_get_new_command_with_package_name(mocker):
    command = Command('choco install package', '')
    mocker.patch('thefuck.types.Command.script_parts', 
                 new_callable=lambda: ['choco', 'install', 'package'])
    new_command = get_new_command(command)
    assert new_command == 'choco install package.install'

def test_get_new_command_with_hyphenated_package_name(mocker):
    command = Command('choco install -pre package', '')
    mocker.patch('thefuck.types.Command.script_parts', 
                 new_callable=lambda: ['choco', 'install', '-pre', 'package'])
    new_command = get_new_command(command)
    assert new_command == 'choco install -pre package.install'

def test_get_new_command_with_no_package_name(mocker):
    command = Command('choco install', '')
    mocker.patch('thefuck.types.Command.script_parts', 
                 new_callable=lambda: ['choco', 'install'])
    new_command = get_new_command(command)
    assert new_command == []

def test_get_new_command_with_parameter_containing_equal_sign(mocker):
    command = Command('choco install package=version', '')
    mocker.patch('thefuck.types.Command.script_parts', 
                 new_callable=lambda: ['choco', 'install', 'package=version'])
    new_command = get_new_command(command)
    assert new_command == []

def test_get_new_command_with_parameter_containing_slash(mocker):
    command = Command('choco install /parameter package', '')
    mocker.patch('thefuck.types.Command.script_parts', 
                 new_callable=lambda: ['choco', 'install', '/parameter', 'package'])
    new_command = get_new_command(command)
    assert new_command == 'choco install /parameter package.install'
