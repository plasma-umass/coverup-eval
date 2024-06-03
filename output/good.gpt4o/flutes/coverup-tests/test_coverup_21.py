# file flutes/iterator.py:258-261
# lines [259, 260, 261]
# branches ['259->260', '259->261']

import pytest
from flutes.iterator import LazyList

class TestLazyList:
    def test_lazy_list_exhausted(self, mocker):
        # Create a mock LazyList instance
        lazy_list = LazyList(iterable=[])
        lazy_list.exhausted = True
        lazy_list.list = [1, 2, 3]
        
        # Mock the LazyListIterator to ensure it is not called
        mocker.patch.object(lazy_list, 'LazyListIterator', autospec=True)
        
        # Test the __iter__ method
        iterator = iter(lazy_list)
        
        # Verify that the iterator is indeed an iterator over lazy_list.list
        assert list(iterator) == [1, 2, 3]
        lazy_list.LazyListIterator.assert_not_called()
