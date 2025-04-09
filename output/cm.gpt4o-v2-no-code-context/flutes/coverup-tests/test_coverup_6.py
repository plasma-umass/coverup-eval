# file: flutes/iterator.py:237-251
# asked: {"lines": [237, 238, 239, 240, 242, 243, 245, 246, 247, 248, 249, 250, 251], "branches": []}
# gained: {"lines": [237, 238, 239, 240, 242, 243, 245, 246, 247, 248, 249, 250, 251], "branches": []}

import pytest
from flutes.iterator import LazyList

class TestLazyList:
    def test_lazy_list_iterator(self):
        # Create a LazyList instance with some elements
        lazy_list = LazyList([1, 2, 3])

        # Create an iterator from the LazyList
        iterator = lazy_list.LazyListIterator(lazy_list)

        # Test the __iter__ method
        assert iter(iterator) is iterator

        # Test the __next__ method
        assert next(iterator) == 1
        assert next(iterator) == 2
        assert next(iterator) == 3

        # Test StopIteration is raised after the last element
        with pytest.raises(StopIteration):
            next(iterator)
