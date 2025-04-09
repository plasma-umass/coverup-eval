# file: lib/ansible/cli/inventory.py:100-122
# asked: {"lines": [101, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 120, 122], "branches": [[108, 109], [108, 111], [109, 108], [109, 110], [111, 112], [111, 113], [113, 114], [113, 117], [117, 118], [117, 120]]}
# gained: {"lines": [101, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 120, 122], "branches": [[108, 109], [108, 111], [109, 108], [109, 110], [111, 112], [111, 113], [113, 114], [113, 117], [117, 118], [117, 120]]}

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.errors import AnsibleOptionsError
from unittest.mock import MagicMock

class MockOptions:
    def __init__(self, verbosity=0, list=False, host=False, graph=False, args=None):
        self.verbosity = verbosity
        self.list = list
        self.host = host
        self.graph = graph
        self.args = args
        self.pattern = None

@pytest.fixture
def inventory_cli(monkeypatch):
    cli = InventoryCLI(['inventory'])
    mock_parser = MagicMock()
    mock_parser.prog = 'ansible-inventory'
    monkeypatch.setattr(cli, 'parser', mock_parser)
    return cli

def test_post_process_args_no_action_selected(inventory_cli):
    options = MockOptions()
    with pytest.raises(AnsibleOptionsError, match="No action selected, at least one of --host, --graph or --list needs to be specified."):
        inventory_cli.post_process_args(options)

def test_post_process_args_conflicting_options(inventory_cli):
    options = MockOptions(list=True, host=True)
    with pytest.raises(AnsibleOptionsError, match="Conflicting options used, only one of --host, --graph or --list can be used at the same time."):
        inventory_cli.post_process_args(options)

def test_post_process_args_default_pattern(inventory_cli):
    options = MockOptions(list=True)
    processed_options = inventory_cli.post_process_args(options)
    assert processed_options.pattern == 'all'

def test_post_process_args_with_args(inventory_cli):
    options = MockOptions(list=True, args='some_pattern')
    processed_options = inventory_cli.post_process_args(options)
    assert processed_options.pattern == 'some_pattern'

def test_post_process_args_verbosity(inventory_cli, monkeypatch):
    mock_display = MagicMock()
    monkeypatch.setattr('ansible.cli.inventory.display', mock_display)
    options = MockOptions(list=True, verbosity=3)
    inventory_cli.post_process_args(options)
    assert mock_display.verbosity == 3
