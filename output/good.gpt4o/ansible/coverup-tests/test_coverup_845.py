# file lib/ansible/plugins/inventory/yaml.py:79-82
# lines [79, 81]
# branches []

import pytest
from ansible.plugins.inventory.yaml import InventoryModule
from ansible.plugins.inventory import BaseFileInventoryPlugin

def test_inventory_module_name():
    # Ensure the InventoryModule class is correctly inheriting from BaseFileInventoryPlugin
    assert issubclass(InventoryModule, BaseFileInventoryPlugin)
    
    # Ensure the NAME attribute is correctly set
    assert InventoryModule.NAME == 'yaml'
