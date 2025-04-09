# file: lib/ansible/inventory/manager.py:66-91
# asked: {"lines": [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91], "branches": [[73, 74], [73, 86], [74, 75], [74, 77], [77, 78], [77, 79], [79, 80], [79, 82], [86, 87], [86, 91]]}
# gained: {"lines": [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91], "branches": [[73, 74], [73, 86], [74, 75], [74, 77], [77, 78], [77, 79], [79, 80], [79, 82], [86, 87], [86, 91]]}

import pytest
from ansible.inventory.manager import order_patterns

def test_order_patterns_all_empty():
    patterns = []
    result = order_patterns(patterns)
    assert result == ['all']

def test_order_patterns_only_exclude():
    patterns = ['!exclude']
    result = order_patterns(patterns)
    assert result == ['all', '!exclude']

def test_order_patterns_only_intersection():
    patterns = ['&intersection']
    result = order_patterns(patterns)
    assert result == ['all', '&intersection']

def test_order_patterns_mixed():
    patterns = ['pattern1', '!exclude', '&intersection', 'pattern2']
    result = order_patterns(patterns)
    assert result == ['pattern1', 'pattern2', '&intersection', '!exclude']

def test_order_patterns_empty_string():
    patterns = ['']
    result = order_patterns(patterns)
    assert result == ['all']

def test_order_patterns_none():
    patterns = [None]
    result = order_patterns(patterns)
    assert result == ['all']
