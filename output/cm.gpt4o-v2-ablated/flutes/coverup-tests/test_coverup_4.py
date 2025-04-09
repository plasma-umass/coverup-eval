# file: flutes/iterator.py:237-251
# asked: {"lines": [239, 240, 243, 246, 247, 248, 249, 250, 251], "branches": []}
# gained: {"lines": [239, 240, 243, 246, 247, 248, 249, 250, 251], "branches": []}

import pytest
from flutes.iterator import LazyList

def test_lazy_list_iterator():
    class TestLazyList(LazyList[int]):
        def __init__(self, data):
            self.data = data

        def __getitem__(self, index):
            if index >= len(self.data):
                raise IndexError
            return self.data[index]

        def __len__(self):
            return len(self.data)

    data = [1, 2, 3]
    lazy_list = TestLazyList(data)
    iterator = lazy_list.LazyListIterator(lazy_list)

    # Test __iter__ method
    assert iter(iterator) is iterator

    # Test __next__ method
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3

    # Test StopIteration
    with pytest.raises(StopIteration):
        next(iterator)

    # Test IndexError handling
    empty_list = TestLazyList([])
    empty_iterator = empty_list.LazyListIterator(empty_list)
    with pytest.raises(StopIteration):
        next(empty_iterator)
