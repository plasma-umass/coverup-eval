# file pymonet/utils.py:64-78
# lines [64, 65, 76, 77, 78]
# branches ['76->exit', '76->77', '77->76', '77->78']

import pytest
from pymonet.utils import find

def test_find_returns_first_matching_element():
    collection = [1, 2, 3, 4, 5]
    key = lambda x: x > 3
    assert find(collection, key) == 4

def test_find_returns_none_when_no_match():
    collection = [1, 2, 3, 4, 5]
    key = lambda x: x > 5
    assert find(collection, key) is None

def test_find_with_empty_collection():
    collection = []
    key = lambda x: x > 3
    assert find(collection, key) is None
