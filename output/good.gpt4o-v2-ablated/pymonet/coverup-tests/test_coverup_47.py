# file: pymonet/utils.py:54-56
# asked: {"lines": [54, 55, 56], "branches": []}
# gained: {"lines": [54, 55, 56], "branches": []}

import pytest
from pymonet.utils import curried_map

def test_curried_map_basic():
    mapper = lambda x: x * 2
    collection = [1, 2, 3]
    result = curried_map(mapper, collection)
    assert result == [2, 4, 6]

def test_curried_map_empty_collection():
    mapper = lambda x: x * 2
    collection = []
    result = curried_map(mapper, collection)
    assert result == []

def test_curried_map_with_strings():
    mapper = lambda x: x.upper()
    collection = ['a', 'b', 'c']
    result = curried_map(mapper, collection)
    assert result == ['A', 'B', 'C']

def test_curried_map_partial_application():
    mapper = lambda x: x + 1
    curried = curried_map(mapper)
    collection = [1, 2, 3]
    result = curried(collection)
    assert result == [2, 3, 4]
