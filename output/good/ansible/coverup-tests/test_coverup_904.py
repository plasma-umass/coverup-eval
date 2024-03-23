# file lib/ansible/inventory/manager.py:194-195
# lines [194, 195]
# branches []

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def inventory_manager(mocker):
    # Mock the DataLoader object
    loader = mocker.MagicMock(spec=DataLoader)
    # Mock the InventoryData object
    inventory_data = mocker.MagicMock(spec=InventoryData)
    # Create an instance of InventoryManager with the mocked DataLoader and InventoryData
    inventory_manager_instance = InventoryManager(loader=loader)
    inventory_manager_instance._inventory = inventory_data
    return inventory_manager_instance

def test_get_host(inventory_manager, mocker):
    # Mock the get_host method of the InventoryData object
    hostname = 'testhost'
    mock_host = mocker.MagicMock()
    inventory_manager._inventory.get_host.return_value = mock_host

    # Call the get_host method of the InventoryManager
    host = inventory_manager.get_host(hostname)

    # Assert that the InventoryData get_host method was called with the correct hostname
    inventory_manager._inventory.get_host.assert_called_once_with(hostname)

    # Assert that the return value is the mock host
    assert host == mock_host
