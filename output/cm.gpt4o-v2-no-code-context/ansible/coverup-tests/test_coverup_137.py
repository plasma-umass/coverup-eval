# file: lib/ansible/inventory/manager.py:143-167
# asked: {"lines": [143, 146, 147, 150, 151, 154, 155, 158, 159, 160, 161, 163, 166, 167], "branches": [[158, 159], [158, 160], [160, 161], [160, 163], [166, 0], [166, 167]]}
# gained: {"lines": [143, 146, 147, 150, 151, 154, 155, 158, 159, 160, 161, 163, 166, 167], "branches": [[158, 159], [158, 160], [160, 161], [160, 163], [166, 0], [166, 167]]}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.data import InventoryData
from unittest.mock import patch

@pytest.fixture
def mock_loader():
    return DataLoader()

def test_inventory_manager_no_sources(mock_loader):
    manager = InventoryManager(loader=mock_loader, sources=None, parse=False)
    assert manager._sources == []

def test_inventory_manager_string_sources(mock_loader):
    manager = InventoryManager(loader=mock_loader, sources='localhost', parse=False)
    assert manager._sources == ['localhost']

def test_inventory_manager_list_sources(mock_loader):
    manager = InventoryManager(loader=mock_loader, sources=['localhost', 'remotehost'], parse=False)
    assert manager._sources == ['localhost', 'remotehost']

@patch.object(InventoryManager, 'parse_sources')
def test_inventory_manager_parse_sources(mock_parse_sources, mock_loader):
    manager = InventoryManager(loader=mock_loader, sources=None, parse=True)
    mock_parse_sources.assert_called_once_with(cache=True)
