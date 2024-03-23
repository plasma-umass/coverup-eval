# file lib/ansible/cli/console.py:261-273
# lines [261, 273]
# branches []

import pytest
from ansible.cli.console import ConsoleCLI
from unittest.mock import MagicMock

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    console_cli_instance = ConsoleCLI(args=[])
    console_cli_instance.default = MagicMock()
    return console_cli_instance

def test_do_shell(console_cli):
    test_arg = 'ps aux | grep java | wc -l'
    console_cli.do_shell(test_arg)
    console_cli.default.assert_called_once_with(test_arg, True)
