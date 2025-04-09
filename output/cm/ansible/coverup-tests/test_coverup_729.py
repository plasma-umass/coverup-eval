# file lib/ansible/inventory/manager.py:177-179
# lines [177, 178, 179]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

# Mocking the InventoryData class
class MockInventoryData(InventoryData):
    def __init__(self):
        self.hosts = {'localhost': None}

@pytest.fixture
def inventory_manager(mocker):
    # Mock the InventoryManager's __init__ to not require any parameters
    mocker.patch.object(InventoryManager, '__init__', return_value=None)
    inventory_manager = InventoryManager()
    inventory_manager._inventory = MockInventoryData()
    return inventory_manager

def test_inventory_manager_hosts_property(inventory_manager):
    # Test the hosts property
    assert 'localhost' in inventory_manager.hosts
    assert inventory_manager.hosts['localhost'] is None

    # Cleanup is handled by the fixture scope, no other tests will be affected
