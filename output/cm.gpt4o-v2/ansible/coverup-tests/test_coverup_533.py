# file: lib/ansible/cli/console.py:348-355
# asked: {"lines": [348, 350, 351, 353, 354, 355], "branches": [[350, 351], [350, 353]]}
# gained: {"lines": [348, 350, 351, 353, 354, 355], "branches": [[350, 351], [350, 353]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    cli = ConsoleCLI(args=['test'])
    cli.become_user = None
    cli.inventory = MagicMock()
    return cli

def test_do_become_user_with_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.do_become_user('testuser')
        assert console_cli.become_user == 'testuser'
        mock_display.display.assert_not_called()
        mock_display.v.assert_not_called()

def test_do_become_user_without_arg(console_cli):
    with patch('ansible.cli.console.display') as mock_display:
        console_cli.become_user = 'currentuser'
        console_cli.do_become_user('')
        mock_display.display.assert_called_once_with("Please specify a user, e.g. `become_user jenkins`")
        mock_display.v.assert_called_once_with("Current user is currentuser")

def test_do_become_user_set_prompt_called(console_cli):
    with patch.object(console_cli, 'set_prompt') as mock_set_prompt:
        console_cli.do_become_user('testuser')
        mock_set_prompt.assert_called_once()
