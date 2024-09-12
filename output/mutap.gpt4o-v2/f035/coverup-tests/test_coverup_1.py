# file: f035/__init__.py:1-7
# asked: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest
from f035 import max_element

def test_max_element():
    # Test with a normal list
    assert max_element([1, 2, 3, 4, 5]) == 5
    # Test with a list with negative numbers
    assert max_element([-1, -2, -3, -4, -5]) == -1
    # Test with a list with mixed positive and negative numbers
    assert max_element([-1, 2, -3, 4, -5]) == 4
    # Test with a list with all elements the same
    assert max_element([1, 1, 1, 1, 1]) == 1
    # Test with a list with one element
    assert max_element([1]) == 1
    # Test with an empty list should raise an IndexError
    with pytest.raises(IndexError):
        max_element([])

