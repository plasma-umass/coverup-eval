# file: f057/__init__.py:1-5
# asked: {"lines": [1, 3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [1, 3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest
from f057 import monotonic

def test_monotonic_sorted_list():
    assert monotonic([1, 2, 3, 4, 5]) == True

def test_monotonic_reverse_sorted_list():
    assert monotonic([5, 4, 3, 2, 1]) == True

def test_monotonic_unsorted_list():
    assert monotonic([1, 3, 2, 4, 5]) == False
