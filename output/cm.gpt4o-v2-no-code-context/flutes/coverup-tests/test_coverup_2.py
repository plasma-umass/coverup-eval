# file: flutes/iterator.py:253-256
# asked: {"lines": [253, 254, 255, 256], "branches": []}
# gained: {"lines": [253, 254, 255, 256], "branches": []}

import pytest
from flutes.iterator import LazyList

def test_lazylist_initialization():
    # Test initialization with an empty iterable
    lazy_list = LazyList([])
    assert lazy_list.exhausted == False
    assert lazy_list.list == []

    # Test initialization with a non-empty iterable
    lazy_list = LazyList([1, 2, 3])
    assert lazy_list.exhausted == False
    assert lazy_list.list == []

    # Test initialization with a generator
    lazy_list = LazyList((x for x in range(3)))
    assert lazy_list.exhausted == False
    assert lazy_list.list == []
