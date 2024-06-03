# file lib/ansible/cli/inventory.py:100-122
# lines [101, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 120, 122]
# branches ['108->109', '108->111', '109->108', '109->110', '111->112', '111->113', '113->114', '113->117', '117->118', '117->120']

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.errors import AnsibleOptionsError
from unittest.mock import MagicMock

class MockOptions:
    def __init__(self, list=False, host=False, graph=False, verbosity=0, args=None):
        self.list = list
        self.host = host
        self.graph = graph
        self.verbosity = verbosity
        self.args = args

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.cli.inventory.display')

@pytest.fixture
def inventory_cli(mocker):
    mock_args = MagicMock()
    mock_parser = MagicMock()
    mock_parser.prog = 'ansible-inventory'
    cli = InventoryCLI(mock_args)
    cli.parser = mock_parser
    return cli

def test_post_process_args_no_action_selected(mock_display, inventory_cli):
    options = MockOptions()
    with pytest.raises(AnsibleOptionsError, match="No action selected, at least one of --host, --graph or --list needs to be specified."):
        inventory_cli.post_process_args(options)

def test_post_process_args_conflicting_options(mock_display, inventory_cli):
    options = MockOptions(list=True, host=True)
    with pytest.raises(AnsibleOptionsError, match="Conflicting options used, only one of --host, --graph or --list can be used at the same time."):
        inventory_cli.post_process_args(options)

def test_post_process_args_default_pattern(mock_display, inventory_cli):
    options = MockOptions(list=True)
    processed_options = inventory_cli.post_process_args(options)
    assert processed_options.pattern == 'all'

def test_post_process_args_custom_pattern(mock_display, inventory_cli):
    options = MockOptions(list=True, args='custom_pattern')
    processed_options = inventory_cli.post_process_args(options)
    assert processed_options.pattern == 'custom_pattern'
