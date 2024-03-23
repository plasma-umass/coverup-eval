# file lib/ansible/plugins/inventory/yaml.py:87-94
# lines [87, 89, 90, 91, 92, 93, 94]
# branches ['90->91', '90->94', '92->93', '92->94']

import os
import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

# Mocking the BaseFileInventoryPlugin to control the behavior of verify_file
class MockedBaseFileInventoryPlugin(BaseFileInventoryPlugin):
    def verify_file(self, path):
        return True

# Test function to cover the missing lines/branches in InventoryModule.verify_file
def test_inventory_module_verify_file(mocker, tmp_path):
    # Setup: Create a temporary YAML file with a custom extension
    custom_yaml_extension = '.customyaml'
    temp_yaml_file = tmp_path / f"inventory{custom_yaml_extension}"
    temp_yaml_file.touch()

    # Mock the get_option method to return the custom extension
    mocker.patch.object(InventoryModule, 'get_option', return_value=[custom_yaml_extension])

    # Mock the super() call to return our mocked base plugin
    mocker.patch('ansible.plugins.inventory.yaml.super', return_value=MockedBaseFileInventoryPlugin())

    # Instantiate the InventoryModule
    inventory_module = InventoryModule()

    # Assertion: verify_file should return True for a file with the custom extension
    assert inventory_module.verify_file(str(temp_yaml_file)) is True

    # Cleanup: No cleanup needed as we are using pytest's tmp_path fixture
