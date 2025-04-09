# file lib/ansible/inventory/data.py:36-41
# lines [36, 37]
# branches []

import pytest
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_data():
    return InventoryData()

def test_inventory_data_initialization(inventory_data):
    assert isinstance(inventory_data, InventoryData)

# Clean up after the test
def test_inventory_data_cleanup(mocker):
    mocker.patch('ansible.inventory.data.InventoryData', autospec=True)
    inventory_data = InventoryData()
    assert isinstance(inventory_data, InventoryData)
    del inventory_data
