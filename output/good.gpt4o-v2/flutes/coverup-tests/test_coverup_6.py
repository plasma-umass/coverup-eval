# file: flutes/iterator.py:237-251
# asked: {"lines": [237, 238, 239, 240, 242, 243, 245, 246, 247, 248, 249, 250, 251], "branches": []}
# gained: {"lines": [237, 238, 239, 240, 242, 243, 245, 246, 247, 248, 249, 250, 251], "branches": []}

import pytest
from flutes.iterator import LazyList

def test_lazy_list_iterator():
    data = [1, 2, 3, 4]
    lazy_list = LazyList(data)
    iterator = lazy_list.LazyListIterator(lazy_list)

    # Test __iter__ method
    assert iter(iterator) is iterator

    # Test __next__ method
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 4

    # Test StopIteration
    with pytest.raises(StopIteration):
        next(iterator)
