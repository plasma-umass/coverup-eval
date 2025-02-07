# file: lib/ansible/inventory/manager.py:143-167
# asked: {"lines": [143, 146, 147, 150, 151, 154, 155, 158, 159, 160, 161, 163, 166, 167], "branches": [[158, 159], [158, 160], [160, 161], [160, 163], [166, 0], [166, 167]]}
# gained: {"lines": [143, 146, 147, 150, 151, 154, 155, 158, 159, 160, 161, 163, 166, 167], "branches": [[158, 159], [158, 160], [160, 161], [160, 163], [166, 0], [166, 167]]}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible.inventory.data import InventoryData
from ansible.module_utils.six import string_types

class MockLoader:
    pass

@pytest.fixture
def mock_loader():
    return MockLoader()

def test_inventory_manager_init_no_sources(mock_loader, mocker):
    mock_parse_sources = mocker.patch.object(InventoryManager, 'parse_sources', return_value=None)
    
    manager = InventoryManager(mock_loader, sources=None, parse=True)
    
    assert manager._loader == mock_loader
    assert isinstance(manager._inventory, InventoryData)
    assert manager._restriction is None
    assert manager._subset is None
    assert manager._hosts_patterns_cache == {}
    assert manager._pattern_cache == {}
    assert manager._sources == []
    mock_parse_sources.assert_called_once_with(cache=True)

def test_inventory_manager_init_with_string_source(mock_loader, mocker):
    mock_parse_sources = mocker.patch.object(InventoryManager, 'parse_sources', return_value=None)
    
    manager = InventoryManager(mock_loader, sources='localhost', parse=True)
    
    assert manager._loader == mock_loader
    assert isinstance(manager._inventory, InventoryData)
    assert manager._restriction is None
    assert manager._subset is None
    assert manager._hosts_patterns_cache == {}
    assert manager._pattern_cache == {}
    assert manager._sources == ['localhost']
    mock_parse_sources.assert_called_once_with(cache=True)

def test_inventory_manager_init_with_list_sources(mock_loader, mocker):
    mock_parse_sources = mocker.patch.object(InventoryManager, 'parse_sources', return_value=None)
    
    manager = InventoryManager(mock_loader, sources=['localhost', 'remotehost'], parse=True)
    
    assert manager._loader == mock_loader
    assert isinstance(manager._inventory, InventoryData)
    assert manager._restriction is None
    assert manager._subset is None
    assert manager._hosts_patterns_cache == {}
    assert manager._pattern_cache == {}
    assert manager._sources == ['localhost', 'remotehost']
    mock_parse_sources.assert_called_once_with(cache=True)

def test_inventory_manager_init_no_parse(mock_loader, mocker):
    mock_parse_sources = mocker.patch.object(InventoryManager, 'parse_sources', return_value=None)
    
    manager = InventoryManager(mock_loader, sources=None, parse=False)
    
    assert manager._loader == mock_loader
    assert isinstance(manager._inventory, InventoryData)
    assert manager._restriction is None
    assert manager._subset is None
    assert manager._hosts_patterns_cache == {}
    assert manager._pattern_cache == {}
    assert manager._sources == []
    mock_parse_sources.assert_not_called()
