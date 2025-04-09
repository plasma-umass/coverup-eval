# file: lib/ansible/plugins/inventory/yaml.py:83-85
# asked: {"lines": [83, 85], "branches": []}
# gained: {"lines": [83, 85], "branches": []}

import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

def test_inventory_module_init(mocker):
    # Mock the BaseFileInventoryPlugin's __init__ method to ensure it is called
    mock_init = mocker.patch.object(BaseFileInventoryPlugin, '__init__', return_value=None)
    
    # Instantiate the InventoryModule
    inventory_module = InventoryModule()
    
    # Assert that the BaseFileInventoryPlugin's __init__ method was called
    mock_init.assert_called_once()
    
    # Clean up by deleting the instance
    del inventory_module
