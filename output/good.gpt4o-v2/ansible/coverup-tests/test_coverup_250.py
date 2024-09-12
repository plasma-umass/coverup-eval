# file: lib/ansible/inventory/manager.py:448-498
# asked: {"lines": [448, 486, 487, 489, 490, 491, 492, 493, 494, 495, 496, 498], "branches": [[486, 487], [486, 489], [489, 490], [489, 498]]}
# gained: {"lines": [448, 486, 489, 490, 491, 492, 493, 494, 495, 496, 498], "branches": [[486, 489], [489, 490], [489, 498]]}

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.manager import InventoryManager

class MockInventoryManager(InventoryManager):
    def __init__(self):
        self._pattern_cache = {}
        self._groups = {
            'group1': ['host1', 'host2'],
            'group2': ['host3', 'host4'],
        }

    def _split_subscript(self, pattern):
        if '[' in pattern and ']' in pattern:
            expr, subscript = pattern.split('[')
            subscript = subscript.rstrip(']')
            return expr, subscript
        return pattern, None

    def _enumerate_matches(self, expr):
        if expr == 'all':
            return ['host1', 'host2', 'host3', 'host4']
        elif expr in self._groups:
            return self._groups[expr]
        return []

    def _apply_subscript(self, hosts, subscript):
        if subscript is None:
            return hosts
        index = int(subscript)
        return [hosts[index]]

@pytest.fixture
def inventory_manager():
    return MockInventoryManager()

def test_match_one_pattern_all(inventory_manager):
    result = inventory_manager._match_one_pattern('all')
    assert result == ['host1', 'host2', 'host3', 'host4']

def test_match_one_pattern_group(inventory_manager):
    result = inventory_manager._match_one_pattern('group1')
    assert result == ['host1', 'host2']

def test_match_one_pattern_subscript(inventory_manager):
    result = inventory_manager._match_one_pattern('group1[1]')
    assert result == ['host2']

def test_match_one_pattern_no_match(inventory_manager):
    with pytest.raises(AnsibleError, match=r"No hosts matched the subscripted pattern 'group1\[10\]'"):
        inventory_manager._match_one_pattern('group1[10]')

def test_match_one_pattern_cache(inventory_manager):
    inventory_manager._pattern_cache['group1'] = ['host1', 'host2']
    result = inventory_manager._match_one_pattern('group1')
    assert result == ['host1', 'host2']
