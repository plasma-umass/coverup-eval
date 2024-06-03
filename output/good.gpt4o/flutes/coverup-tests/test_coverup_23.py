# file flutes/iterator.py:288-292
# lines [289, 290, 292]
# branches ['289->290', '289->292']

import pytest
from flutes.iterator import LazyList

class TestLazyList:
    def test_len_before_exhaustion(self):
        lazy_list = LazyList(iterable=iter([1, 2, 3]))
        lazy_list.exhausted = False
        lazy_list.list = [1, 2, 3]
        
        with pytest.raises(TypeError, match="__len__ is not available before the iterable is depleted"):
            len(lazy_list)
    
    def test_len_after_exhaustion(self):
        lazy_list = LazyList(iterable=iter([1, 2, 3]))
        lazy_list.exhausted = True
        lazy_list.list = [1, 2, 3]
        
        assert len(lazy_list) == 3
