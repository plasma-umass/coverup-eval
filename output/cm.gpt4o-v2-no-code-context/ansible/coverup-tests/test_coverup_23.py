# file: lib/ansible/inventory/manager.py:365-420
# asked: {"lines": [365, 372, 375, 376, 378, 380, 381, 382, 384, 385, 389, 391, 393, 394, 397, 399, 400, 402, 404, 406, 409, 410, 411, 412, 414, 415, 416, 417, 418, 420], "branches": [[375, 376], [375, 378], [380, 381], [380, 420], [381, 382], [381, 384], [384, 385], [384, 389], [391, 393], [391, 409], [397, 399], [397, 402], [402, 404], [402, 406], [409, 410], [409, 411], [411, 412], [411, 414], [415, 416], [415, 417], [417, 418], [417, 420]]}
# gained: {"lines": [365, 372, 375, 376, 378, 380, 381, 382, 384, 385, 389, 391, 393, 394, 397, 399, 400, 402, 404, 406, 409, 410, 411, 412, 414, 415, 416, 417, 418, 420], "branches": [[375, 376], [375, 378], [380, 381], [381, 382], [381, 384], [384, 385], [384, 389], [391, 393], [397, 399], [397, 402], [402, 404], [402, 406], [409, 410], [409, 411], [411, 412], [411, 414], [415, 416], [415, 417], [417, 418], [417, 420]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.inventory.manager import InventoryManager
from ansible.errors import AnsibleOptionsError

class MockHost:
    def __init__(self, name, uuid):
        self.name = name
        self._uuid = uuid

@pytest.fixture
def inventory_manager():
    loader = MagicMock()
    sources = MagicMock()
    manager = InventoryManager(loader, sources)
    manager._subset = None
    manager._restriction = None
    manager._hosts_patterns_cache = {}
    return manager

def test_get_hosts_with_pattern_list(inventory_manager):
    inventory_manager._evaluate_patterns = MagicMock(return_value=[MockHost('host1', 'uuid1'), MockHost('host2', 'uuid2')])
    inventory_manager._hosts_patterns_cache = {}
    pattern = ['pattern1', 'pattern2']
    result = inventory_manager.get_hosts(pattern=pattern)
    assert [host.name for host in result] == ['host1', 'host2']

def test_get_hosts_with_subset(inventory_manager):
    inventory_manager._subset = ['subset1']
    inventory_manager._evaluate_patterns = MagicMock(side_effect=[[MockHost('host1', 'uuid1'), MockHost('host2', 'uuid2')], [MockHost('subset_host', 'uuid3')]])
    inventory_manager._hosts_patterns_cache = {}
    pattern = 'pattern1'
    result = inventory_manager.get_hosts(pattern=pattern)
    assert result == []

def test_get_hosts_with_restriction(inventory_manager):
    inventory_manager._restriction = ['host1']
    inventory_manager._evaluate_patterns = MagicMock(return_value=[MockHost('host1', 'uuid1'), MockHost('host2', 'uuid2')])
    inventory_manager._hosts_patterns_cache = {}
    pattern = 'pattern1'
    result = inventory_manager.get_hosts(pattern=pattern)
    assert [host.name for host in result] == ['host1']

def test_get_hosts_with_order_sorted(inventory_manager):
    inventory_manager._evaluate_patterns = MagicMock(return_value=[MockHost('host2', 'uuid2'), MockHost('host1', 'uuid1')])
    inventory_manager._hosts_patterns_cache = {}
    pattern = 'pattern1'
    result = inventory_manager.get_hosts(pattern=pattern, order='sorted')
    assert [host.name for host in result] == ['host1', 'host2']

def test_get_hosts_with_order_reverse_sorted(inventory_manager):
    inventory_manager._evaluate_patterns = MagicMock(return_value=[MockHost('host1', 'uuid1'), MockHost('host2', 'uuid2')])
    inventory_manager._hosts_patterns_cache = {}
    pattern = 'pattern1'
    result = inventory_manager.get_hosts(pattern=pattern, order='reverse_sorted')
    assert [host.name for host in result] == ['host2', 'host1']

def test_get_hosts_with_order_reverse_inventory(inventory_manager):
    inventory_manager._evaluate_patterns = MagicMock(return_value=[MockHost('host1', 'uuid1'), MockHost('host2', 'uuid2')])
    inventory_manager._hosts_patterns_cache = {}
    pattern = 'pattern1'
    result = inventory_manager.get_hosts(pattern=pattern, order='reverse_inventory')
    assert [host.name for host in result] == ['host2', 'host1']

def test_get_hosts_with_order_shuffle(inventory_manager, monkeypatch):
    inventory_manager._evaluate_patterns = MagicMock(return_value=[MockHost('host1', 'uuid1'), MockHost('host2', 'uuid2')])
    inventory_manager._hosts_patterns_cache = {}
    pattern = 'pattern1'
    monkeypatch.setattr('ansible.inventory.manager.shuffle', lambda x: x.reverse())
    result = inventory_manager.get_hosts(pattern=pattern, order='shuffle')
    assert [host.name for host in result] == ['host2', 'host1']

def test_get_hosts_with_invalid_order(inventory_manager):
    inventory_manager._evaluate_patterns = MagicMock(return_value=[MockHost('host1', 'uuid1'), MockHost('host2', 'uuid2')])
    inventory_manager._hosts_patterns_cache = {}
    pattern = 'pattern1'
    with pytest.raises(AnsibleOptionsError, match="Invalid 'order' specified for inventory hosts: invalid_order"):
        inventory_manager.get_hosts(pattern=pattern, order='invalid_order')
