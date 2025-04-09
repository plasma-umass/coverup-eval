# file: lib/ansible/plugins/inventory/ini.py:95-100
# asked: {"lines": [95, 97, 99, 100], "branches": []}
# gained: {"lines": [95, 97, 99, 100], "branches": []}

import pytest
from ansible.plugins.inventory.ini import InventoryModule

def test_inventory_module_init():
    inventory_module = InventoryModule()
    
    assert isinstance(inventory_module, InventoryModule)
    assert inventory_module.patterns == {}
    assert inventory_module._filename is None
