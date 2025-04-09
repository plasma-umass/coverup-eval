# file: lib/ansible/cli/console.py:66-92
# asked: {"lines": [66, 68, 70, 72, 73, 74, 75, 76, 77, 79, 80, 83, 84, 85, 86, 87, 88, 89, 90, 92], "branches": []}
# gained: {"lines": [66, 68, 70, 72, 73, 74, 75, 76, 77, 79, 80, 83, 84, 85, 86, 87, 88, 89, 90, 92], "branches": []}

import pytest
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    args = ['test']
    return ConsoleCLI(args)

def test_console_cli_initialization(console_cli):
    assert console_cli.intro == 'Welcome to the ansible console. Type help or ? to list commands.\n'
    assert console_cli.groups == []
    assert console_cli.hosts == []
    assert console_cli.pattern is None
    assert console_cli.variable_manager is None
    assert console_cli.loader is None
    assert console_cli.passwords == {}
    assert console_cli.modules is None
    assert console_cli.cwd == '*'
    assert console_cli.remote_user is None
    assert console_cli.become is None
    assert console_cli.become_user is None
    assert console_cli.become_method is None
    assert console_cli.check_mode is None
    assert console_cli.diff is None
    assert console_cli.forks is None
    assert console_cli.task_timeout is None
