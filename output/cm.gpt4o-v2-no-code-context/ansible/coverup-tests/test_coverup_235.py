# file: lib/ansible/inventory/manager.py:533-549
# asked: {"lines": [533, 539, 540, 542, 544, 545, 546, 547, 549], "branches": [[539, 540], [539, 542], [544, 545], [544, 549], [545, 546], [545, 547]]}
# gained: {"lines": [533, 539, 540, 542, 544, 545, 546, 547, 549], "branches": [[539, 540], [539, 542], [544, 545], [544, 549], [545, 546], [545, 547]]}

import pytest
from ansible.inventory.manager import InventoryManager
from unittest.mock import Mock

@pytest.fixture
def inventory_manager():
    loader = Mock()
    return InventoryManager(loader)

def test_apply_subscript_no_hosts(inventory_manager):
    result = inventory_manager._apply_subscript([], (0, 1))
    assert result == []

def test_apply_subscript_no_subscript(inventory_manager):
    hosts = ['host1', 'host2', 'host3']
    result = inventory_manager._apply_subscript(hosts, None)
    assert result == hosts

def test_apply_subscript_with_end(inventory_manager):
    hosts = ['host1', 'host2', 'host3', 'host4']
    result = inventory_manager._apply_subscript(hosts, (1, 3))
    assert result == ['host2', 'host3', 'host4']

def test_apply_subscript_with_end_minus_one(inventory_manager):
    hosts = ['host1', 'host2', 'host3', 'host4']
    result = inventory_manager._apply_subscript(hosts, (1, -1))
    assert result == ['host2', 'host3', 'host4']

def test_apply_subscript_without_end(inventory_manager):
    hosts = ['host1', 'host2', 'host3', 'host4']
    result = inventory_manager._apply_subscript(hosts, (2, None))
    assert result == ['host3']
