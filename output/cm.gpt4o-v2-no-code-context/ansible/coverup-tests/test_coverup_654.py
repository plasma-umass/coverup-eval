# file: lib/ansible/inventory/manager.py:169-171
# asked: {"lines": [169, 170, 171], "branches": []}
# gained: {"lines": [169, 170, 171], "branches": []}

import pytest
from unittest.mock import MagicMock

class MockInventory:
    @property
    def localhost(self):
        return "localhost"

@pytest.fixture
def inventory_manager():
    from ansible.inventory.manager import InventoryManager
    loader = MagicMock()
    sources = MagicMock()
    manager = InventoryManager(loader, sources)
    manager._inventory = MockInventory()
    return manager

def test_localhost_property(inventory_manager):
    assert inventory_manager.localhost == "localhost"
