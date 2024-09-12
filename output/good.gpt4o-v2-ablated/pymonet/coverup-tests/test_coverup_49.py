# file: pymonet/utils.py:59-61
# asked: {"lines": [59, 60, 61], "branches": []}
# gained: {"lines": [59, 60, 61], "branches": []}

import pytest
from pymonet.utils import curried_filter
from pymonet.utils import curry

def test_curried_filter_all_true():
    filterer = lambda x: True
    collection = [1, 2, 3]
    result = curried_filter(filterer, collection)
    assert result == [1, 2, 3]

def test_curried_filter_all_false():
    filterer = lambda x: False
    collection = [1, 2, 3]
    result = curried_filter(filterer, collection)
    assert result == []

def test_curried_filter_mixed():
    filterer = lambda x: x % 2 == 0
    collection = [1, 2, 3, 4]
    result = curried_filter(filterer, collection)
    assert result == [2, 4]

def test_curried_filter_empty_collection():
    filterer = lambda x: True
    collection = []
    result = curried_filter(filterer, collection)
    assert result == []

def test_curried_filter_curry():
    filterer = lambda x: x > 1
    curried = curried_filter(filterer)
    collection = [0, 1, 2, 3]
    result = curried(collection)
    assert result == [2, 3]
