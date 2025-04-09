# file: flutes/iterator.py:263-273
# asked: {"lines": [263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273], "branches": [[264, 265], [264, 266], [267, 268], [267, 269], [269, 0], [269, 270]]}
# gained: {"lines": [263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273], "branches": [[264, 265], [264, 266], [267, 268], [267, 269], [269, 0], [269, 270]]}

import pytest
from flutes.iterator import LazyList

class TestLazyList:
    @pytest.fixture
    def lazy_list(self):
        def generator():
            for i in range(5):
                yield i
        return LazyList(generator())

    def test_fetch_until_exhausted(self, lazy_list):
        lazy_list.exhausted = True
        lazy_list._fetch_until(2)
        assert len(lazy_list.list) == 0  # No items should be fetched

    def test_fetch_until_negative_index(self, lazy_list):
        lazy_list._fetch_until(-1)
        assert len(lazy_list.list) == 5  # All items should be fetched

    def test_fetch_until_valid_index(self, lazy_list):
        lazy_list._fetch_until(2)
        assert len(lazy_list.list) == 3  # Items up to index 2 should be fetched

    def test_fetch_until_stop_iteration(self, lazy_list):
        lazy_list._fetch_until(10)
        assert len(lazy_list.list) == 5  # All items should be fetched
        assert lazy_list.exhausted is True  # Iterator should be exhausted
        with pytest.raises(AttributeError):
            _ = lazy_list.iter  # Iterator should be deleted
