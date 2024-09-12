# file: lib/ansible/inventory/manager.py:169-171
# asked: {"lines": [169, 170, 171], "branches": []}
# gained: {"lines": [169, 170, 171], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    return InventoryManager(loader)

def test_localhost_property(inventory_manager):
    mock_localhost = MagicMock()
    inventory_manager._inventory.localhost = mock_localhost

    assert inventory_manager.localhost == mock_localhost
