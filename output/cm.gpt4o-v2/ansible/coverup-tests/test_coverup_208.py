# file: lib/ansible/inventory/manager.py:197-213
# asked: {"lines": [197, 200, 202, 203, 204, 205, 206, 208, 210, 211, 213], "branches": [[203, 204], [203, 210], [205, 206], [205, 208], [210, 211], [210, 213]]}
# gained: {"lines": [197, 200, 202, 203, 204, 205, 206, 208, 210, 211, 213], "branches": [[203, 204], [203, 210], [205, 206], [205, 208], [210, 211], [210, 213]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    return InventoryManager(loader)

def test_fetch_inventory_plugins_success(inventory_manager):
    with patch('ansible.inventory.manager.C.INVENTORY_ENABLED', ['plugin1', 'plugin2']), \
         patch('ansible.inventory.manager.inventory_loader.get', side_effect=[MagicMock(), MagicMock()]), \
         patch('ansible.inventory.manager.display.vvvv'), \
         patch('ansible.inventory.manager.display.warning') as mock_warning:
        
        plugins = inventory_manager._fetch_inventory_plugins()
        
        assert len(plugins) == 2
        mock_warning.assert_not_called()

def test_fetch_inventory_plugins_partial_success(inventory_manager):
    with patch('ansible.inventory.manager.C.INVENTORY_ENABLED', ['plugin1', 'plugin2']), \
         patch('ansible.inventory.manager.inventory_loader.get', side_effect=[MagicMock(), None]), \
         patch('ansible.inventory.manager.display.vvvv'), \
         patch('ansible.inventory.manager.display.warning') as mock_warning:
        
        plugins = inventory_manager._fetch_inventory_plugins()
        
        assert len(plugins) == 1
        mock_warning.assert_called_once_with('Failed to load inventory plugin, skipping plugin2')

def test_fetch_inventory_plugins_failure(inventory_manager):
    with patch('ansible.inventory.manager.C.INVENTORY_ENABLED', ['plugin1', 'plugin2']), \
         patch('ansible.inventory.manager.inventory_loader.get', return_value=None), \
         patch('ansible.inventory.manager.display.vvvv'), \
         patch('ansible.inventory.manager.display.warning') as mock_warning:
        
        with pytest.raises(AnsibleError, match="No inventory plugins available to generate inventory, make sure you have at least one whitelisted."):
            inventory_manager._fetch_inventory_plugins()
        
        mock_warning.assert_called_with('Failed to load inventory plugin, skipping plugin2')
