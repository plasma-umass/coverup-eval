# file: flutes/iterator.py:237-251
# asked: {"lines": [243], "branches": []}
# gained: {"lines": [243], "branches": []}

import pytest
from flutes.iterator import LazyList

def test_lazy_list_iterator():
    data = [1, 2, 3, 4]
    lazy_list = LazyList(data)
    iterator = lazy_list.LazyListIterator(lazy_list)
    
    assert iter(iterator) is iterator
    
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 4
    
    with pytest.raises(StopIteration):
        next(iterator)
