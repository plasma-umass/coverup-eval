# file: pymonet/utils.py:59-61
# asked: {"lines": [59, 60, 61], "branches": []}
# gained: {"lines": [59, 60, 61], "branches": []}

import pytest
from pymonet.utils import curried_filter

def test_curried_filter():
    def is_even(n):
        return n % 2 == 0

    collection = [1, 2, 3, 4, 5, 6]
    expected_result = [2, 4, 6]

    curried = curried_filter(is_even)
    result = curried(collection)

    assert result == expected_result

