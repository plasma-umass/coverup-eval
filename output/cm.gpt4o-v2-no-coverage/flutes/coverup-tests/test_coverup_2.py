# file: flutes/iterator.py:253-256
# asked: {"lines": [253, 254, 255, 256], "branches": []}
# gained: {"lines": [253, 254, 255, 256], "branches": []}

import pytest
from typing import List
from flutes.iterator import LazyList

def test_lazylist_init():
    iterable = [1, 2, 3]
    lazy_list = LazyList(iterable)
    
    assert not lazy_list.exhausted
    assert lazy_list.list == []
    assert list(lazy_list.iter) == iterable
