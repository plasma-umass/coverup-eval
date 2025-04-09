# file lib/ansible/inventory/manager.py:66-91
# lines [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91]
# branches ['73->74', '73->86', '74->75', '74->77', '77->78', '77->79', '79->80', '79->82', '86->87', '86->91']

import pytest
from ansible.inventory.manager import order_patterns

def test_order_patterns():
    # Test with a mix of regular, intersection, and exclude patterns
    patterns = ['web', '&db', '!test']
    expected_order = ['web', '&db', '!test']
    assert order_patterns(patterns) == expected_order

    # Test with only exclude patterns
    patterns = ['!test', '!prod']
    expected_order = ['all', '!test', '!prod']
    assert order_patterns(patterns) == expected_order

    # Test with only intersection patterns
    patterns = ['&db', '&cache']
    expected_order = ['all', '&db', '&cache']
    assert order_patterns(patterns) == expected_order

    # Test with empty patterns
    patterns = []
    expected_order = ['all']
    assert order_patterns(patterns) == expected_order

    # Test with a mix of empty, regular, intersection, and exclude patterns
    patterns = ['', 'web', '&db', '!test', '']
    expected_order = ['web', '&db', '!test']
    assert order_patterns(patterns) == expected_order

    # Test with only regular patterns
    patterns = ['web', 'db']
    expected_order = ['web', 'db']
    assert order_patterns(patterns) == expected_order
