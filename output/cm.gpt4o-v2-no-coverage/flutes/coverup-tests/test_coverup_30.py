# file: flutes/iterator.py:263-273
# asked: {"lines": [268], "branches": [[267, 268]]}
# gained: {"lines": [268], "branches": [[267, 268]]}

import pytest
from typing import List

from flutes.iterator import LazyList

def test_fetch_until_exhausted():
    lazy_list = LazyList(iter([1, 2, 3]))
    lazy_list.exhausted = True
    lazy_list._fetch_until(0)
    assert lazy_list.list == []

def test_fetch_until_negative_index():
    lazy_list = LazyList(iter([1, 2, 3]))
    lazy_list._fetch_until(-1)
    assert lazy_list.list == [1, 2, 3]
    assert lazy_list.exhausted

def test_fetch_until_none_index():
    lazy_list = LazyList(iter([1, 2, 3]))
    lazy_list._fetch_until(None)
    assert lazy_list.list == [1, 2, 3]
    assert lazy_list.exhausted

def test_fetch_until_positive_index():
    lazy_list = LazyList(iter([1, 2, 3, 4, 5]))
    lazy_list._fetch_until(2)
    assert lazy_list.list == [1, 2, 3]
    assert not lazy_list.exhausted

def test_fetch_until_stop_iteration():
    lazy_list = LazyList(iter([1, 2, 3]))
    lazy_list._fetch_until(5)
    assert lazy_list.list == [1, 2, 3]
    assert lazy_list.exhausted
