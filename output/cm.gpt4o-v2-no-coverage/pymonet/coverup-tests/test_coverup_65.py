# file: pymonet/utils.py:54-56
# asked: {"lines": [54, 55, 56], "branches": []}
# gained: {"lines": [54, 55, 56], "branches": []}

import pytest
from pymonet.utils import curried_map

def test_curried_map_full_coverage():
    # Test curried_map with a simple mapper and collection
    mapper = lambda x: x * 2
    collection = [1, 2, 3]
    curried_function = curried_map(mapper)
    result = curried_function(collection)
    assert result == [2, 4, 6]

    # Test curried_map with an empty collection
    collection = []
    result = curried_map(mapper)(collection)
    assert result == []

    # Test curried_map with a different mapper
    mapper = lambda x: x + 1
    collection = [1, 2, 3]
    result = curried_map(mapper)(collection)
    assert result == [2, 3, 4]

    # Test curried_map with a single item collection
    collection = [5]
    result = curried_map(mapper)(collection)
    assert result == [6]

    # Test curried_map with a more complex mapper
    mapper = lambda x: x ** 2
    collection = [1, 2, 3, 4]
    result = curried_map(mapper)(collection)
    assert result == [1, 4, 9, 16]
