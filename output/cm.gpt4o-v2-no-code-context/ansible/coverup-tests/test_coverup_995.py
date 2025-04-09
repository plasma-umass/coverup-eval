# file: lib/ansible/cli/console.py:135-145
# asked: {"lines": [136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[139, 140], [139, 143]]}
# gained: {"lines": [136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[139, 140], [139, 143]]}

import pytest
from unittest import mock
from ansible.cli.console import ConsoleCLI
import getpass
from ansible.utils.color import stringc

@pytest.fixture
def console_cli():
    args = mock.Mock()
    cli = ConsoleCLI(args)
    cli.remote_user = None
    cli.cwd = 'test_cwd'
    cli.forks = 5
    cli.become = False
    cli.become_user = None
    cli.inventory = mock.Mock()
    cli.inventory.list_hosts = mock.Mock(return_value=['host1', 'host2'])
    cli.NORMAL_PROMPT = 'normal_prompt_color'
    return cli

def test_set_prompt_no_become(console_cli, monkeypatch):
    monkeypatch.setattr(getpass, 'getuser', lambda: 'testuser')
    monkeypatch.setattr('ansible.cli.console.stringc', lambda text, color, wrap_nonvisible_chars: text)
    console_cli.set_prompt()
    assert console_cli.prompt == 'testuser@test_cwd (2)[f:5]$ '

def test_set_prompt_become_root(console_cli, monkeypatch):
    monkeypatch.setattr(getpass, 'getuser', lambda: 'testuser')
    monkeypatch.setattr('ansible.cli.console.stringc', lambda text, color, wrap_nonvisible_chars: text)
    console_cli.become = True
    console_cli.become_user = 'root'
    console_cli.set_prompt()
    assert console_cli.prompt == 'testuser@test_cwd (2)[f:5]# '

def test_set_prompt_become_non_root(console_cli, monkeypatch):
    monkeypatch.setattr(getpass, 'getuser', lambda: 'testuser')
    monkeypatch.setattr('ansible.cli.console.stringc', lambda text, color, wrap_nonvisible_chars: text)
    console_cli.become = True
    console_cli.become_user = 'nonroot'
    console_cli.set_prompt()
    assert console_cli.prompt == 'testuser@test_cwd (2)[f:5]$ '
