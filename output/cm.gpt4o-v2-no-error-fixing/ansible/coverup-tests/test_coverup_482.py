# file: lib/ansible/cli/inventory.py:233-235
# asked: {"lines": [233, 234, 235], "branches": []}
# gained: {"lines": [233, 234, 235], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.cli.inventory import InventoryCLI

@pytest.fixture
def inventory_cli():
    args = ['dummy_arg']
    cli = InventoryCLI(args)
    cli.inventory = MagicMock()
    return cli

def test_get_group_existing(inventory_cli):
    group_name = 'existing_group'
    expected_group = MagicMock()
    inventory_cli.inventory.groups.get.return_value = expected_group

    result = inventory_cli._get_group(group_name)

    assert result == expected_group
    inventory_cli.inventory.groups.get.assert_called_once_with(group_name)

def test_get_group_non_existing(inventory_cli):
    group_name = 'non_existing_group'
    inventory_cli.inventory.groups.get.return_value = None

    result = inventory_cli._get_group(group_name)

    assert result is None
    inventory_cli.inventory.groups.get.assert_called_once_with(group_name)
