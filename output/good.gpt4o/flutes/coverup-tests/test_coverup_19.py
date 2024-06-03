# file flutes/iterator.py:263-273
# lines [264, 265, 266, 267, 268, 269, 270, 271, 272, 273]
# branches ['264->265', '264->266', '267->268', '267->269', '269->exit', '269->270']

import pytest
from flutes.iterator import LazyList

class TestLazyList:
    def test_fetch_until_exhausted(self):
        # Create a LazyList with an exhausted iterator
        lazy_list = LazyList(iter([]))
        lazy_list.exhausted = True
        lazy_list._fetch_until(0)
        assert lazy_list.exhausted is True

    def test_fetch_until_negative_index(self):
        # Create a LazyList with a non-empty iterator
        lazy_list = LazyList(iter([1, 2, 3]))
        lazy_list._fetch_until(-1)
        assert len(lazy_list.list) == 3
        assert lazy_list.list == [1, 2, 3]

    def test_fetch_until_stop_iteration(self):
        # Create a LazyList with an iterator that will raise StopIteration
        lazy_list = LazyList(iter([1, 2, 3]))
        lazy_list._fetch_until(5)
        assert lazy_list.exhausted is True
        assert len(lazy_list.list) == 3
        assert lazy_list.list == [1, 2, 3]
        with pytest.raises(AttributeError):
            _ = lazy_list.iter

    def test_fetch_until_none_index(self):
        # Create a LazyList with a non-empty iterator
        lazy_list = LazyList(iter([1, 2, 3]))
        lazy_list._fetch_until(None)
        assert lazy_list.exhausted is True
        assert len(lazy_list.list) == 3
        assert lazy_list.list == [1, 2, 3]
