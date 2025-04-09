# file: pymonet/utils.py:54-56
# asked: {"lines": [54, 55, 56], "branches": []}
# gained: {"lines": [54, 55, 56], "branches": []}

import pytest
from pymonet.utils import curried_map
from pymonet.utils import curry

def test_curried_map_with_collection():
    def mapper(x):
        return x * 2

    collection = [1, 2, 3]
    result = curried_map(mapper, collection)
    assert result == [2, 4, 6]

def test_curried_map_with_empty_collection():
    def mapper(x):
        return x * 2

    collection = []
    result = curried_map(mapper, collection)
    assert result == []

def test_curried_map_with_curry(monkeypatch):
    def mapper(x):
        return x * 2

    collection = [1, 2, 3]
    curried_function = curried_map(mapper)
    result = curried_function(collection)
    assert result == [2, 4, 6]
