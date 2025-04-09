# file: lib/ansible/inventory/manager.py:590-599
# asked: {"lines": [590, 593, 596, 597, 599], "branches": [[596, 597], [596, 599]]}
# gained: {"lines": [590, 593, 596, 597, 599], "branches": [[596, 597], [596, 599]]}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible import constants as C

class MockedConstants:
    LOCALHOST = ['localhost']

@pytest.fixture
def inventory_manager(mocker):
    loader = mocker.Mock()
    manager = InventoryManager(loader)
    mocker.patch('ansible.inventory.manager.InventoryManager.get_hosts', return_value=[])
    return manager

def test_list_hosts_with_no_hosts_and_pattern_in_localhost(inventory_manager, mocker):
    mocker.patch('ansible.constants', MockedConstants)
    result = inventory_manager.list_hosts('localhost')
    assert result == ['localhost']

def test_list_hosts_with_no_hosts_and_pattern_not_in_localhost(inventory_manager):
    result = inventory_manager.list_hosts('not_in_localhost')
    assert result == []

def test_list_hosts_with_hosts(inventory_manager, mocker):
    mocker.patch('ansible.inventory.manager.InventoryManager.get_hosts', return_value=['host1', 'host2'])
    result = inventory_manager.list_hosts('some_pattern')
    assert result == ['host1', 'host2']
