# file lib/ansible/inventory/manager.py:215-241
# lines []
# branches ['222->220', '223->225', '226->220']

import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def inventory_manager():
    from ansible.inventory.manager import InventoryManager
    manager = InventoryManager(loader=MagicMock())
    manager._sources = ['source1', 'source2']
    manager._inventory = MagicMock()
    manager._groups = {}
    manager._hosts = {}
    manager._loader = MagicMock()
    return manager

def test_parse_sources_with_comma(inventory_manager, mocker):
    mocker.patch('ansible.inventory.manager.unfrackpath', return_value='unfracked_path')
    mocker.patch.object(inventory_manager, 'parse_source', return_value=True)
    mocker.patch('ansible.inventory.manager.C', INVENTORY_UNPARSED_IS_FAILED=False)
    mocker.patch('ansible.inventory.manager.display')

    inventory_manager._sources = ['source1,source2']

    inventory_manager.parse_sources(cache=False)

    inventory_manager.parse_source.assert_called_with('source1,source2', cache=False)
    inventory_manager._inventory.reconcile_inventory.assert_called_once()

def test_parse_sources_without_comma(inventory_manager, mocker):
    mocker.patch('ansible.inventory.manager.unfrackpath', return_value='unfracked_path')
    mocker.patch.object(inventory_manager, 'parse_source', return_value=True)
    mocker.patch('ansible.inventory.manager.C', INVENTORY_UNPARSED_IS_FAILED=False)
    mocker.patch('ansible.inventory.manager.display')

    inventory_manager._sources = ['source1']

    inventory_manager.parse_sources(cache=False)

    inventory_manager.parse_source.assert_called_with('unfracked_path', cache=False)
    inventory_manager._inventory.reconcile_inventory.assert_called_once()

def test_parse_sources_no_inventory_parsed(inventory_manager, mocker):
    mocker.patch('ansible.inventory.manager.unfrackpath', return_value='unfracked_path')
    mocker.patch.object(inventory_manager, 'parse_source', return_value=False)
    mocker.patch('ansible.inventory.manager.C', INVENTORY_UNPARSED_IS_FAILED=True)
    mocker.patch('ansible.inventory.manager.display')

    inventory_manager._sources = ['source1']

    with pytest.raises(Exception) as excinfo:
        inventory_manager.parse_sources(cache=False)

    assert "No inventory was parsed, please check your configuration and options." in str(excinfo.value)
