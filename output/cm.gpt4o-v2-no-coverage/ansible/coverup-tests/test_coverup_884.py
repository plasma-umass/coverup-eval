# file: lib/ansible/inventory/manager.py:194-195
# asked: {"lines": [194, 195], "branches": []}
# gained: {"lines": [194, 195], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    sources = None
    return InventoryManager(loader, sources)

def test_get_host(inventory_manager, mocker):
    mock_inventory = mocker.patch.object(inventory_manager, '_inventory', autospec=True)
    mock_inventory.get_host.return_value = 'mock_host'

    hostname = 'test_host'
    result = inventory_manager.get_host(hostname)

    mock_inventory.get_host.assert_called_once_with(hostname)
    assert result == 'mock_host'
