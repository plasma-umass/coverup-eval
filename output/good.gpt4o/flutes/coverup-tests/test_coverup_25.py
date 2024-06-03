# file flutes/iterator.py:258-261
# lines [261]
# branches ['259->261']

import pytest
from collections.abc import Iterator
from flutes.iterator import LazyList

class TestLazyList:
    def test_lazy_list_iterator(self):
        class MockLazyList(LazyList):
            def __init__(self):
                self.exhausted = False
                self.list = []
            
            class LazyListIterator(Iterator):
                def __init__(self, lazy_list):
                    self.lazy_list = lazy_list
                
                def __next__(self):
                    raise StopIteration

        lazy_list = MockLazyList()
        iterator = iter(lazy_list)
        
        assert isinstance(iterator, MockLazyList.LazyListIterator)
