# file lib/ansible/plugins/inventory/constructed.py:104-113
# lines [106, 107, 108, 110, 111, 113]
# branches ['107->108', '107->113', '110->111', '110->113']

import os
import pytest
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.constants import YAML_FILENAME_EXTENSIONS as C_YAML_FILENAME_EXTENSIONS

# Test function to cover lines 106-113
def test_verify_file_with_yaml_extension(tmp_path, mocker):
    # Create a temporary YAML file
    yaml_file = tmp_path / "test_inventory.yaml"
    yaml_file.touch()

    # Create an instance of the InventoryModule
    inventory_module = InventoryModule()

    # Mock the super().verify_file method to return True for YAML files
    mocker.patch.object(BaseInventoryPlugin, 'verify_file', return_value=True)

    # Call the verify_file method with the path of the temporary YAML file
    result = inventory_module.verify_file(str(yaml_file))

    # Assert that the result is True, which means the file was verified successfully
    assert result == True

    # Clean up the temporary file
    yaml_file.unlink()

# Test function to cover lines 106-113 with a non-YAML file
def test_verify_file_with_non_yaml_extension(tmp_path, mocker):
    # Create a temporary non-YAML file
    non_yaml_file = tmp_path / "test_inventory.txt"
    non_yaml_file.touch()

    # Create an instance of the InventoryModule
    inventory_module = InventoryModule()

    # Mock the super().verify_file method to return True for non-YAML files
    mocker.patch.object(BaseInventoryPlugin, 'verify_file', return_value=True)

    # Call the verify_file method with the path of the temporary non-YAML file
    result = inventory_module.verify_file(str(non_yaml_file))

    # Assert that the result is False, which means the file was not verified successfully
    assert result == False

    # Clean up the temporary file
    non_yaml_file.unlink()
