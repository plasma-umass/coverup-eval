# file: lib/ansible/inventory/manager.py:601-603
# asked: {"lines": [601, 603], "branches": []}
# gained: {"lines": [601, 603], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager

class MockInventory:
    def __init__(self, groups):
        self.groups = groups

@pytest.fixture
def inventory_manager(monkeypatch):
    def mock_init(self, *args, **kwargs):
        self._inventory = MockInventory(groups={'group1': {}, 'group2': {}})
    monkeypatch.setattr(InventoryManager, '__init__', mock_init)
    return InventoryManager()

def test_list_groups(inventory_manager):
    groups = inventory_manager.list_groups()
    assert groups == ['group1', 'group2']
