# file flutes/iterator.py:360-401
# lines [360, 361, 382, 383, 384, 386, 387, 389, 390, 392, 393, 394, 395, 397, 398, 400, 401]
# branches ['393->394', '393->395']

import pytest
from flutes.iterator import MapList

def test_maplist_getitem_slice():
    # Setup
    a = [1, 2, 3, 4, 5]
    func = lambda x: x * x
    map_list = MapList(func, a)

    # Exercise
    result_slice = map_list[1:4]

    # Verify
    assert result_slice == [4, 9, 16], "The result should be a list of squared values"

    # Cleanup - nothing to do since there are no side effects

def test_maplist_getitem_int():
    # Setup
    a = [1, 2, 3, 4, 5]
    func = lambda x: x * x
    map_list = MapList(func, a)

    # Exercise
    result_int = map_list[2]

    # Verify
    assert result_int == 9, "The result should be the square of the third element"

    # Cleanup - nothing to do since there are no side effects

# The following test is not necessary for coverage but ensures that __iter__ and __len__ are working correctly.
def test_maplist_iter_len():
    # Setup
    a = [1, 2, 3, 4, 5]
    func = lambda x: x * 2
    map_list = MapList(func, a)

    # Exercise
    result_iter = list(iter(map_list))
    result_len = len(map_list)

    # Verify
    assert result_iter == [2, 4, 6, 8, 10], "The result should be a list of doubled values"
    assert result_len == 5, "The length should be equal to the length of the original list"

    # Cleanup - nothing to do since there are no side effects
