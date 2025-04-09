# file: lib/ansible/inventory/manager.py:66-91
# asked: {"lines": [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91], "branches": [[73, 74], [73, 86], [74, 75], [74, 77], [77, 78], [77, 79], [79, 80], [79, 82], [86, 87], [86, 91]]}
# gained: {"lines": [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91], "branches": [[73, 74], [73, 86], [74, 75], [74, 77], [77, 78], [77, 79], [79, 80], [79, 82], [86, 87], [86, 91]]}

import pytest
from ansible.inventory.manager import order_patterns

def test_order_patterns():
    # Test with a mix of patterns
    patterns = ["!exclude", "&intersection", "regular", "!exclude2", "&intersection2", "regular2"]
    expected = ["regular", "regular2", "&intersection", "&intersection2", "!exclude", "!exclude2"]
    assert order_patterns(patterns) == expected

    # Test with only exclude patterns
    patterns = ["!exclude", "!exclude2"]
    expected = ["all", "!exclude", "!exclude2"]
    assert order_patterns(patterns) == expected

    # Test with only intersection patterns
    patterns = ["&intersection", "&intersection2"]
    expected = ["all", "&intersection", "&intersection2"]
    assert order_patterns(patterns) == expected

    # Test with empty patterns
    patterns = []
    expected = ["all"]
    assert order_patterns(patterns) == expected

    # Test with None patterns
    patterns = [None, "!exclude", "&intersection", "regular"]
    expected = ["regular", "&intersection", "!exclude"]
    assert order_patterns(patterns) == expected

    # Test with empty string patterns
    patterns = ["", "!exclude", "&intersection", "regular"]
    expected = ["regular", "&intersection", "!exclude"]
    assert order_patterns(patterns) == expected
