# file: lib/ansible/cli/console.py:348-355
# asked: {"lines": [348, 350, 351, 353, 354, 355], "branches": [[350, 351], [350, 353]]}
# gained: {"lines": [348, 350, 351, 353, 354, 355], "branches": [[350, 351], [350, 353]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    cli = ConsoleCLI(args=['test'])
    cli.become_user = None
    cli.remote_user = 'test_user'
    cli.cwd = 'test_cwd'
    cli.forks = 1
    cli.NORMAL_PROMPT = 'normal'
    cli.inventory = MagicMock()
    cli.inventory.list_hosts.return_value = ['host1', 'host2']
    return cli

def test_do_become_user_with_arg(console_cli):
    console_cli.set_prompt = MagicMock()
    console_cli.do_become_user('jenkins')
    assert console_cli.become_user == 'jenkins'
    console_cli.set_prompt.assert_called_once()

def test_do_become_user_without_arg(console_cli):
    with patch('ansible.cli.console.display.display') as mock_display, \
         patch('ansible.cli.console.display.v') as mock_v:
        console_cli.set_prompt = MagicMock()
        console_cli.do_become_user('')
        mock_display.assert_called_once_with("Please specify a user, e.g. `become_user jenkins`")
        mock_v.assert_called_once_with("Current user is %s" % console_cli.become_user)
        console_cli.set_prompt.assert_called_once()
