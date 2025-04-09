# file: flutes/iterator.py:263-273
# asked: {"lines": [263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273], "branches": [[264, 265], [264, 266], [267, 268], [267, 269], [269, 0], [269, 270]]}
# gained: {"lines": [263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273], "branches": [[264, 265], [264, 266], [267, 268], [267, 269], [269, 0], [269, 270]]}

import pytest
from flutes.iterator import LazyList

def test_fetch_until_exhausted():
    lazy_list = LazyList(iter([1, 2, 3]))
    lazy_list.exhausted = True
    lazy_list._fetch_until(1)
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

def test_fetch_until_valid_index():
    lazy_list = LazyList(iter([1, 2, 3, 4, 5]))
    lazy_list._fetch_until(2)
    assert lazy_list.list == [1, 2, 3]
    assert not lazy_list.exhausted

def test_fetch_until_stop_iteration():
    lazy_list = LazyList(iter([1, 2, 3]))
    lazy_list._fetch_until(5)
    assert lazy_list.list == [1, 2, 3]
    assert lazy_list.exhausted
