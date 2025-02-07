# file: lib/ansible/cli/inventory.py:100-122
# asked: {"lines": [101, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 120, 122], "branches": [[108, 109], [108, 111], [109, 108], [109, 110], [111, 112], [111, 113], [113, 114], [113, 117], [117, 118], [117, 120]]}
# gained: {"lines": [101, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 120, 122], "branches": [[108, 109], [108, 111], [109, 108], [109, 110], [111, 112], [111, 113], [113, 114], [113, 117], [117, 118], [117, 120]]}

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.errors import AnsibleOptionsError
from unittest.mock import MagicMock

@pytest.fixture
def mock_display(monkeypatch):
    mock_display = MagicMock()
    monkeypatch.setattr("ansible.cli.inventory.display", mock_display)
    return mock_display

@pytest.fixture
def valid_args():
    return ['ansible-inventory', '--list']

def test_post_process_args_no_action_selected(mock_display, valid_args):
    cli = InventoryCLI(valid_args)
    cli.parser = MagicMock()
    cli.parser.prog = 'ansible-inventory'
    options = MagicMock()
    options.verbosity = 3
    options.list = False
    options.host = False
    options.graph = False
    options.args = None

    with pytest.raises(AnsibleOptionsError, match="No action selected, at least one of --host, --graph or --list needs to be specified."):
        cli.post_process_args(options)

def test_post_process_args_conflicting_options(mock_display, valid_args):
    cli = InventoryCLI(valid_args)
    cli.parser = MagicMock()
    cli.parser.prog = 'ansible-inventory'
    options = MagicMock()
    options.verbosity = 3
    options.list = True
    options.host = True
    options.graph = False
    options.args = None

    with pytest.raises(AnsibleOptionsError, match="Conflicting options used, only one of --host, --graph or --list can be used at the same time."):
        cli.post_process_args(options)

def test_post_process_args_set_pattern_from_args(mock_display, valid_args):
    cli = InventoryCLI(valid_args)
    cli.parser = MagicMock()
    cli.parser.prog = 'ansible-inventory'
    options = MagicMock()
    options.verbosity = 3
    options.list = True
    options.host = False
    options.graph = False
    options.args = 'some_pattern'

    result = cli.post_process_args(options)
    assert result.pattern == 'some_pattern'

def test_post_process_args_set_default_pattern(mock_display, valid_args):
    cli = InventoryCLI(valid_args)
    cli.parser = MagicMock()
    cli.parser.prog = 'ansible-inventory'
    options = MagicMock()
    options.verbosity = 3
    options.list = True
    options.host = False
    options.graph = False
    options.args = None

    result = cli.post_process_args(options)
    assert result.pattern == 'all'
