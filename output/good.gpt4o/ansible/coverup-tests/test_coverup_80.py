# file lib/ansible/inventory/manager.py:215-241
# lines [215, 218, 220, 222, 223, 224, 225, 226, 227, 229, 231, 233, 234, 236, 238, 239, 240, 241]
# branches ['220->222', '220->229', '222->220', '222->223', '223->224', '223->225', '226->220', '226->227', '229->231', '229->233', '233->234', '233->236', '238->239', '238->240', '240->exit', '240->241']

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError
from ansible.utils.display import Display

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    inventory = MagicMock()
    manager = InventoryManager(loader, inventory)
    manager._sources = []
    manager._inventory = inventory
    manager._inventory.groups = {}
    manager._inventory.hosts = {}
    return manager

def test_parse_sources_no_sources(inventory_manager, mocker):
    mocker.patch('ansible.inventory.manager.C.INVENTORY_UNPARSED_IS_FAILED', True)
    with pytest.raises(AnsibleError, match="No inventory was parsed, please check your configuration and options."):
        inventory_manager.parse_sources()

def test_parse_sources_no_sources_warning(inventory_manager, mocker):
    mocker.patch('ansible.inventory.manager.C.INVENTORY_UNPARSED_IS_FAILED', False)
    display_warning = mocker.patch.object(Display, 'warning')
    inventory_manager.parse_sources()
    display_warning.assert_called_once_with("No inventory was parsed, only implicit localhost is available")

def test_parse_sources_with_sources(inventory_manager, mocker):
    inventory_manager._sources = ['source1']
    inventory_manager.parse_source = MagicMock(return_value=True)
    inventory_manager._inventory.reconcile_inventory = MagicMock()
    inventory_manager.parse_sources()
    inventory_manager._inventory.reconcile_inventory.assert_called_once()

def test_parse_sources_group_vars(inventory_manager, mocker):
    inventory_manager._sources = ['source1']
    inventory_manager.parse_source = MagicMock(return_value=True)
    inventory_manager._inventory.reconcile_inventory = MagicMock()
    inventory_manager._inventory.groups = {'group1': MagicMock()}
    mocker.patch('ansible.inventory.manager.combine_vars', return_value={'var1': 'value1'})
    mocker.patch('ansible.inventory.manager.get_vars_from_inventory_sources', return_value={'var1': 'value1'})
    inventory_manager.parse_sources()
    assert inventory_manager._inventory.groups['group1'].vars == {'var1': 'value1'}

def test_parse_sources_host_vars(inventory_manager, mocker):
    inventory_manager._sources = ['source1']
    inventory_manager.parse_source = MagicMock(return_value=True)
    inventory_manager._inventory.reconcile_inventory = MagicMock()
    inventory_manager._inventory.hosts = {'host1': MagicMock()}
    mocker.patch('ansible.inventory.manager.combine_vars', return_value={'var1': 'value1'})
    mocker.patch('ansible.inventory.manager.get_vars_from_inventory_sources', return_value={'var1': 'value1'})
    inventory_manager.parse_sources()
    assert inventory_manager._inventory.hosts['host1'].vars == {'var1': 'value1'}
