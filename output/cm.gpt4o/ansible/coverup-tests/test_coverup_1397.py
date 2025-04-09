# file lib/ansible/inventory/manager.py:551-588
# lines [569, 570, 574, 575, 576, 584, 585]
# branches ['568->569', '569->570', '569->572', '572->574', '575->576', '575->579', '582->584', '584->585', '584->588']

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleError
import ansible.constants as C

@pytest.fixture
def inventory_manager():
    inventory = MagicMock()
    inventory.groups = {
        'group1': MagicMock(get_hosts=MagicMock(return_value=[])),
        'group2': MagicMock(get_hosts=MagicMock(return_value=[]))
    }
    inventory.hosts = {
        'host1': MagicMock(),
        'host2': MagicMock()
    }
    return InventoryManager(inventory)

def test_enumerate_matches_no_matching_groups_or_hosts(inventory_manager):
    pattern = 'nonexistent'
    with patch('ansible.inventory.manager.display') as mock_display:
        C.HOST_PATTERN_MISMATCH = 'warning'
        results = inventory_manager._enumerate_matches(pattern)
        assert results == []
        mock_display.debug.assert_called_once_with("Could not match supplied host pattern, ignoring: nonexistent")
        mock_display.warning.assert_called_once_with("Could not match supplied host pattern, ignoring: nonexistent")

def test_enumerate_matches_implicit_localhost(inventory_manager):
    pattern = 'localhost'
    with patch('ansible.inventory.manager.C.LOCALHOST', ['localhost']):
        inventory_manager._inventory.get_host = MagicMock(return_value='implicit_localhost')
        results = inventory_manager._enumerate_matches(pattern)
        assert results == ['implicit_localhost']
        inventory_manager._inventory.get_host.assert_called_once_with('localhost')

def test_enumerate_matches_host_pattern_mismatch_error(inventory_manager):
    pattern = 'nonexistent'
    with patch('ansible.inventory.manager.display') as mock_display:
        C.HOST_PATTERN_MISMATCH = 'error'
        with pytest.raises(AnsibleError, match="Could not match supplied host pattern, ignoring: nonexistent"):
            inventory_manager._enumerate_matches(pattern)
        mock_display.debug.assert_called_once_with("Could not match supplied host pattern, ignoring: nonexistent")

def test_enumerate_matches_matching_hosts(inventory_manager):
    pattern = 'host1'
    inventory_manager._inventory.hosts = {
        'host1': MagicMock(),
        'host2': MagicMock()
    }
    results = inventory_manager._enumerate_matches(pattern)
    assert results == [inventory_manager._inventory.hosts['host1']]
