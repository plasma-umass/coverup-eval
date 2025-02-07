# file: lib/ansible/cli/console.py:261-273
# asked: {"lines": [261, 273], "branches": []}
# gained: {"lines": [261, 273], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    args = ['test']
    return ConsoleCLI(args)

def test_do_shell_executes_default(console_cli, mocker):
    mock_default = mocker.patch.object(console_cli, 'default')
    test_arg = 'ps aux | grep python'
    
    console_cli.do_shell(test_arg)
    
    mock_default.assert_called_once_with(test_arg, True)
