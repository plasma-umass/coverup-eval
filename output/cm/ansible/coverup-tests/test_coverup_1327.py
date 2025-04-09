# file lib/ansible/cli/console.py:431-437
# lines [432, 433, 434, 435, 437]
# branches ['432->exit', '432->433']

import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    mocker.patch('cmd.Cmd.__init__', return_value=None)
    console_cli = ConsoleCLI(args=[])
    console_cli.modules = {'testmodule': None}
    console_cli.module_args = mocker.Mock(return_value=['arg1', 'arg2'])
    return console_cli

def test_completedefault_with_module(console_cli):
    text = 'arg'
    line = 'testmodule arg'
    begidx = len('testmodule ')
    endidx = len(line)
    completions = console_cli.completedefault(text, line, begidx, endidx)
    assert completions == ['arg1=', 'arg2=']
    console_cli.module_args.assert_called_once_with('testmodule')
