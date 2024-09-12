# file: lib/ansible/cli/console.py:135-145
# asked: {"lines": [135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[139, 140], [139, 143]]}
# gained: {"lines": [135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[139, 140], [139, 143]]}

import pytest
import getpass
from ansible.cli.console import ConsoleCLI
from ansible import constants as C
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.utils.color import stringc

@pytest.fixture
def console_cli():
    args = ['test']
    cli = ConsoleCLI(args)
    cli.loader = DataLoader()
    cli.inventory = InventoryManager(loader=cli.loader, sources=['localhost,'])
    cli.variable_manager = VariableManager(loader=cli.loader, inventory=cli.inventory)
    return cli

def test_set_prompt_normal_user(monkeypatch, console_cli):
    monkeypatch.setattr(getpass, 'getuser', lambda: 'testuser')
    console_cli.remote_user = None
    console_cli.cwd = 'all'
    console_cli.forks = 5
    console_cli.become = False
    console_cli.become_user = None
    
    console_cli.set_prompt()
    
    expected_prompt = "testuser@all (1)[f:5]$ "
    assert console_cli.prompt == stringc(expected_prompt, console_cli.NORMAL_PROMPT, wrap_nonvisible_chars=True)

def test_set_prompt_become_root(monkeypatch, console_cli):
    monkeypatch.setattr(getpass, 'getuser', lambda: 'testuser')
    console_cli.remote_user = None
    console_cli.cwd = 'all'
    console_cli.forks = 5
    console_cli.become = True
    console_cli.become_user = 'root'
    
    console_cli.set_prompt()
    
    expected_prompt = "testuser@all (1)[f:5]# "
    assert console_cli.prompt == stringc(expected_prompt, C.COLOR_ERROR, wrap_nonvisible_chars=True)

def test_set_prompt_become_non_root(monkeypatch, console_cli):
    monkeypatch.setattr(getpass, 'getuser', lambda: 'testuser')
    console_cli.remote_user = None
    console_cli.cwd = 'all'
    console_cli.forks = 5
    console_cli.become = True
    console_cli.become_user = 'nonroot'
    
    console_cli.set_prompt()
    
    expected_prompt = "testuser@all (1)[f:5]$ "
    assert console_cli.prompt == stringc(expected_prompt, console_cli.NORMAL_PROMPT, wrap_nonvisible_chars=True)
