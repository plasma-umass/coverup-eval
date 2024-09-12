# file: lib/ansible/cli/console.py:66-92
# asked: {"lines": [66, 68, 70, 72, 73, 74, 75, 76, 77, 79, 80, 83, 84, 85, 86, 87, 88, 89, 90, 92], "branches": []}
# gained: {"lines": [66, 68, 70, 72, 73, 74, 75, 76, 77, 79, 80, 83, 84, 85, 86, 87, 88, 89, 90, 92], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI
from unittest import mock

@pytest.fixture
def mock_args():
    return mock.Mock()

def test_console_cli_initialization(mock_args):
    cli = ConsoleCLI(mock_args)
    
    assert cli.intro == 'Welcome to the ansible console. Type help or ? to list commands.\n'
    assert cli.groups == []
    assert cli.hosts == []
    assert cli.pattern is None
    assert cli.variable_manager is None
    assert cli.loader is None
    assert cli.passwords == {}
    assert cli.modules is None
    assert cli.cwd == '*'
    assert cli.remote_user is None
    assert cli.become is None
    assert cli.become_user is None
    assert cli.become_method is None
    assert cli.check_mode is None
    assert cli.diff is None
    assert cli.forks is None
    assert cli.task_timeout is None
