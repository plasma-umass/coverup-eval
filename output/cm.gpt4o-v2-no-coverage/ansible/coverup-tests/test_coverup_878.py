# file: lib/ansible/inventory/manager.py:181-182
# asked: {"lines": [181, 182], "branches": []}
# gained: {"lines": [181, 182], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager():
    loader = Mock()
    return InventoryManager(loader)

def test_add_host(inventory_manager, mocker):
    mock_inventory = mocker.patch.object(inventory_manager, '_inventory', autospec=True)
    host = 'test_host'
    group = 'test_group'
    port = 1234

    inventory_manager.add_host(host, group, port)

    mock_inventory.add_host.assert_called_once_with(host, group, port)
