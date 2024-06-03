# file lib/ansible/cli/console.py:348-355
# lines [348, 350, 351, 353, 354, 355]
# branches ['350->351', '350->353']

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
from ansible.utils.display import Display

@pytest.fixture
def console_cli():
    cli = ConsoleCLI(args=['test'])
    cli.become_user = 'default_user'
    cli.set_prompt = mock.MagicMock()
    return cli

def test_do_become_user_with_arg(console_cli):
    console_cli.do_become_user('jenkins')
    assert console_cli.become_user == 'jenkins'
    console_cli.set_prompt.assert_called_once()

def test_do_become_user_without_arg(console_cli, mocker):
    mock_display = mocker.patch.object(Display, 'display')
    mock_v = mocker.patch.object(Display, 'v')
    
    console_cli.do_become_user('')
    
    mock_display.assert_called_once_with("Please specify a user, e.g. `become_user jenkins`")
    mock_v.assert_called_once_with("Current user is default_user")
    console_cli.set_prompt.assert_called_once()
