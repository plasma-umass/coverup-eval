# file: lib/ansible/inventory/manager.py:590-599
# asked: {"lines": [590, 593, 596, 597, 599], "branches": [[596, 597], [596, 599]]}
# gained: {"lines": [590, 593, 596, 597, 599], "branches": [[596, 597], [596, 599]]}

import pytest
from ansible.inventory.manager import InventoryManager
from ansible import constants as C
from unittest.mock import MagicMock

@pytest.fixture
def inventory_manager(mocker):
    loader = MagicMock()
    return InventoryManager(loader)

def test_list_hosts_with_pattern_all(inventory_manager, mocker):
    mocker.patch.object(inventory_manager, 'get_hosts', return_value=[])
    pattern = "all"
    result = inventory_manager.list_hosts(pattern)
    assert result == []

def test_list_hosts_with_non_empty_result(inventory_manager, mocker):
    mocker.patch.object(inventory_manager, 'get_hosts', return_value=['host1', 'host2'])
    pattern = "all"
    result = inventory_manager.list_hosts(pattern)
    assert result == ['host1', 'host2']

def test_list_hosts_with_empty_result_and_non_localhost_pattern(inventory_manager, mocker):
    mocker.patch.object(inventory_manager, 'get_hosts', return_value=[])
    pattern = "non_localhost"
    result = inventory_manager.list_hosts(pattern)
    assert result == []

def test_list_hosts_with_empty_result_and_localhost_pattern(inventory_manager, mocker):
    mocker.patch.object(inventory_manager, 'get_hosts', return_value=[])
    pattern = "localhost"
    mocker.patch('ansible.constants.LOCALHOST', pattern)
    result = inventory_manager.list_hosts(pattern)
    assert result == [pattern]
