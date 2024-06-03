# file lib/ansible/inventory/manager.py:143-167
# lines [143, 146, 147, 150, 151, 154, 155, 158, 159, 160, 161, 163, 166, 167]
# branches ['158->159', '158->160', '160->161', '160->163', '166->exit', '166->167']

import pytest
from unittest.mock import Mock, patch
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData

@pytest.fixture
def mock_loader():
    return Mock()

@pytest.fixture
def mock_inventory_data():
    with patch('ansible.inventory.manager.InventoryData', autospec=True) as mock_inventory_data:
        yield mock_inventory_data

def test_inventory_manager_init_no_sources(mock_loader, mock_inventory_data):
    manager = InventoryManager(mock_loader, sources=None, parse=False)
    assert manager._sources == []
    assert manager._loader == mock_loader
    assert isinstance(manager._inventory, InventoryData)
    assert manager._restriction is None
    assert manager._subset is None
    assert manager._hosts_patterns_cache == {}
    assert manager._pattern_cache == {}

def test_inventory_manager_init_with_string_source(mock_loader, mock_inventory_data):
    manager = InventoryManager(mock_loader, sources='localhost', parse=False)
    assert manager._sources == ['localhost']
    assert manager._loader == mock_loader
    assert isinstance(manager._inventory, InventoryData)
    assert manager._restriction is None
    assert manager._subset is None
    assert manager._hosts_patterns_cache == {}
    assert manager._pattern_cache == {}

def test_inventory_manager_init_with_list_sources(mock_loader, mock_inventory_data):
    sources = ['localhost', 'remotehost']
    manager = InventoryManager(mock_loader, sources=sources, parse=False)
    assert manager._sources == sources
    assert manager._loader == mock_loader
    assert isinstance(manager._inventory, InventoryData)
    assert manager._restriction is None
    assert manager._subset is None
    assert manager._hosts_patterns_cache == {}
    assert manager._pattern_cache == {}

def test_inventory_manager_init_with_parse(mock_loader, mock_inventory_data):
    with patch.object(InventoryManager, 'parse_sources', autospec=True) as mock_parse_sources:
        manager = InventoryManager(mock_loader, sources=None, parse=True)
        mock_parse_sources.assert_called_once_with(manager, cache=True)
