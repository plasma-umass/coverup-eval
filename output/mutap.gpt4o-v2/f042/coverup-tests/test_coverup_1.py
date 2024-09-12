# file: f042/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f042 import incr_list

def test_incr_list():
    # Test with an empty list
    assert incr_list([]) == []

    # Test with a list of integers
    assert incr_list([1, 2, 3]) == [2, 3, 4]

    # Test with a list of negative integers
    assert incr_list([-1, -2, -3]) == [0, -1, -2]

    # Test with a list of mixed integers
    assert incr_list([0, -1, 1]) == [1, 0, 2]
