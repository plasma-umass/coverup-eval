# file: lib/ansible/inventory/manager.py:646-648
# asked: {"lines": [646, 648], "branches": []}
# gained: {"lines": [646, 648], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader

def test_remove_restriction():
    loader = DataLoader()
    inventory_manager = InventoryManager(loader)
    inventory_manager._restriction = "some_restriction"
    
    inventory_manager.remove_restriction()
    
    assert inventory_manager._restriction is None
