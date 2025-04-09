# file lib/ansible/plugins/inventory/toml.py:226-247
# lines [246, 247]
# branches ['243->246', '246->exit', '246->247']

import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.toml import InventoryModule
from unittest.mock import MagicMock, patch

# Create a test function to cover lines 246-247
def test_parse_group_called():
    with patch('ansible.plugins.inventory.toml.HAS_TOML', True):
        # Mock the necessary components
        inventory = MagicMock()
        loader = MagicMock()
        path = 'dummy_path'
        inventory_module = InventoryModule()

        # Mock the _load_file method to return a dict with a group
        data_with_group = {'group1': {'hosts': ['host1', 'host2']}}
        inventory_module._load_file = MagicMock(return_value=data_with_group)

        # Mock the _parse_group method to check if it's called
        inventory_module._parse_group = MagicMock()

        # Mock the set_options method to avoid AttributeError
        inventory_module.set_options = MagicMock()

        # Call the parse method which should trigger _parse_group
        inventory_module.parse(inventory, loader, path)

        # Assert _parse_group was called with the correct arguments
        inventory_module._parse_group.assert_called_once_with('group1', data_with_group['group1'])

# Create a test function to cover the AnsibleParserError for empty data
def test_parse_empty_toml_file():
    with patch('ansible.plugins.inventory.toml.HAS_TOML', True):
        inventory = MagicMock()
        loader = MagicMock()
        path = 'dummy_path'
        inventory_module = InventoryModule()

        # Mock the _load_file method to return an empty dict
        inventory_module._load_file = MagicMock(return_value={})

        # Mock the set_options method to avoid AttributeError
        inventory_module.set_options = MagicMock()

        # Call the parse method and expect an AnsibleParserError
        with pytest.raises(AnsibleParserError) as excinfo:
            inventory_module.parse(inventory, loader, path)

        # Assert the exception message is correct
        assert str(excinfo.value) == 'Parsed empty TOML file'
