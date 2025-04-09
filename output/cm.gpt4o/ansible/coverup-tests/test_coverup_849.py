# file lib/ansible/plugins/inventory/generator.py:88-90
# lines [88, 90]
# branches []

import pytest
from ansible.plugins.inventory.generator import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin

def test_inventory_module_init(mocker):
    # Mock the BaseInventoryPlugin's __init__ method to ensure it is called
    mock_init = mocker.patch.object(BaseInventoryPlugin, '__init__', return_value=None)
    
    # Instantiate the InventoryModule
    inventory_module = InventoryModule()
    
    # Assert that the BaseInventoryPlugin's __init__ method was called
    mock_init.assert_called_once()
    
    # Assert that the inventory_module is an instance of InventoryModule
    assert isinstance(inventory_module, InventoryModule)
    
    # Assert that the inventory_module is also an instance of BaseInventoryPlugin
    assert isinstance(inventory_module, BaseInventoryPlugin)
