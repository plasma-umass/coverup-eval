# file lib/ansible/inventory/manager.py:187-188
# lines [187, 188]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData
from ansible.parsing.dataloader import DataLoader

# Mock class to simulate the behavior of the actual InventoryData
class MockInventoryData(InventoryData):
    def get_groups_dict(self):
        return {'all': {'hosts': ['host1', 'host2'], 'children': ['ungrouped']}}

@pytest.fixture
def inventory_manager(mocker):
    # Create an instance of InventoryManager with a mocked InventoryData
    loader = DataLoader()
    inventory_manager_instance = InventoryManager(loader=loader)
    mocker.patch.object(inventory_manager_instance, '_inventory', new_callable=lambda: MockInventoryData())
    return inventory_manager_instance

def test_get_groups_dict(inventory_manager):
    # Test the get_groups_dict method to ensure it returns the correct dictionary
    expected_groups_dict = {'all': {'hosts': ['host1', 'host2'], 'children': ['ungrouped']}}
    groups_dict = inventory_manager.get_groups_dict()
    assert groups_dict == expected_groups_dict, "The returned groups dictionary does not match the expected dictionary"

    # Cleanup is handled by the fixture's scope and pytest's garbage collection
