# file: lib/ansible/cli/inventory.py:100-122
# asked: {"lines": [100, 101, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 120, 122], "branches": [[108, 109], [108, 111], [109, 108], [109, 110], [111, 112], [111, 113], [113, 114], [113, 117], [117, 118], [117, 120]]}
# gained: {"lines": [100, 101, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 120, 122], "branches": [[108, 109], [108, 111], [109, 108], [109, 110], [111, 112], [111, 113], [113, 114], [113, 117], [117, 118], [117, 120]]}

import pytest
from ansible.errors import AnsibleOptionsError
from ansible.cli.inventory import InventoryCLI
from unittest.mock import Mock

class MockOptions:
    def __init__(self, verbosity=None, list=None, host=None, graph=None, args=None):
        self.verbosity = verbosity
        self.list = list
        self.host = host
        self.graph = graph
        self.args = args

@pytest.fixture
def mock_options():
    return MockOptions()

@pytest.fixture
def cli(monkeypatch):
    cli_instance = InventoryCLI(args=['dummy_arg'])
    mock_parser = Mock()
    mock_parser.prog = 'ansible-inventory'
    monkeypatch.setattr(cli_instance, 'parser', mock_parser)
    return cli_instance

def test_post_process_args_no_action_selected(mock_options, cli):
    mock_options.list = False
    mock_options.host = False
    mock_options.graph = False
    
    with pytest.raises(AnsibleOptionsError, match="No action selected, at least one of --host, --graph or --list needs to be specified."):
        cli.post_process_args(mock_options)

def test_post_process_args_conflicting_options(mock_options, cli):
    mock_options.list = True
    mock_options.host = True
    mock_options.graph = False
    
    with pytest.raises(AnsibleOptionsError, match="Conflicting options used, only one of --host, --graph or --list can be used at the same time."):
        cli.post_process_args(mock_options)

def test_post_process_args_set_pattern_to_args(mock_options, cli):
    mock_options.list = True
    mock_options.host = False
    mock_options.graph = False
    mock_options.args = 'some_pattern'
    
    options = cli.post_process_args(mock_options)
    assert options.pattern == 'some_pattern'

def test_post_process_args_set_pattern_to_all(mock_options, cli):
    mock_options.list = True
    mock_options.host = False
    mock_options.graph = False
    mock_options.args = None
    
    options = cli.post_process_args(mock_options)
    assert options.pattern == 'all'

def test_post_process_args_set_verbosity(mock_options, cli, monkeypatch):
    mock_options.list = True
    mock_options.host = False
    mock_options.graph = False
    mock_options.verbosity = 3
    
    mock_display = Mock()
    monkeypatch.setattr("ansible.cli.inventory.display", mock_display)
    
    cli.post_process_args(mock_options)
    assert mock_display.verbosity == 3
