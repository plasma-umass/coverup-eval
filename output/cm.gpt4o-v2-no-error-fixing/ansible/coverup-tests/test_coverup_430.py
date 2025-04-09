# file: lib/ansible/cli/inventory.py:52-57
# asked: {"lines": [52, 54, 55, 56, 57], "branches": []}
# gained: {"lines": [52, 54, 55, 56, 57], "branches": []}

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.cli import CLI

def test_inventory_cli_init():
    args = ["arg1", "arg2"]
    cli = InventoryCLI(args)
    
    assert cli.args == args
    assert cli.vm is None
    assert cli.loader is None
    assert cli.inventory is None

def test_inventory_cli_init_no_args():
    with pytest.raises(ValueError, match="A non-empty list for args is required"):
        InventoryCLI([])

@pytest.fixture
def mock_cli_init(mocker):
    return mocker.patch('ansible.cli.CLI.__init__', return_value=None)

def test_inventory_cli_init_with_mock(mock_cli_init):
    args = ["arg1", "arg2"]
    cli = InventoryCLI(args)
    
    mock_cli_init.assert_called_once_with(args)
    assert cli.vm is None
    assert cli.loader is None
    assert cli.inventory is None
