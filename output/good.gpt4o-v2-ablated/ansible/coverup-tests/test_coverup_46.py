# file: lib/ansible/inventory/manager.py:66-91
# asked: {"lines": [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91], "branches": [[73, 74], [73, 86], [74, 75], [74, 77], [77, 78], [77, 79], [79, 80], [79, 82], [86, 87], [86, 91]]}
# gained: {"lines": [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91], "branches": [[73, 74], [73, 86], [74, 75], [74, 77], [77, 78], [77, 79], [79, 80], [79, 82], [86, 87], [86, 91]]}

import pytest

from ansible.inventory.manager import order_patterns

def test_order_patterns_all_types():
    patterns = ["!exclude", "&intersection", "regular"]
    expected = ["regular", "&intersection", "!exclude"]
    result = order_patterns(patterns)
    assert result == expected

def test_order_patterns_only_exclude():
    patterns = ["!exclude1", "!exclude2"]
    expected = ["all", "!exclude1", "!exclude2"]
    result = order_patterns(patterns)
    assert result == expected

def test_order_patterns_only_intersection():
    patterns = ["&intersection1", "&intersection2"]
    expected = ["all", "&intersection1", "&intersection2"]
    result = order_patterns(patterns)
    assert result == expected

def test_order_patterns_mixed():
    patterns = ["regular1", "!exclude1", "&intersection1", "regular2", "!exclude2", "&intersection2"]
    expected = ["regular1", "regular2", "&intersection1", "&intersection2", "!exclude1", "!exclude2"]
    result = order_patterns(patterns)
    assert result == expected

def test_order_patterns_empty():
    patterns = []
    expected = ["all"]
    result = order_patterns(patterns)
    assert result == expected

def test_order_patterns_none():
    patterns = [None, "!exclude", "&intersection", "regular"]
    expected = ["regular", "&intersection", "!exclude"]
    result = order_patterns(patterns)
    assert result == expected

def test_order_patterns_empty_string():
    patterns = ["", "!exclude", "&intersection", "regular"]
    expected = ["regular", "&intersection", "!exclude"]
    result = order_patterns(patterns)
    assert result == expected
