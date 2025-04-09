# file lib/ansible/cli/console.py:261-273
# lines [261, 273]
# branches []

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli(mocker):
    mock_args = mocker.Mock()
    return ConsoleCLI(mock_args)

def test_do_shell(console_cli, mocker):
    mock_default = mocker.patch.object(console_cli, 'default')
    
    test_command = 'ps aux | grep java | wc -l'
    console_cli.do_shell(test_command)
    
    mock_default.assert_called_once_with(test_command, True)
