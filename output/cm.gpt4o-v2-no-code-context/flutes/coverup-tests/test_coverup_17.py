# file: flutes/iterator.py:258-261
# asked: {"lines": [258, 259, 260, 261], "branches": [[259, 260], [259, 261]]}
# gained: {"lines": [258, 259, 260, 261], "branches": [[259, 260], [259, 261]]}

import pytest
from flutes.iterator import LazyList

class TestLazyList:
    def test_iter_exhausted(self, mocker):
        # Create a LazyList instance with an empty iterable and mock its attributes
        lazy_list = LazyList(iterable=[])
        lazy_list.exhausted = True
        lazy_list.list = [1, 2, 3]
        
        # Call __iter__ and check if it returns an iterator over the list
        iterator = iter(lazy_list)
        assert list(iterator) == [1, 2, 3]

    def test_iter_not_exhausted(self, mocker):
        # Mock the LazyListIterator class
        mock_lazy_list_iterator = mocker.patch('flutes.iterator.LazyList.LazyListIterator')
        
        # Create a LazyList instance with an empty iterable and mock its attributes
        lazy_list = LazyList(iterable=[])
        lazy_list.exhausted = False
        
        # Call __iter__ and check if it returns a LazyListIterator instance
        iterator = iter(lazy_list)
        mock_lazy_list_iterator.assert_called_once_with(lazy_list)
        assert iterator == mock_lazy_list_iterator.return_value
