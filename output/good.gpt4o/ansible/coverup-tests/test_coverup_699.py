# file lib/ansible/plugins/inventory/constructed.py:93-97
# lines [93, 94, 96]
# branches []

import pytest
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_inventory_module_initialization(inventory_module):
    assert isinstance(inventory_module, BaseInventoryPlugin)
    assert isinstance(inventory_module, Constructable)
    assert inventory_module.NAME == 'constructed'
