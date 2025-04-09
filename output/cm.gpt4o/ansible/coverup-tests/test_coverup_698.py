# file lib/ansible/plugins/inventory/generator.py:83-87
# lines [83, 84, 86]
# branches []

import pytest
from ansible.plugins.inventory.generator import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin

def test_inventory_module_initialization():
    # Test that InventoryModule is correctly initialized and is a subclass of BaseInventoryPlugin
    inventory_module = InventoryModule()
    assert isinstance(inventory_module, BaseInventoryPlugin)
    assert inventory_module.NAME == 'generator'
