# file: flutes/iterator.py:288-292
# asked: {"lines": [289, 290, 292], "branches": [[289, 290], [289, 292]]}
# gained: {"lines": [289, 290, 292], "branches": [[289, 290], [289, 292]]}

import pytest
from flutes.iterator import LazyList

class TestLazyList:
    @pytest.fixture
    def lazy_list(self):
        class TestLazyList(LazyList):
            def __init__(self):
                self.exhausted = False
                self.list = []

        return TestLazyList()

    def test_len_exhausted(self, lazy_list):
        lazy_list.exhausted = True
        lazy_list.list = [1, 2, 3]
        assert len(lazy_list) == 3

    def test_len_not_exhausted(self, lazy_list):
        lazy_list.exhausted = False
        with pytest.raises(TypeError, match="__len__ is not available before the iterable is depleted"):
            len(lazy_list)
