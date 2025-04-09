# file: lib/ansible/cli/console.py:348-355
# asked: {"lines": [348, 350, 351, 353, 354, 355], "branches": [[350, 351], [350, 353]]}
# gained: {"lines": [348, 350, 351, 353, 354, 355], "branches": [[350, 351], [350, 353]]}

import pytest
from ansible.cli.console import ConsoleCLI
from unittest import mock

@pytest.fixture
def console_cli():
    return ConsoleCLI(args=['test'])

def test_do_become_user_with_arg(console_cli, monkeypatch):
    mock_display = mock.Mock()
    monkeypatch.setattr('ansible.cli.console.display', mock_display)
    
    console_cli.become_user = None
    console_cli.set_prompt = mock.Mock()
    
    console_cli.do_become_user('jenkins')
    
    assert console_cli.become_user == 'jenkins'
    console_cli.set_prompt.assert_called_once()
    mock_display.display.assert_not_called()
    mock_display.v.assert_not_called()

def test_do_become_user_without_arg(console_cli, monkeypatch):
    mock_display = mock.Mock()
    monkeypatch.setattr('ansible.cli.console.display', mock_display)
    
    console_cli.become_user = 'existing_user'
    console_cli.set_prompt = mock.Mock()
    
    console_cli.do_become_user('')
    
    mock_display.display.assert_called_once_with("Please specify a user, e.g. `become_user jenkins`")
    mock_display.v.assert_called_once_with("Current user is existing_user")
    console_cli.set_prompt.assert_called_once()
