# file lib/ansible/plugins/inventory/constructed.py:98-102
# lines [98, 100, 102]
# branches []

import pytest
from ansible.plugins.inventory.constructed import InventoryModule
from ansible.plugins.inventory.constructed import FactCache
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable

def test_inventory_module_initialization(mocker):
    # Mock the FactCache to ensure it is called correctly
    mock_fact_cache = mocker.patch('ansible.plugins.inventory.constructed.FactCache', autospec=True)
    
    # Initialize the InventoryModule
    inventory_module = InventoryModule()
    
    # Assertions to verify the correct initialization
    assert isinstance(inventory_module, BaseInventoryPlugin)
    assert isinstance(inventory_module, Constructable)
    mock_fact_cache.assert_called_once()
    assert isinstance(inventory_module._cache, FactCache)
