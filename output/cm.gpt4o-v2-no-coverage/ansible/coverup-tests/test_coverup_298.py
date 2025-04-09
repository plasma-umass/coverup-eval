# file: lib/ansible/inventory/manager.py:533-549
# asked: {"lines": [533, 539, 540, 542, 544, 545, 546, 547, 549], "branches": [[539, 540], [539, 542], [544, 545], [544, 549], [545, 546], [545, 547]]}
# gained: {"lines": [533, 539, 540, 542, 544, 545, 546, 547, 549], "branches": [[539, 540], [539, 542], [544, 545], [544, 549], [545, 546], [545, 547]]}

import pytest
from ansible.inventory.manager import InventoryManager

@pytest.fixture
def inventory_manager():
    return InventoryManager(loader=None)

def test_apply_subscript_no_hosts(inventory_manager):
    assert inventory_manager._apply_subscript([], (0, 1)) == []

def test_apply_subscript_no_subscript(inventory_manager):
    hosts = ['host1', 'host2', 'host3']
    assert inventory_manager._apply_subscript(hosts, None) == hosts

def test_apply_subscript_with_end(inventory_manager):
    hosts = ['host1', 'host2', 'host3']
    assert inventory_manager._apply_subscript(hosts, (0, 1)) == ['host1', 'host2']

def test_apply_subscript_with_end_minus_one(inventory_manager):
    hosts = ['host1', 'host2', 'host3']
    assert inventory_manager._apply_subscript(hosts, (0, -1)) == ['host1', 'host2', 'host3']

def test_apply_subscript_with_no_end(inventory_manager):
    hosts = ['host1', 'host2', 'host3']
    assert inventory_manager._apply_subscript(hosts, (1, None)) == ['host2']
