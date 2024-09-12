# file: lib/ansible/inventory/manager.py:66-91
# asked: {"lines": [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91], "branches": [[73, 74], [73, 86], [74, 75], [74, 77], [77, 78], [77, 79], [79, 80], [79, 82], [86, 87], [86, 91]]}
# gained: {"lines": [66, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91], "branches": [[73, 74], [73, 86], [74, 75], [74, 77], [77, 78], [77, 79], [79, 80], [79, 82], [86, 87], [86, 91]]}

import pytest
from ansible.inventory.manager import order_patterns

def test_order_patterns_all_cases():
    # Test with regular patterns, intersection patterns, and exclude patterns
    patterns = ['host1', '&host2', '!host3']
    result = order_patterns(patterns)
    assert result == ['host1', '&host2', '!host3']

    # Test with only exclude patterns
    patterns = ['!host1', '!host2']
    result = order_patterns(patterns)
    assert result == ['all', '!host1', '!host2']

    # Test with only intersection patterns
    patterns = ['&host1', '&host2']
    result = order_patterns(patterns)
    assert result == ['all', '&host1', '&host2']

    # Test with mixed empty and valid patterns
    patterns = ['', 'host1', '&host2', '', '!host3']
    result = order_patterns(patterns)
    assert result == ['host1', '&host2', '!host3']

    # Test with empty patterns list
    patterns = []
    result = order_patterns(patterns)
    assert result == ['all']

    # Test with only empty patterns
    patterns = ['', '', '']
    result = order_patterns(patterns)
    assert result == ['all']
