# file: lib/ansible/inventory/manager.py:215-241
# asked: {"lines": [215, 218, 220, 222, 223, 224, 225, 226, 227, 229, 231, 233, 234, 236, 238, 239, 240, 241], "branches": [[220, 222], [220, 229], [222, 220], [222, 223], [223, 224], [223, 225], [226, 220], [226, 227], [229, 231], [229, 233], [233, 234], [233, 236], [238, 239], [238, 240], [240, 0], [240, 241]]}
# gained: {"lines": [215, 218, 220, 222, 223, 224, 225, 226, 227, 229, 231, 233, 234, 236, 238, 239, 240, 241], "branches": [[220, 222], [220, 229], [222, 223], [223, 224], [226, 220], [226, 227], [229, 231], [229, 233], [233, 234], [233, 236], [238, 239], [238, 240], [240, 0], [240, 241]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError
from ansible import constants as C

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    sources = ['inventory1', 'inventory2']
    return InventoryManager(loader, sources)

def test_parse_sources_with_valid_sources(inventory_manager):
    inventory_manager._sources = ['inventory1', 'inventory2']
    inventory_manager.parse_source = MagicMock(return_value=True)
    inventory_manager._inventory.reconcile_inventory = MagicMock()
    inventory_manager._inventory.groups = {'group1': MagicMock(vars={}), 'group2': MagicMock(vars={})}
    inventory_manager._inventory.hosts = {'host1': MagicMock(vars={}), 'host2': MagicMock(vars={})}

    with patch('ansible.inventory.manager.unfrackpath', side_effect=lambda x, follow: x):
        with patch('ansible.inventory.manager.get_vars_from_inventory_sources', return_value={'var1': 'value1'}):
            inventory_manager.parse_sources()

    inventory_manager._inventory.reconcile_inventory.assert_called_once()
    for group in inventory_manager.groups.values():
        assert group.vars == {'var1': 'value1'}
    for host in inventory_manager.hosts.values():
        assert host.vars == {'var1': 'value1'}

def test_parse_sources_with_no_parsed_sources(inventory_manager):
    inventory_manager._sources = ['inventory1', 'inventory2']
    inventory_manager.parse_source = MagicMock(return_value=False)
    inventory_manager._inventory.groups = {}
    inventory_manager._inventory.hosts = {}

    with patch('ansible.inventory.manager.unfrackpath', side_effect=lambda x, follow: x):
        with patch('ansible.inventory.manager.display.warning') as mock_warning:
            inventory_manager.parse_sources()

    mock_warning.assert_called_once_with("No inventory was parsed, only implicit localhost is available")

def test_parse_sources_with_no_parsed_sources_and_error(inventory_manager):
    inventory_manager._sources = ['inventory1', 'inventory2']
    inventory_manager.parse_source = MagicMock(return_value=False)
    inventory_manager._inventory.groups = {}
    inventory_manager._inventory.hosts = {}

    with patch('ansible.inventory.manager.unfrackpath', side_effect=lambda x, follow: x):
        with patch('ansible.inventory.manager.C.INVENTORY_UNPARSED_IS_FAILED', True):
            with pytest.raises(AnsibleError, match="No inventory was parsed, please check your configuration and options."):
                inventory_manager.parse_sources()
