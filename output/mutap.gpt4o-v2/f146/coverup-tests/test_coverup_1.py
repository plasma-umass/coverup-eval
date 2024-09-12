# file: f146/__init__.py:1-12
# asked: {"lines": [1, 4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}
# gained: {"lines": [1, 4, 5, 6, 7, 8, 9, 10, 12], "branches": [[5, 6], [5, 12], [6, 5], [6, 7], [9, 5], [9, 10]]}

import pytest
from f146 import specialFilter

def test_specialFilter_all_conditions_met():
    nums = [13, 15, 17, 19, 31, 35, 37, 39, 51, 53, 55, 57, 59, 71, 73, 75, 77, 79, 91, 93, 95, 97, 99]
    result = specialFilter(nums)
    assert result == len(nums)

def test_specialFilter_no_conditions_met():
    nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    result = specialFilter(nums)
    assert result == 0

def test_specialFilter_mixed_conditions():
    nums = [13, 22, 35, 44, 57, 68, 79, 80, 91, 100]
    result = specialFilter(nums)
    assert result == 5

def test_specialFilter_empty_list():
    nums = []
    result = specialFilter(nums)
    assert result == 0
