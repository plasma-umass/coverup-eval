# file lib/ansible/plugins/inventory/yaml.py:87-94
# lines []
# branches ['92->94']

import os
import pytest
from ansible.plugins.inventory.yaml import InventoryModule

# Assuming the existence of a BaseFileInventoryPlugin mock
class MockBaseFileInventoryPlugin:
    def verify_file(self, path):
        return True

# Assuming the existence of a mock for the get_option method
def mock_get_option(self, option):
    if option == 'yaml_extensions':
        return ['.yml', '.yaml']

# Test function to cover the missing branch
def test_inventory_module_verify_file_with_no_extension(mocker, tmp_path):
    # Setup the mock for the base class and the get_option method
    mocker.patch('ansible.plugins.inventory.yaml.BaseFileInventoryPlugin', new=MockBaseFileInventoryPlugin)
    mocker.patch('ansible.plugins.inventory.yaml.InventoryModule.get_option', new=mock_get_option)

    # Create a temporary file with no extension
    temp_file = tmp_path / "testfile"
    temp_file.touch()

    # Instantiate the InventoryModule
    inventory_module = InventoryModule()

    # Assert that verify_file returns True for a file with no extension
    assert inventory_module.verify_file(str(temp_file)) == True

# Test function to cover the missing branch with an extension that is not in yaml_extensions
def test_inventory_module_verify_file_with_unexpected_extension(mocker, tmp_path):
    # Setup the mock for the base class and the get_option method
    mocker.patch('ansible.plugins.inventory.yaml.BaseFileInventoryPlugin', new=MockBaseFileInventoryPlugin)
    mocker.patch('ansible.plugins.inventory.yaml.InventoryModule.get_option', new=mock_get_option)

    # Create a temporary file with an extension that is not in yaml_extensions
    temp_file = tmp_path / "testfile.unexpected"
    temp_file.touch()

    # Instantiate the InventoryModule
    inventory_module = InventoryModule()

    # Assert that verify_file returns False for a file with an extension that is not in yaml_extensions
    assert inventory_module.verify_file(str(temp_file)) == False
