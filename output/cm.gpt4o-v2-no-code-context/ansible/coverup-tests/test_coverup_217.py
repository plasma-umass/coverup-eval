# file: lib/ansible/inventory/manager.py:197-213
# asked: {"lines": [197, 200, 202, 203, 204, 205, 206, 208, 210, 211, 213], "branches": [[203, 204], [203, 210], [205, 206], [205, 208], [210, 211], [210, 213]]}
# gained: {"lines": [197, 200, 202, 203, 204, 205, 206, 208, 210, 211, 213], "branches": [[203, 204], [203, 210], [205, 206], [205, 208], [210, 211], [210, 213]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    mock_loader = MagicMock()
    return InventoryManager(loader=mock_loader)

def test_fetch_inventory_plugins_success(monkeypatch, inventory_manager):
    # Mocking the necessary components
    mock_display = MagicMock()
    mock_inventory_loader = MagicMock()
    mock_plugin = MagicMock()
    
    monkeypatch.setattr('ansible.inventory.manager.display', mock_display)
    monkeypatch.setattr('ansible.inventory.manager.inventory_loader', mock_inventory_loader)
    
    with patch('ansible.constants.INVENTORY_ENABLED', ['plugin1', 'plugin2']):
        mock_inventory_loader.get.side_effect = [mock_plugin, mock_plugin]
        
        plugins = inventory_manager._fetch_inventory_plugins()
        
        assert len(plugins) == 2
        mock_display.vvvv.assert_called_once_with('setting up inventory plugins')
        mock_inventory_loader.get.assert_any_call('plugin1')
        mock_inventory_loader.get.assert_any_call('plugin2')

def test_fetch_inventory_plugins_partial_failure(monkeypatch, inventory_manager):
    # Mocking the necessary components
    mock_display = MagicMock()
    mock_inventory_loader = MagicMock()
    mock_plugin = MagicMock()
    
    monkeypatch.setattr('ansible.inventory.manager.display', mock_display)
    monkeypatch.setattr('ansible.inventory.manager.inventory_loader', mock_inventory_loader)
    
    with patch('ansible.constants.INVENTORY_ENABLED', ['plugin1', 'plugin2']):
        mock_inventory_loader.get.side_effect = [mock_plugin, None]
        
        plugins = inventory_manager._fetch_inventory_plugins()
        
        assert len(plugins) == 1
        mock_display.vvvv.assert_called_once_with('setting up inventory plugins')
        mock_inventory_loader.get.assert_any_call('plugin1')
        mock_inventory_loader.get.assert_any_call('plugin2')
        mock_display.warning.assert_called_once_with('Failed to load inventory plugin, skipping plugin2')

def test_fetch_inventory_plugins_failure(monkeypatch, inventory_manager):
    # Mocking the necessary components
    mock_display = MagicMock()
    mock_inventory_loader = MagicMock()
    
    monkeypatch.setattr('ansible.inventory.manager.display', mock_display)
    monkeypatch.setattr('ansible.inventory.manager.inventory_loader', mock_inventory_loader)
    
    with patch('ansible.constants.INVENTORY_ENABLED', ['plugin1', 'plugin2']):
        mock_inventory_loader.get.side_effect = [None, None]
        
        with pytest.raises(AnsibleError, match="No inventory plugins available to generate inventory, make sure you have at least one whitelisted."):
            inventory_manager._fetch_inventory_plugins()
        
        mock_display.vvvv.assert_called_once_with('setting up inventory plugins')
        mock_inventory_loader.get.assert_any_call('plugin1')
        mock_inventory_loader.get.assert_any_call('plugin2')
        mock_display.warning.assert_any_call('Failed to load inventory plugin, skipping plugin1')
        mock_display.warning.assert_any_call('Failed to load inventory plugin, skipping plugin2')
