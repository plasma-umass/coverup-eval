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
    assert lazy_list[1] == 2
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
    
    with pytest.raises(TypeError):
        len(lazy_list)
    
    # Exhaust the iterator
    _ = lazy_list[:]
    
    assert len(lazy_list) == 5

def test_lazylist_fetch_until():
    data = [1, 2, 3, 4, 5]
    lazy_list = LazyList(data)
    
    lazy_list._fetch_until(2)
    assert lazy_list.list == [1, 2, 3]
    
    lazy_list._fetch_until(None)
    assert lazy_list.list == [1, 2, 3, 4, 5]
    assert lazy_list.exhausted

    lazy_list._fetch_until(10)  # Should not raise an error even if idx is out of range
