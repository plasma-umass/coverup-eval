# file flutes/iterator.py:230-236
# lines [230, 231]
# branches []

import pytest
from flutes.iterator import LazyList

def test_lazy_list():
    # Create a generator to test lazy evaluation
    def gen():
        for i in range(5):
            yield i

    lazy_list = LazyList(gen())

    # Accessing elements to trigger iteration
    assert lazy_list[0] == 0
    assert lazy_list[1] == 1
    assert lazy_list[2] == 2

    # Accessing an element that has not been iterated yet
    assert lazy_list[4] == 4

    # Accessing an element out of the range of the generator
    with pytest.raises(IndexError):
        _ = lazy_list[5]

    # Check if the length is correct
    assert len(lazy_list) == 5

    # Check if the list contains all the elements
    assert all(item in lazy_list for item in range(5))

    # Check if the list can be iterated completely
    assert list(lazy_list) == [0, 1, 2, 3, 4]

    # Check if the list supports negative indexing
    assert lazy_list[-1] == 4
    assert lazy_list[-5] == 0

    # Check if the list raises IndexError for out of range negative indexing
    with pytest.raises(IndexError):
        _ = lazy_list[-6]

    # Check if the list supports slicing
    assert lazy_list[1:3] == [1, 2]
    assert lazy_list[:3] == [0, 1, 2]
    assert lazy_list[3:] == [3, 4]
    assert lazy_list[:] == [0, 1, 2, 3, 4]

    # Check if the list supports step in slicing
    assert lazy_list[::2] == [0, 2, 4]
    assert lazy_list[1::2] == [1, 3]

    # Check if the list supports negative slicing
    assert lazy_list[-3:-1] == [2, 3]
    assert lazy_list[:-3] == [0, 1]
    assert lazy_list[-3:] == [2, 3, 4]

    # Check if the list supports negative step in slicing
    assert lazy_list[::-1] == [4, 3, 2, 1, 0]
    assert lazy_list[::-2] == [4, 2, 0]
    assert lazy_list[-2::-2] == [3, 1]

    # Check if the list supports complex slicing
    assert lazy_list[-4:-2:2] == [1]
    assert lazy_list[4:1:-2] == [4, 2]

    # Check if the list raises ValueError for zero step in slicing
    with pytest.raises(ValueError):
        _ = lazy_list[::0]
