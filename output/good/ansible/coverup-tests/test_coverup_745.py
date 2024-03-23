# file lib/ansible/inventory/manager.py:173-175
# lines [173, 174, 175]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

# Mock class to simulate the InventoryData behavior
class MockInventoryData(InventoryData):
    def __init__(self):
        super(MockInventoryData, self).__init__()
        self.groups = {'all': 'mock_group'}

# Test function to cover the 'groups' property
def test_inventory_manager_groups_property(mocker):
    # Setup the mock for InventoryData
    inventory_manager = InventoryManager(loader=None, sources=[])
    inventory_manager._inventory = MockInventoryData()

    # Assert that accessing the 'groups' property returns the correct data
    assert inventory_manager.groups == {'all': 'mock_group'}

    # No need to patch or cleanup since we're directly assigning the mock object
