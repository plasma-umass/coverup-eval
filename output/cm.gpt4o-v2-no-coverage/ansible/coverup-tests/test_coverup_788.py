# file: lib/ansible/cli/inventory.py:233-235
# asked: {"lines": [233, 234, 235], "branches": []}
# gained: {"lines": [233, 234, 235], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.inventory import InventoryCLI

@pytest.fixture
def inventory_cli():
    args = MagicMock()
    cli = InventoryCLI(args)
    cli.inventory = MagicMock()
    cli.inventory.groups = {
        'group1': 'Group 1',
        'group2': 'Group 2'
    }
    return cli

def test_get_group_existing(inventory_cli):
    group = inventory_cli._get_group('group1')
    assert group == 'Group 1'

def test_get_group_non_existing(inventory_cli):
    group = inventory_cli._get_group('non_existing_group')
    assert group is None
