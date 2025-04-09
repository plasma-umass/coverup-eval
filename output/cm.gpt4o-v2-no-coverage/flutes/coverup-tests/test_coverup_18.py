# file: flutes/iterator.py:275-276
# asked: {"lines": [275, 276], "branches": []}
# gained: {"lines": [275, 276], "branches": []}

import pytest
from typing import List
from flutes.iterator import LazyList

def test_lazylist_getitem_int():
    data = [1, 2, 3, 4, 5]
    lazy_list = LazyList(data)
    assert lazy_list[0] == 1
    assert lazy_list[4] == 5
    with pytest.raises(IndexError):
        _ = lazy_list[5]

def test_lazylist_getitem_slice():
    data = [1, 2, 3, 4, 5]
    lazy_list = LazyList(data)
    assert lazy_list[1:3] == [2, 3]
    assert lazy_list[:2] == [1, 2]
    assert lazy_list[3:] == [4, 5]
    assert lazy_list[:] == [1, 2, 3, 4, 5]

def test_lazylist_len():
    data = [1, 2, 3, 4, 5]
    lazy_list = LazyList(data)
    # Exhaust the iterable
    for _ in lazy_list:
        pass
    assert len(lazy_list) == 5
