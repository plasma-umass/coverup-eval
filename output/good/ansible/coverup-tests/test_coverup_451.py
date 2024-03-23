# file lib/ansible/plugins/inventory/toml.py:249-254
# lines [249, 250, 251, 252, 253, 254]
# branches ['250->251', '250->254', '252->253', '252->254']

import os
import pytest
from ansible.plugins.inventory.toml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

# Mocking the BaseFileInventoryPlugin to control the behavior of verify_file
class MockedBaseFileInventoryPlugin(BaseFileInventoryPlugin):
    def verify_file(self, path):
        return True

# Test function to cover the missing lines/branches in the InventoryModule.verify_file method
def test_inventory_module_verify_file_with_toml_extension(mocker, tmp_path):
    # Setup: Create a temporary .toml file
    toml_file = tmp_path / "test_inventory.toml"
    toml_file.touch()

    # Mock the super() call to return True
    mocker.patch.object(BaseFileInventoryPlugin, 'verify_file', return_value=True)

    # Instantiate the InventoryModule
    inventory_module = InventoryModule()

    # Assert that verify_file returns True for a .toml file
    assert inventory_module.verify_file(str(toml_file)) is True

    # Cleanup: Remove the temporary .toml file
    toml_file.unlink()

def test_inventory_module_verify_file_with_non_toml_extension(mocker, tmp_path):
    # Setup: Create a temporary non-.toml file
    non_toml_file = tmp_path / "test_inventory.txt"
    non_toml_file.touch()

    # Mock the super() call to return True
    mocker.patch.object(BaseFileInventoryPlugin, 'verify_file', return_value=True)

    # Instantiate the InventoryModule
    inventory_module = InventoryModule()

    # Assert that verify_file returns False for a non-.toml file
    assert inventory_module.verify_file(str(non_toml_file)) is False

    # Cleanup: Remove the temporary non-.toml file
    non_toml_file.unlink()
