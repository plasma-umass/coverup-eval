# file: f030/__init__.py:1-3
# asked: {"lines": [1, 3], "branches": []}
# gained: {"lines": [1, 3], "branches": []}

import pytest
from f030 import get_positive

def test_get_positive_with_positive_numbers():
    assert get_positive([1, 2, 3]) == [1, 2, 3]

def test_get_positive_with_negative_numbers():
    assert get_positive([-1, -2, -3]) == []

def test_get_positive_with_mixed_numbers():
    assert get_positive([-1, 0, 1, 2, -2]) == [1, 2]

def test_get_positive_with_empty_list():
    assert get_positive([]) == []

def test_get_positive_with_no_positive_numbers():
    assert get_positive([-1, -2, 0]) == []
