# file flutes/iterator.py:237-251
# lines [237, 238, 239, 240, 242, 243, 245, 246, 247, 248, 249, 250, 251]
# branches []

import pytest
from flutes.iterator import LazyList

def test_lazy_list_iterator():
    class TestLazyList(LazyList[int]):
        def __init__(self, data):
            self.data = data

        def __getitem__(self, index):
            return self.data[index]

        def __len__(self):
            return len(self.data)

    data = [1, 2, 3, 4, 5]
    lazy_list = TestLazyList(data)
    iterator = lazy_list.LazyListIterator(lazy_list)

    # Test __iter__ method
    assert iter(iterator) is iterator

    # Test __next__ method
    result = []
    for item in iterator:
        result.append(item)
    assert result == data

    # Test StopIteration
    with pytest.raises(StopIteration):
        next(iterator)

    # Test weak reference cleanup
    del lazy_list
    with pytest.raises(TypeError):
        next(iterator)
