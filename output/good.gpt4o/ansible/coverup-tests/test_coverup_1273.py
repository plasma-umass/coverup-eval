# file lib/ansible/cli/inventory.py:233-235
# lines [234, 235]
# branches []

import pytest
from unittest.mock import MagicMock

def test_get_group_executes_missing_lines(mocker):
    from ansible.cli.inventory import InventoryCLI

    # Mock the inventory and groups
    mock_inventory = MagicMock()
    mock_groups = {'existing_group': 'group_object'}
    mock_inventory.groups = mock_groups

    # Create an instance of InventoryCLI and set the inventory attribute
    cli_instance = InventoryCLI(args=['test'])
    cli_instance.inventory = mock_inventory

    # Test with a group that exists
    group_name = 'existing_group'
    result = cli_instance._get_group(group_name)
    assert result == 'group_object'

    # Test with a group that does not exist
    group_name = 'non_existing_group'
    result = cli_instance._get_group(group_name)
    assert result is None
