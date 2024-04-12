# file lib/ansible/inventory/manager.py:448-498
# lines [448, 486, 487, 489, 490, 491, 492, 493, 494, 495, 496, 498]
# branches ['486->487', '486->489', '489->490', '489->498']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager
from ansible.inventory.host import Host
from ansible.inventory.group import Group

@pytest.fixture
def inventory_manager(mocker):
    mocker.patch('ansible.inventory.manager.InventoryManager.parse_sources', return_value=None)
    inventory = InventoryManager(loader=None, sources='localhost,')
    all_group = Group('all')
    ungrouped_group = Group('ungrouped')
    test_group = Group('testgroup')
    test_group.add_host(Host('testhost1'))
    test_group.add_host(Host('testhost2'))
    inventory._inventory.groups = {
        'all': all_group,
        'ungrouped': ungrouped_group,
        'testgroup': test_group
    }
    inventory._inventory.hosts = {
        'testhost1': inventory._inventory.groups['testgroup'].hosts[0],
        'testhost2': inventory._inventory.groups['testgroup'].hosts[1]
    }
    inventory._pattern_cache = {}
    return inventory

def test_match_one_pattern_with_subscript(inventory_manager):
    # Test a pattern with a valid subscript
    matched_hosts = inventory_manager._match_one_pattern('testgroup[0]')
    assert len(matched_hosts) == 1
    assert matched_hosts[0].name == 'testhost1'

    # Test a pattern with an invalid subscript that should raise an error
    with pytest.raises(AnsibleError) as excinfo:
        inventory_manager._match_one_pattern('testgroup[2]')
    assert "No hosts matched the subscripted pattern 'testgroup[2]'" in str(excinfo.value)

def test_match_one_pattern_with_special_characters(inventory_manager):
    # Test a pattern starting with '&' or '!' which should be ignored
    matched_hosts_ampersand = inventory_manager._match_one_pattern('&testgroup')
    matched_hosts_exclamation = inventory_manager._match_one_pattern('!testgroup')
    assert matched_hosts_ampersand == inventory_manager._match_one_pattern('testgroup')
    assert matched_hosts_exclamation == inventory_manager._match_one_pattern('testgroup')

    # Test that the cache is used after the first call
    assert 'testgroup' in inventory_manager._pattern_cache
    assert inventory_manager._pattern_cache['testgroup'] == inventory_manager._match_one_pattern('testgroup')
