# file: lib/ansible/cli/console.py:420-429
# asked: {"lines": [421, 422, 424, 425, 427, 429], "branches": [[424, 425], [424, 427]]}
# gained: {"lines": [421, 422, 424, 425, 427, 429], "branches": [[424, 425], [424, 427]]}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils._text import to_native
from ansible.cli.console import ConsoleCLI

class MockHost:
    def __init__(self, name):
        self.name = name

class MockInventory:
    def list_hosts(self, cwd):
        if cwd == 'group1':
            return [MockHost('host1'), MockHost('host2')]
        return []

class MockCLI(ConsoleCLI):
    def __init__(self, *args, **kwargs):
        self.cwd = 'group1'
        self.hosts = ['host1', 'host2']
        self.groups = ['group1', 'group2']
        self.inventory = MockInventory()

@pytest.fixture
def console_cli():
    return MockCLI([])

def test_complete_cd_all(console_cli):
    console_cli.cwd = 'all'
    completions = console_cli.complete_cd('ho', 'cd ho', 3, 5)
    assert completions == ['host1', 'host2']

def test_complete_cd_group(console_cli):
    console_cli.cwd = 'group1'
    completions = console_cli.complete_cd('ho', 'cd ho', 3, 5)
    assert completions == ['host1', 'host2']

def test_complete_cd_no_match(console_cli):
    console_cli.cwd = 'group1'
    completions = console_cli.complete_cd('no_match', 'cd no_match', 3, 11)
    assert completions == []
