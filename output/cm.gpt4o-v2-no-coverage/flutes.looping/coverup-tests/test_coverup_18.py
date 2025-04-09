# file: flutes/iterator.py:237-251
# asked: {"lines": [237, 238, 239, 240, 242, 243, 245, 246, 247, 248, 249, 250, 251], "branches": []}
# gained: {"lines": [237, 238, 239, 240, 242, 243, 245, 246, 247, 248, 249, 250, 251], "branches": []}

import pytest
from flutes.iterator import LazyList

def test_lazy_list_iterator():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    iterator = lazy_list.LazyListIterator(lazy_list)
    
    assert iter(iterator) is iterator
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    with pytest.raises(StopIteration):
        next(iterator)

def test_lazy_list_fetch_until():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    lazy_list._fetch_until(1)
    assert lazy_list.list == [1, 2]
    
    lazy_list._fetch_until(None)
    assert lazy_list.list == [1, 2, 3]
    assert lazy_list.exhausted

def test_lazy_list_getitem():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    assert lazy_list[0] == 1
    assert lazy_list[1] == 2
    assert lazy_list[2] == 3
    assert lazy_list[:] == [1, 2, 3]
    with pytest.raises(IndexError):
        _ = lazy_list[3]

def test_lazy_list_len():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    with pytest.raises(TypeError):
        len(lazy_list)
    
    lazy_list._fetch_until(None)
    assert len(lazy_list) == 3

def test_lazy_list_iter():
    data = [1, 2, 3]
    lazy_list = LazyList(data)
    
    iter_list = list(iter(lazy_list))
    assert iter_list == [1, 2, 3]
    
    lazy_list._fetch_until(None)
    iter_list = list(iter(lazy_list))
    assert iter_list == [1, 2, 3]
