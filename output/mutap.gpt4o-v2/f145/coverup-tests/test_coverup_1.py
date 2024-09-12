# file: f145/__init__.py:1-9
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8, 9], "branches": [[5, 5], [5, 6]]}

import pytest
from f145 import order_by_points

def test_order_by_points():
    # Test with positive numbers
    nums = [123, 456, 789]
    sorted_nums = order_by_points(nums)
    assert sorted_nums == [123, 456, 789]

    # Test with negative numbers
    nums = [-123, -456, -789]
    sorted_nums = order_by_points(nums)
    assert sorted_nums == [-123, -456, -789]

    # Test with mixed positive and negative numbers
    nums = [123, -456, 789, -101]
    sorted_nums = order_by_points(nums)
    assert sorted_nums == [-101, 123, -456, 789]

    # Test with zero
    nums = [0, 123, -456]
    sorted_nums = order_by_points(nums)
    assert sorted_nums == [0, 123, -456]

    # Test with single element
    nums = [5]
    sorted_nums = order_by_points(nums)
    assert sorted_nums == [5]

    # Test with empty list
    nums = []
    sorted_nums = order_by_points(nums)
    assert sorted_nums == []

