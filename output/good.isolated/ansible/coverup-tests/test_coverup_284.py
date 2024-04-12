# file lib/ansible/inventory/manager.py:533-549
# lines [533, 539, 540, 542, 544, 545, 546, 547, 549]
# branches ['539->540', '539->542', '544->545', '544->549', '545->546', '545->547']

import pytest
from unittest.mock import MagicMock

# Assuming the InventoryManager class is part of the ansible.inventory.manager module
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    return InventoryManager(loader=loader)

def test_apply_subscript_with_full_range(inventory_manager):
    hosts = ['host1', 'host2', 'host3']
    subscript = (0, -1)
    result = inventory_manager._apply_subscript(hosts, subscript)
    assert result == hosts

def test_apply_subscript_with_sub_range(inventory_manager):
    hosts = ['host1', 'host2', 'host3']
    subscript = (1, 2)
    result = inventory_manager._apply_subscript(hosts, subscript)
    assert result == ['host2', 'host3']

def test_apply_subscript_with_single_element(inventory_manager):
    hosts = ['host1', 'host2', 'host3']
    subscript = (1, None)
    result = inventory_manager._apply_subscript(hosts, subscript)
    assert result == ['host2']

def test_apply_subscript_with_no_subscript(inventory_manager):
    hosts = ['host1', 'host2', 'host3']
    subscript = None
    result = inventory_manager._apply_subscript(hosts, subscript)
    assert result == hosts

def test_apply_subscript_with_empty_hosts(inventory_manager):
    hosts = []
    subscript = (0, 1)
    result = inventory_manager._apply_subscript(hosts, subscript)
    assert result == hosts

def test_apply_subscript_with_no_hosts(inventory_manager):
    hosts = None
    subscript = (0, 1)
    result = inventory_manager._apply_subscript(hosts, subscript)
    assert result == hosts
