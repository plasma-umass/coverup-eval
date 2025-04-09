# file: pymonet/utils.py:64-78
# asked: {"lines": [64, 65, 76, 77, 78], "branches": [[76, 0], [76, 77], [77, 76], [77, 78]]}
# gained: {"lines": [64, 65, 76, 77, 78], "branches": [[76, 0], [76, 77], [77, 76], [77, 78]]}

import pytest
from pymonet.utils import find

def test_find_with_matching_element():
    collection = [1, 2, 3, 4]
    key = lambda x: x == 3
    result = find(collection, key)
    assert result == 3

def test_find_with_no_matching_element():
    collection = [1, 2, 3, 4]
    key = lambda x: x == 5
    result = find(collection, key)
    assert result is None

def test_find_with_empty_collection():
    collection = []
    key = lambda x: x == 1
    result = find(collection, key)
    assert result is None
