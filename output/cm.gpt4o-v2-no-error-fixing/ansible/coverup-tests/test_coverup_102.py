# file: lib/ansible/inventory/manager.py:143-167
# asked: {"lines": [143, 146, 147, 150, 151, 154, 155, 158, 159, 160, 161, 163, 166, 167], "branches": [[158, 159], [158, 160], [160, 161], [160, 163], [166, 0], [166, 167]]}
# gained: {"lines": [143, 146, 147, 150, 151, 154, 155, 158, 159, 160, 161, 163, 166, 167], "branches": [[158, 159], [158, 160], [160, 161], [160, 163], [166, 0], [166, 167]]}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from unittest.mock import patch

@pytest.fixture
def loader():
    return DataLoader()

def test_inventory_manager_no_sources(loader):
    with patch.object(InventoryManager, 'parse_sources') as mock_parse_sources:
        inv_mgr = InventoryManager(loader)
        assert inv_mgr._sources == []
        mock_parse_sources.assert_called_once_with(cache=True)

def test_inventory_manager_with_string_source(loader):
    with patch.object(InventoryManager, 'parse_sources') as mock_parse_sources:
        inv_mgr = InventoryManager(loader, sources='localhost')
        assert inv_mgr._sources == ['localhost']
        mock_parse_sources.assert_called_once_with(cache=True)

def test_inventory_manager_with_list_sources(loader):
    with patch.object(InventoryManager, 'parse_sources') as mock_parse_sources:
        inv_mgr = InventoryManager(loader, sources=['localhost', '127.0.0.1'])
        assert inv_mgr._sources == ['localhost', '127.0.0.1']
        mock_parse_sources.assert_called_once_with(cache=True)

def test_inventory_manager_no_parse(loader):
    with patch.object(InventoryManager, 'parse_sources') as mock_parse_sources:
        inv_mgr = InventoryManager(loader, parse=False)
        assert inv_mgr._sources == []
        mock_parse_sources.assert_not_called()
