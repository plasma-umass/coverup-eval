# file: lib/ansible/inventory/manager.py:181-182
# asked: {"lines": [181, 182], "branches": []}
# gained: {"lines": [181, 182], "branches": []}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager(mocker):
    mock_inventory_data = mocker.patch('ansible.inventory.manager.InventoryData', autospec=True)
    mock_inventory_data_instance = mock_inventory_data.return_value
    mock_inventory_data_instance.groups = {}
    mock_inventory_data_instance.hosts = {}
    loader = mocker.Mock()
    return InventoryManager(loader)

def test_add_host(inventory_manager):
    host = 'test_host'
    group = 'test_group'
    port = 1234

    inventory_manager.add_host(host, group, port)

    inventory_manager._inventory.add_host.assert_called_once_with(host, group, port)
