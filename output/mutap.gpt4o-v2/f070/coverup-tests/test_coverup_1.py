# file: f070/__init__.py:1-8
# asked: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8]]}

import pytest
from f070.__init__ import strange_sort_list

def test_strange_sort_list():
    # Test with a mixed list of integers
    lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [1, 9, 1, 6, 2, 5, 3, 5, 3, 5, 4]
    assert strange_sort_list(lst) == expected

    # Test with an empty list
    lst = []
    expected = []
    assert strange_sort_list(lst) == expected

    # Test with a list of one element
    lst = [42]
    expected = [42]
    assert strange_sort_list(lst) == expected

    # Test with a list of two elements
    lst = [2, 1]
    expected = [1, 2]
    assert strange_sort_list(lst) == expected

    # Test with a list of identical elements
    lst = [7, 7, 7, 7]
    expected = [7, 7, 7, 7]
    assert strange_sort_list(lst) == expected

    # Test with a list of negative and positive integers
    lst = [-1, -3, 2, 1, -2, 3]
    expected = [-3, 3, -2, 2, -1, 1]
    assert strange_sort_list(lst) == expected
