# file: lib/ansible/inventory/manager.py:66-91
# asked: {"lines": [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91], "branches": [[73, 74], [73, 86], [74, 75], [74, 77], [77, 78], [77, 79], [79, 80], [79, 82], [86, 87], [86, 91]]}
# gained: {"lines": [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91], "branches": [[73, 74], [73, 86], [74, 75], [74, 77], [77, 78], [77, 79], [79, 80], [79, 82], [86, 87], [86, 91]]}

import pytest
from ansible.inventory.manager import order_patterns

def test_order_patterns_all_types():
    patterns = ["!exclude", "&intersection", "regular"]
    result = order_patterns(patterns)
    assert result == ["regular", "&intersection", "!exclude"]

def test_order_patterns_only_exclude():
    patterns = ["!exclude1", "!exclude2"]
    result = order_patterns(patterns)
    assert result == ["all", "!exclude1", "!exclude2"]

def test_order_patterns_only_intersection():
    patterns = ["&intersection1", "&intersection2"]
    result = order_patterns(patterns)
    assert result == ["all", "&intersection1", "&intersection2"]

def test_order_patterns_mixed_with_empty():
    patterns = ["!exclude", "", "&intersection", "regular"]
    result = order_patterns(patterns)
    assert result == ["regular", "&intersection", "!exclude"]

def test_order_patterns_empty_list():
    patterns = []
    result = order_patterns(patterns)
    assert result == ["all"]
