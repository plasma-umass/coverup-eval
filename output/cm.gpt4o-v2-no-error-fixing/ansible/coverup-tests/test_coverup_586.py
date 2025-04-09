# file: lib/ansible/inventory/manager.py:646-648
# asked: {"lines": [646, 648], "branches": []}
# gained: {"lines": [646, 648], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import MagicMock

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    return InventoryManager(loader)

def test_remove_restriction(inventory_manager):
    # Set a restriction first
    inventory_manager._restriction = "some_restriction"
    assert inventory_manager._restriction is not None

    # Remove the restriction
    inventory_manager.remove_restriction()

    # Verify the restriction is removed
    assert inventory_manager._restriction is None
