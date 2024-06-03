# file lib/ansible/cli/console.py:331-338
# lines [331, 333, 334, 335, 336, 338]
# branches ['333->334', '333->338']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli(mocker):
    mocker.patch('ansible.cli.console.CLI.__init__', return_value=None)
    cli = ConsoleCLI(args=[])
    cli.become = False
    cli.set_prompt = mock.Mock()
    return cli

def test_do_become_with_arg(console_cli, mocker):
    mocker.patch('ansible.cli.console.boolean', return_value=True)
    display_v_mock = mocker.patch('ansible.cli.console.display.v')
    
    console_cli.do_become('yes')
    
    assert console_cli.become is True
    console_cli.set_prompt.assert_called_once()
    display_v_mock.assert_called_once_with("become changed to True")

def test_do_become_without_arg(console_cli, mocker):
    display_display_mock = mocker.patch('ansible.cli.console.display.display')
    
    console_cli.do_become('')
    
    display_display_mock.assert_called_once_with("Please specify become value, e.g. `become yes`")
