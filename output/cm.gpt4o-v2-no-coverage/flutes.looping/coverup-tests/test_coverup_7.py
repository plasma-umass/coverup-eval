# file: flutes/iterator.py:281-286
# asked: {"lines": [281, 282, 283, 285, 286], "branches": [[282, 283], [282, 285]]}
# gained: {"lines": [281, 282, 283, 285, 286], "branches": [[282, 283], [282, 285]]}

import pytest
from flutes.iterator import LazyList

def test_lazy_list_getitem_int():
    data = [1, 2, 3, 4, 5]
    lazy_list = LazyList(data)
    
    assert lazy_list[0] == 1
    assert lazy_list[4] == 5
    with pytest.raises(IndexError):
        _ = lazy_list[5]

def test_lazy_list_getitem_slice():
    data = [1, 2, 3, 4, 5]
    lazy_list = LazyList(data)
    
    assert lazy_list[1:3] == [2, 3]
    assert lazy_list[:2] == [1, 2]
    assert lazy_list[3:] == [4, 5]
    assert lazy_list[:] == [1, 2, 3, 4, 5]
