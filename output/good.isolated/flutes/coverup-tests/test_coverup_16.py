# file flutes/iterator.py:275-276
# lines [275, 276]
# branches []

import pytest
from flutes.iterator import LazyList

class TestLazyList:
    def test_getitem_with_int(self):
        class TestLazyListImpl(LazyList):
            def __init__(self):
                self.items = [0, 1, 2, 3, 4, 5]

            def __getitem__(self, idx):
                return self.items[idx]

        lazy_list = TestLazyListImpl()
        result = lazy_list[3]  # Use an integer index
        
        # Verify that the result is as expected
        assert result == 3
