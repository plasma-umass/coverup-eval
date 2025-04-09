# file lib/ansible/plugins/inventory/toml.py:152-154
# lines [152, 153]
# branches []

import pytest
from ansible.plugins.inventory.toml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

def test_inventory_module_name():
    # Ensure the InventoryModule class is correctly inheriting from BaseFileInventoryPlugin
    assert issubclass(InventoryModule, BaseFileInventoryPlugin)
    
    # Ensure the NAME attribute is correctly set
    assert InventoryModule.NAME == 'toml'
