# file: flutes/iterator.py:253-256
# asked: {"lines": [253, 254, 255, 256], "branches": []}
# gained: {"lines": [253, 254, 255, 256], "branches": []}

import pytest
from typing import Iterable
from flutes.iterator import LazyList

def test_lazylist_init():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    assert hasattr(lazy_list, 'iter')
    assert hasattr(lazy_list, 'exhausted')
    assert hasattr(lazy_list, 'list')
    assert lazy_list.exhausted == False
    assert lazy_list.list == []

    # Clean up
    del lazy_list

@pytest.fixture
def lazy_list():
    data = [1, 2, 3]
    return LazyList(data)

def test_lazylist_iter(lazy_list):
    iterator = iter(lazy_list)
    assert hasattr(iterator, '__next__')

def test_lazylist_fetch_until(lazy_list):
    lazy_list._fetch_until(2)
    assert len(lazy_list.list) >= 2

def test_lazylist_getitem(lazy_list):
    item = lazy_list[0]
    assert item == 1

def test_lazylist_len(lazy_list):
    # Exhaust the iterator to allow __len__ to work
    for _ in lazy_list:
        pass
    length = len(lazy_list)
    assert length == 3
