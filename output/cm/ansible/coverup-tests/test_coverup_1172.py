# file lib/ansible/inventory/manager.py:66-91
# lines [70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 86, 87, 91]
# branches ['73->74', '73->86', '74->75', '74->77', '77->78', '77->79', '79->80', '79->82', '86->87', '86->91']

import pytest

# Assuming the function order_patterns is a standalone function and not a method of InventoryManager
from ansible.inventory.manager import order_patterns

def test_order_patterns():
    patterns = ['!exclude', '&intersection', 'regular']
    ordered_patterns = order_patterns(patterns)
    assert ordered_patterns == ['regular', '&intersection', '!exclude']

    patterns = ['!exclude', '&intersection']
    ordered_patterns = order_patterns(patterns)
    assert ordered_patterns == ['all', '&intersection', '!exclude']

    patterns = ['']
    ordered_patterns = order_patterns(patterns)
    assert ordered_patterns == ['all']

    patterns = []
    ordered_patterns = order_patterns(patterns)
    assert ordered_patterns == ['all']
