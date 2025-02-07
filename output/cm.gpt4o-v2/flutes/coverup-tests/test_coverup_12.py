# file: flutes/iterator.py:275-276
# asked: {"lines": [275, 276], "branches": []}
# gained: {"lines": [275, 276], "branches": []}

import pytest
from flutes.iterator import LazyList

def test_lazy_list_getitem_overload():
    data = [1, 2, 3, 4, 5]
    lazy_list = LazyList(data)
    
    # Test integer index
    assert lazy_list[0] == 1
    assert lazy_list[4] == 5
    
    # Test slice index
    assert lazy_list[1:3] == [2, 3]
    assert lazy_list[:2] == [1, 2]
    assert lazy_list[3:] == [4, 5]
    
    # Ensure the list is fully iterated
    assert lazy_list.list == data
