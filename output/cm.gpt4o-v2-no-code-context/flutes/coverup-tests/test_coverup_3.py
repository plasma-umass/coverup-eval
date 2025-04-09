# file: flutes/iterator.py:281-286
# asked: {"lines": [281, 282, 283, 285, 286], "branches": [[282, 283], [282, 285]]}
# gained: {"lines": [281, 282, 283, 285, 286], "branches": [[282, 283], [282, 285]]}

import pytest
from flutes.iterator import LazyList

class TestLazyList:
    @pytest.fixture
    def lazy_list(self):
        class MockLazyList(LazyList):
            def __init__(self):
                self.list = [1, 2, 3, 4, 5]
                self.fetched_until = None

            def _fetch_until(self, idx):
                self.fetched_until = idx

        return MockLazyList()

    def test_getitem_slice(self, lazy_list):
        result = lazy_list[:3]
        assert result == [1, 2, 3]
        assert lazy_list.fetched_until == 3

    def test_getitem_index(self, lazy_list):
        result = lazy_list[2]
        assert result == 3
        assert lazy_list.fetched_until == 2
