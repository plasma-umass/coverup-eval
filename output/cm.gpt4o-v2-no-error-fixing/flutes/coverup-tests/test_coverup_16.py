# file: flutes/iterator.py:258-261
# asked: {"lines": [258, 259, 260, 261], "branches": [[259, 260], [259, 261]]}
# gained: {"lines": [258, 259, 260, 261], "branches": [[259, 260], [259, 261]]}

import pytest
from flutes.iterator import LazyList

def test_lazylist_iter_exhausted():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    # Exhaust the LazyList
    for _ in lazy_list:
        pass
    
    # Now the LazyList should be exhausted
    assert lazy_list.exhausted is True
    
    # Test the __iter__ method when exhausted
    iter_list = list(iter(lazy_list))
    assert iter_list == data

def test_lazylist_iter_not_exhausted():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    # Test the __iter__ method when not exhausted
    iterator = iter(lazy_list)
    assert isinstance(iterator, LazyList.LazyListIterator)
