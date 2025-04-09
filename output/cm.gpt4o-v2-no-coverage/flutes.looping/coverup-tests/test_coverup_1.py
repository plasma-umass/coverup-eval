# file: flutes/iterator.py:253-256
# asked: {"lines": [253, 254, 255, 256], "branches": []}
# gained: {"lines": [253, 254, 255, 256], "branches": []}

import pytest
from typing import List
from flutes.iterator import LazyList

def test_lazylist_init():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    assert isinstance(lazy_list.iter, type(iter(data)))
    assert lazy_list.exhausted is False
    assert lazy_list.list == []

