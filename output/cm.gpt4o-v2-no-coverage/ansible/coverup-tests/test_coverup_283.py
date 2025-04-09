# file: lib/ansible/inventory/manager.py:197-213
# asked: {"lines": [197, 200, 202, 203, 204, 205, 206, 208, 210, 211, 213], "branches": [[203, 204], [203, 210], [205, 206], [205, 208], [210, 211], [210, 213]]}
# gained: {"lines": [197, 200, 202, 203, 204, 205, 206, 208, 210, 211, 213], "branches": [[203, 204], [203, 210], [205, 206], [205, 208], [210, 211], [210, 213]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.inventory.manager.display')

@pytest.fixture
def mock_constants(mocker):
    return mocker.patch('ansible.inventory.manager.C')

@pytest.fixture
def mock_inventory_loader(mocker):
    return mocker.patch('ansible.inventory.manager.inventory_loader')

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_inventory_data(mocker):
    return mocker.patch('ansible.inventory.manager.InventoryData')

def test_fetch_inventory_plugins_success(mock_display, mock_constants, mock_inventory_loader, mock_loader, mock_inventory_data):
    mock_constants.INVENTORY_ENABLED = ['plugin1', 'plugin2']
    mock_plugin = MagicMock()
    mock_inventory_loader.get.side_effect = [mock_plugin, mock_plugin]

    manager = InventoryManager(loader=mock_loader, sources=[], parse=False)
    plugins = manager._fetch_inventory_plugins()

    assert plugins == [mock_plugin, mock_plugin]
    mock_display.vvvv.assert_called_once_with('setting up inventory plugins')
    mock_display.warning.assert_not_called()

def test_fetch_inventory_plugins_partial_success(mock_display, mock_constants, mock_inventory_loader, mock_loader, mock_inventory_data):
    mock_constants.INVENTORY_ENABLED = ['plugin1', 'plugin2']
    mock_plugin = MagicMock()
    mock_inventory_loader.get.side_effect = [mock_plugin, None]

    manager = InventoryManager(loader=mock_loader, sources=[], parse=False)
    plugins = manager._fetch_inventory_plugins()

    assert plugins == [mock_plugin]
    mock_display.vvvv.assert_called_once_with('setting up inventory plugins')
    mock_display.warning.assert_called_once_with('Failed to load inventory plugin, skipping plugin2')

def test_fetch_inventory_plugins_failure(mock_display, mock_constants, mock_inventory_loader, mock_loader, mock_inventory_data):
    mock_constants.INVENTORY_ENABLED = ['plugin1', 'plugin2']
    mock_inventory_loader.get.side_effect = [None, None]

    manager = InventoryManager(loader=mock_loader, sources=[], parse=False)
    with pytest.raises(AnsibleError, match="No inventory plugins available to generate inventory, make sure you have at least one whitelisted."):
        manager._fetch_inventory_plugins()

    mock_display.vvvv.assert_called_once_with('setting up inventory plugins')
    assert mock_display.warning.call_count == 2
    mock_display.warning.assert_any_call('Failed to load inventory plugin, skipping plugin1')
    mock_display.warning.assert_any_call('Failed to load inventory plugin, skipping plugin2')
