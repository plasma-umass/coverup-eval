# file: lib/ansible/cli/console.py:431-437
# asked: {"lines": [431, 432, 433, 434, 435, 437], "branches": [[432, 0], [432, 433]]}
# gained: {"lines": [431, 432, 433, 434, 435, 437], "branches": [[432, 0], [432, 433]]}

import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    return ConsoleCLI(['test_arg'])

def test_completedefault_with_module(console_cli, mocker):
    mocker.patch.object(console_cli, 'modules', ['test_module'])
    mocker.patch.object(console_cli, 'module_args', return_value=['arg1', 'arg2', 'arg3'])
    
    result = console_cli.completedefault('arg', 'test_module arg', 0, 0)
    
    assert result == ['arg1=', 'arg2=', 'arg3=']

def test_completedefault_without_module(console_cli, mocker):
    mocker.patch.object(console_cli, 'modules', ['test_module'])
    
    result = console_cli.completedefault('arg', 'other_module arg', 0, 0)
    
    assert result is None
