# file: flutes/iterator.py:253-256
# asked: {"lines": [253, 254, 255, 256], "branches": []}
# gained: {"lines": [253, 254, 255, 256], "branches": []}

import pytest
from flutes.iterator import LazyList

def test_lazylist_init():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    assert hasattr(lazy_list, 'iter')
    assert hasattr(lazy_list, 'exhausted')
    assert hasattr(lazy_list, 'list')
    assert lazy_list.exhausted == False
    assert lazy_list.list == []
    assert list(lazy_list.iter) == data
