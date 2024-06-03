# file flutes/iterator.py:281-286
# lines [282, 283, 285, 286]
# branches ['282->283', '282->285']

import pytest
from flutes.iterator import LazyList

class TestLazyList:
    @pytest.fixture
    def lazy_list(self, mocker):
        # Mock the _fetch_until method to avoid side effects
        mocker.patch.object(LazyList, '_fetch_until', autospec=True)
        # Create a LazyList instance with a pre-populated list
        lazy_list = LazyList(iterable=[])
        lazy_list.list = [1, 2, 3, 4, 5]
        return lazy_list

    def test_getitem_slice(self, lazy_list):
        # Accessing a slice should call _fetch_until with the stop index
        result = lazy_list[:3]
        lazy_list._fetch_until.assert_called_once_with(lazy_list, 3)
        assert result == [1, 2, 3]

    def test_getitem_index(self, lazy_list):
        # Accessing a single index should call _fetch_until with that index
        result = lazy_list[2]
        lazy_list._fetch_until.assert_called_once_with(lazy_list, 2)
        assert result == 3
