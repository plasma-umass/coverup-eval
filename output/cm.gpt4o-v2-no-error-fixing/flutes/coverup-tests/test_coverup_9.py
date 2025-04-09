# file: flutes/iterator.py:281-286
# asked: {"lines": [281, 282, 283, 285, 286], "branches": [[282, 283], [282, 285]]}
# gained: {"lines": [281, 282, 283, 285, 286], "branches": [[282, 283], [282, 285]]}

import pytest
from flutes.iterator import LazyList

def test_lazy_list_getitem_with_slice():
    data = range(10)
    lazy_list = LazyList(data)
    
    # Accessing a slice
    result = lazy_list[2:5]
    assert result == [2, 3, 4]

def test_lazy_list_getitem_with_index():
    data = range(10)
    lazy_list = LazyList(data)
    
    # Accessing a single index
    result = lazy_list[3]
    assert result == 3

def test_lazy_list_getitem_with_slice_out_of_bounds():
    data = range(5)
    lazy_list = LazyList(data)
    
    # Accessing a slice that goes out of bounds
    result = lazy_list[2:10]
    assert result == [2, 3, 4]

def test_lazy_list_getitem_with_index_out_of_bounds():
    data = range(5)
    lazy_list = LazyList(data)
    
    # Accessing an index that goes out of bounds
    with pytest.raises(IndexError):
        _ = lazy_list[10]
