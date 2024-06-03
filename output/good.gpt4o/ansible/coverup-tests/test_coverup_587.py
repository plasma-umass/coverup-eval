# file lib/ansible/cli/inventory.py:52-57
# lines [52, 54, 55, 56, 57]
# branches []

import pytest
from ansible.cli.inventory import InventoryCLI

def test_inventory_cli_initialization():
    args = ['arg1', 'arg2']
    cli = InventoryCLI(args)
    
    assert cli.vm is None
    assert cli.loader is None
    assert cli.inventory is None
    assert cli.args == args
