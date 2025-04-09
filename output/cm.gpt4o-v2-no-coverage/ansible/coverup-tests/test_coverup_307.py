# file: lib/ansible/inventory/manager.py:448-498
# asked: {"lines": [448, 486, 487, 489, 490, 491, 492, 493, 494, 495, 496, 498], "branches": [[486, 487], [486, 489], [489, 490], [489, 498]]}
# gained: {"lines": [448, 486, 489, 490, 491, 492, 493, 494, 495, 496, 498], "branches": [[486, 489], [489, 490], [489, 498]]}

import pytest
import re
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager

class MockInventoryManager(InventoryManager):
    def __init__(self):
        self._pattern_cache = {}
    
    def _split_subscript(self, pattern):
        # Mock implementation
        if '[' in pattern and ']' in pattern:
            return pattern.split('[')[0], pattern.split('[')[1][:-1]
        return pattern, None
    
    def _enumerate_matches(self, expr):
        # Mock implementation
        if expr == 'all':
            return ['host1', 'host2', 'host3']
        elif expr == 'foo*':
            return ['foo1', 'foo2']
        elif expr == 'bar':
            return ['bar1']
        return []
    
    def _apply_subscript(self, hosts, slice):
        # Mock implementation
        if slice is None:
            return hosts
        index = int(slice)
        if index < len(hosts):
            return [hosts[index]]
        raise IndexError

@pytest.fixture
def inventory_manager():
    return MockInventoryManager()

def test_match_one_pattern_all(inventory_manager):
    pattern = 'all'
    result = inventory_manager._match_one_pattern(pattern)
    assert result == ['host1', 'host2', 'host3']

def test_match_one_pattern_with_subscript(inventory_manager):
    pattern = 'foo*[1]'
    result = inventory_manager._match_one_pattern(pattern)
    assert result == ['foo2']

def test_match_one_pattern_no_match(inventory_manager):
    pattern = 'baz'
    result = inventory_manager._match_one_pattern(pattern)
    assert result == []

def test_match_one_pattern_index_error(inventory_manager):
    pattern = 'foo*[10]'
    with pytest.raises(AnsibleError, match=re.escape("No hosts matched the subscripted pattern 'foo*[10]'")):
        inventory_manager._match_one_pattern(pattern)

def test_match_one_pattern_cache(inventory_manager):
    pattern = 'bar'
    result1 = inventory_manager._match_one_pattern(pattern)
    result2 = inventory_manager._match_one_pattern(pattern)
    assert result1 == ['bar1']
    assert result2 == result1
    assert pattern in inventory_manager._pattern_cache
