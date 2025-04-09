# file flutes/iterator.py:237-251
# lines [237, 238, 239, 240, 242, 243, 245, 246, 247, 248, 249, 250, 251]
# branches []

import pytest
import weakref
from flutes.iterator import LazyList

def test_lazy_list_iterator():
    lazy_list = LazyList([1, 2, 3])
    iterator = LazyList.LazyListIterator(lazy_list)
    
    # Test that the iterator can iterate over the LazyList
    assert list(iterator) == [1, 2, 3]
    
    # Test that the iterator raises StopIteration after the list is exhausted
    with pytest.raises(StopIteration):
        next(iterator)

    # Test that the iterator does not hold a strong reference to the LazyList
    weak_lazy_list = weakref.ref(lazy_list)
    del lazy_list
    assert weak_lazy_list() is None, "LazyList should be garbage collected"

def test_lazy_list_iterator_empty():
    empty_lazy_list = LazyList([])
    iterator = LazyList.LazyListIterator(empty_lazy_list)
    
    # Test that the iterator raises StopIteration immediately for an empty LazyList
    with pytest.raises(StopIteration):
        next(iterator)
