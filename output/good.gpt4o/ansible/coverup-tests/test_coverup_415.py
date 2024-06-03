# file lib/ansible/module_utils/common/collections.py:100-112
# lines [100, 107, 108, 109, 110, 111, 112]
# branches ['107->108', '107->109', '110->111', '110->112']

import pytest
from ansible.module_utils.common.collections import count

def is_iterable(obj):
    """Helper function to check if an object is iterable."""
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def test_count_with_iterable():
    seq = [1, 2, 2, 3, 3, 3]
    expected = {1: 1, 2: 2, 3: 3}
    result = count(seq)
    assert result == expected

def test_count_with_non_iterable():
    with pytest.raises(Exception, match='Argument provided  is not an iterable'):
        count(123)

def test_count_with_empty_iterable():
    seq = []
    expected = {}
    result = count(seq)
    assert result == expected
