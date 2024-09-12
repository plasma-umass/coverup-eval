# file: lib/ansible/plugins/inventory/generator.py:88-90
# asked: {"lines": [88, 90], "branches": []}
# gained: {"lines": [88, 90], "branches": []}

import pytest
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.plugins.inventory.generator import InventoryModule

class TestInventoryModule:
    
    def test_init(self):
        # Create an instance of InventoryModule
        inventory_module = InventoryModule()
        
        # Assert that the instance is created and is an instance of InventoryModule
        assert isinstance(inventory_module, InventoryModule)
        
        # Assert that the instance is also an instance of BaseInventoryPlugin
        assert isinstance(inventory_module, BaseInventoryPlugin)
        
        # Assert that the _options attribute is initialized correctly
        assert inventory_module._options == {}
        
        # Assert that the inventory attribute is initialized correctly
        assert inventory_module.inventory is None
        
        # Assert that the _vars attribute is initialized correctly
        assert inventory_module._vars == {}
